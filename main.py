import sys
import os
import importlib
import multiprocessing
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
from app.command_registry import command_registry  
from app.pandas_facade import PandasFacade 

import logging
import logging.config

# Initialize PandasFacade instance to manage calculation history
history_manager = PandasFacade()

def load_environment_variables():
    load_dotenv()
    settings = {key: value for key, value in os.environ.items()}
    logging.info("Environment variables loaded.")
    logging.debug(f"Loaded environment variables: {settings}")
    return settings

def configure_logging():
    os.makedirs("logs", exist_ok=True)
    logging_conf_path = "logging.conf"
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        logging.info("Logging configuration loaded from 'logging.conf'.")
    else:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info("Default logging configuration applied.")
    logging.debug("Logging configured with detailed settings.")

def load_plugins():
    """
    Dynamically loads all command plugins from the plugins folder.
    """
    plugins_dir = os.path.join(os.path.dirname(__file__), 'app', 'plugins')
    logging.info(f"Loading plugins from directory: {plugins_dir}")
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"app.plugins.{filename[:-3]}"  
            logging.debug(f"Importing plugin: {module_name}")
            importlib.import_module(module_name)  
    logging.info("All plugins loaded successfully.")

def perform_calculation_and_display(value1, value2, operation_type):
    """
    Executes the specified arithmetic operation on two inputs using multiprocessing
    and displays the outcome.
    """
    try:
        logging.info(f"Performing calculation: {operation_type} with values {value1} and {value2}")
        
        # Convert inputs to Decimal
        decimal_value1 = Decimal(value1)
        decimal_value2 = Decimal(value2)
        logging.debug(f"Converted values to Decimal: {decimal_value1}, {decimal_value2}")

        # Get the command class from the registry
        command_class = command_registry.get(operation_type)
        if not command_class:
            logging.error(f"Invalid operation type: {operation_type}")
            print(f"Invalid operation type: {operation_type}")
            return

        # Create an instance of the command with the provided arguments
        command_instance = command_class(decimal_value1, decimal_value2)
        logging.debug(f"Command instance created: {command_instance}")

        # Set up multiprocessing to execute the command
        result_queue = multiprocessing.Queue()
        logging.info("Starting process to execute the command.")
        process = multiprocessing.Process(target=command_instance.execute_in_process, args=(result_queue,))
        process.start()
        process.join()

        # Get the result from the process
        result = result_queue.get()
        logging.info(f"Process completed. Result: {result}")

        # Display the result or handle any errors
        if isinstance(result, Exception):
            logging.error(f"An error occurred during the operation: {result}")
            print(f"An error occurred: {result}")
        else:
            logging.info(f"Calculation result: {value1} {operation_type} {value2} = {result}")
            print(f"The result of {value1} {operation_type} {value2} is {result}")
            
            # Save the calculation to the history using PandasFacade
            record = {"operation": operation_type, "num1": str(value1), "num2": str(value2), "result": str(result)}
            history_manager.add_record(record)

    except InvalidOperation:
        logging.error(f"Invalid input: {value1} or {value2} is not a valid number.")
        print(f"Invalid input: {value1} or {value2} is not a valid number.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

def display_menu():
    """
    Displays the list of available commands.
    """
    logging.info("Displaying available commands.")
    print("Available commands:", ", ".join(command_registry.keys()))
    print("Additional options: save history, load history, clear history, view history")

import statistics
from decimal import Decimal, InvalidOperation
import logging

def repl():
    """
    Interactive REPL loop for the calculator using command pattern.
    """
    print("Welcome to the Interactive Calculator. Type 'exit' to quit or 'menu' to see available commands.")
    display_menu()  # Display menu at the start

    while True:
        user_input = input("Enter command (e.g., 'mean 1 2 3 4 5' or 'save history'): ").strip()
        logging.info(f"User input received: {user_input}")

        if user_input.lower() == 'exit':
            logging.info("Exiting the REPL.")
            print("Goodbye!")
            break
        elif user_input.lower() == 'menu':
            display_menu()
            continue
        elif user_input.lower() == 'save_history':
            filepath = input("Enter file path to save history (e.g., 'history.csv'): ")
            history_manager.save_to_csv(filepath)
            logging.info(f"History saved to {filepath}.")
            print("History saved successfully.")
            continue
        elif user_input.lower() == 'load_history':
            filepath = input("Enter file path to load history (e.g., 'history.csv'): ")
            history_manager.load_from_csv(filepath)
            logging.info(f"History loaded from {filepath}.")
            print("History loaded successfully.")
            continue
        elif user_input.lower() == 'clear_history':
            history_manager.clear_data()
            logging.info("History cleared.")
            print("History cleared successfully.")
            continue
        elif user_input.lower() == 'view_history':
            logging.info("Displaying calculation history.")
            print("Calculation History:")
            print(history_manager.dataframe)
            continue
        
        # Handle command input, splitting by spaces
        parts = user_input.split()
        if len(parts) < 3:
            logging.warning(f"Invalid input format: {user_input}. Expected format: <operation> <num1> <num2>")
            print("Invalid input format. Use: <operation> <num1> <num2>")
            continue
        
        operation = parts[0]
        # For 'mean', 'stddev', and 'mode', we want to accept any number of arguments
        if operation.lower() == 'mean':
            try:
                numbers = [Decimal(num) for num in parts[1:]]
                mean_value = sum(numbers) / len(numbers)
                logging.info(f"Mean of {numbers} is {mean_value}")
                print(f"The mean of {', '.join(parts[1:])} is {mean_value}")
                
                # Save to history
                record = {"operation": "mean", "numbers": ', '.join(parts[1:]), "result": str(mean_value)}
                history_manager.add_record(record)
            except InvalidOperation as e:
                logging.error(f"Invalid number in input: {e}")
                print("Invalid number in input.")
            continue
        
        # Handle standard deviation
        elif operation.lower() == 'stddev':
            try:
                numbers = [Decimal(num) for num in parts[1:]]
                # Calculate standard deviation using statistics library
                numbers_float = [float(num) for num in numbers]  # Convert Decimal to float for statistics module
                stddev_value = statistics.stdev(numbers_float)
                logging.info(f"Standard deviation of {numbers} is {stddev_value}")
                print(f"The standard deviation of {', '.join(parts[1:])} is {stddev_value}")
                
                # Save to history
                record = {"operation": "stddev", "numbers": ', '.join(parts[1:]), "result": str(stddev_value)}
                history_manager.add_record(record)
            except InvalidOperation as e:
                logging.error(f"Invalid number in input: {e}")
                print("Invalid number in input.")
            except statistics.StatisticsError as e:
                logging.error(f"Error in calculating standard deviation: {e}")
                print("Standard deviation requires at least two numbers.")
            continue
        
        # Handle mode
        elif operation.lower() == 'mode':
            try:
                numbers = [Decimal(num) for num in parts[1:]]
                # Calculate mode using statistics library
                numbers_float = [float(num) for num in numbers]  # Convert Decimal to float for statistics module
                mode_value = statistics.mode(numbers_float)
                logging.info(f"Mode of {numbers} is {mode_value}")
                print(f"The mode of {', '.join(parts[1:])} is {mode_value}")
                
                # Save to history
                record = {"operation": "mode", "numbers": ', '.join(parts[1:]), "result": str(mode_value)}
                history_manager.add_record(record)
            except InvalidOperation as e:
                logging.error(f"Invalid number in input: {e}")
                print("Invalid number in input.")
            except statistics.StatisticsError as e:
                logging.error(f"Error in calculating mode: {e}")
                print("Mode calculation failed. Ensure there is a mode in the set.")
            continue
        
        # Otherwise handle two-number operations like add, subtract, etc.
        num1, num2 = parts[1], parts[2]
        logging.info(f"Processing command: {operation} {num1} {num2}")
        perform_calculation_and_display(num1, num2, operation)

def main():
    """
    Main function to either process command-line arguments or start the REPL loop.
    """
    # Load plugins dynamically at startup
    load_plugins()

    # If command-line arguments are provided, execute once and exit
    if len(sys.argv) == 4:
        _, value1, value2, operation_type = sys.argv
        logging.info(f"Command-line input detected: {value1}, {value2}, {operation_type}")
        perform_calculation_and_display(value1, value2, operation_type)
    else:
        # Start the REPL if no command-line arguments are provided
        logging.info("Starting REPL loop.")
        repl()

if __name__ == '__main__':
    configure_logging()
    settings = load_environment_variables()

    logging.info(f"Environment: {settings.get('ENVIRONMENT')}")
    logging.info("Application started.")
    main()

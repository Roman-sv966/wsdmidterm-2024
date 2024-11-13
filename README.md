# wsdmidterm-2024

# Advanced Python Calculator Application

## Project Overview

This Advanced Python Calculator is designed with professional software development practices, featuring a flexible, modular design that supports clean, maintainable code. Key features include a REPL interface, plugin system, calculation history management, extensive logging, and configuration via environment variables. The app also integrates several design patterns for scalability and robustness.

## Features

1. **REPL Interface**  
 A Read-Eval-Print Loop (REPL) for interactive calculations, allowing users to enter expressions and receive results immediately.

2. **Plugin System Architecture**  
   Supports dynamically loading plugins for new calculation functions, allowing feature expansion without altering core code.

3. **Calculation History Management**  
   Tracks calculation history using Pandas, enabling easy export to formats like CSV and Excel for data analysis.

4. **Design Patterns Implemented**  
   - **Facade Pattern**: Combines multiple complex functionalities, such as history tracking and file management, into a straightforward interface. This allows users to interact with history and save/load functions without needing to understand the underlying data handling or file I/O details.
   - **Command Pattern**: Packages each calculation as an object, making it easy to manage and execute operations independently. This approach allows for flexible features like undoing or redoing calculations, enhancing the interactive experience.
   - **Factory Method**: Generates different types of calculation operations without changing the core calculator code. This pattern enables the calculator to be extended with new operations, such as trigonometric or custom calculations, by simply adding new operation modules.
   - **Singleton Pattern**: Restricts instantiation of key components, like the logging manager, to a single instance. This ensures consistency across the application, especially in configurations where only one logging instance should manage all logging activities.

5. **Logging**  
   The application uses Python's built-in `logging` module to capture detailed logs at different levels (INFO, WARNING, ERROR). The logging configuration is flexible, allowing adjustment of log levels and output destinations based on the environment.

6. **Testing and Code Quality**:
   - Achieves 95% test coverage with Pytest.
   - Adheres to PEP 8 standards, with code quality verified by Pylint.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Virtual environment (`venv`)
- Git

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd <repository-folder>
2. **Create and Activate a Virtual Environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Set Up Environment Variables**:
    Create a .env file in the root folder and add the following:
    makefile
   ```bash
   ENVIRONMENT=Production
   LOG_LEVEL=INFO
   LOG_FILE=logs/application.log

### Running the Application
- **Command-Line Interface (REPL)**
   ```bash
   python main.py
- a) Use commands like `add 2 4`, `mean 8 4 4 5 6` to perform calculations.
- b) Type `menu` to see all available commands.
- c) Commands like `save_history` and `load_history` allow managing history. Add file path in the next step.
- d) Use `view_history` to view the calculation history.
- e) try `clear_history` to clear the history.

## Testing the Application
- Run the following command to test the application with coverage:
    ```bash
    pytest --cov=app --cov-report=term-missing

## Design Patterns Implemented  
   - **Facade Pattern**: Combines multiple complex functionalities, such as history tracking and file management, into a straightforward interface. This allows users to interact with history and save/load functions without needing to understand the underlying data handling or file I/O details.
   - **Command Pattern**: Packages each calculation as an object, making it easy to manage and execute operations independently. This approach allows for flexible features like undoing or redoing calculations, enhancing the interactive experience.
   - **Factory Method**: Generates different types of calculation operations without changing the core calculator code. This pattern enables the calculator to be extended with new operations, such as trigonometric or custom calculations, by simply adding new operation modules.
   - **Singleton Pattern**: Restricts instantiation of key components, like the logging manager, to a single instance. This ensures consistency across the application, especially in configurations where only one logging instance should manage all logging activities.

## Environment Variables

The application leverages environment variables to adjust its configuration settings dynamically, providing flexibility for different deployment environments. These variables can be set within a .env file.

- **LOG_LEVEL**: Determines the logging detail level (e.g., INFO, WARNING, ERROR).
- **LOG_FILE**: Specifies the location where log files will be stored.
- **ENVIRONMENT**: Defines the current environment (e.g., Production, Development) to adapt application behavior accordingly.

## Logging Configuration

The log level (`LOG_LEVEL`) and log file location (`LOG_FILE`) can be set in a `.env` file, demonstrating flexibility in setting logging behavior based on deployment or testing environments.
The application uses the `logging` module to capture different levels of log messages:

- **INFO**:Records standard application operations, such as calculation results, to track regular activity.
- **DEBUG**:Captures detailed information useful for troubleshooting and in-depth debugging.
- **WARNING**: Logs unusual but manageable events, helping to identify potential issues without disrupting functionality.
- **ERROR**: Tracks critical errors and exceptions, providing details necessary for diagnosing failures in the application.

## Error Handling

- **Easier to Ask for Forgiveness than Permission (EAFP)**: The application uses try-except blocks to catch and handle exceptions, such as invalid operations or division by zero, rather than preemptively checking for errors.
- **Look Before You Leap (LBYL)**: This approach checks the existence of configuration settings in environment variables before utilizing them, ensuring they are available.

## Testing

- **Pytest**: Achieves almost 95% coverage.
  - Includes unit tests for all files.

## Code Quality

- Verified by **Pylint** for adherence to PEP 8 standards.


---

This README provides the key information needed to understand, configure, and run the Advanced Python Calculator project. For additional details, please refer to the source code and documentation available in the repository.

---






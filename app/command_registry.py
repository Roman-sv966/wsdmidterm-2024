# app/command_registry.py

command_registry: dict[str, object] = {}

def register_command(name: str, command_class: object):
    """
    Registers a command in the global command registry.

    Args:
        name (str): The name of the command to register.
        command_class (object): The command class to associate with the name.
    """
    command_registry[name] = command_class

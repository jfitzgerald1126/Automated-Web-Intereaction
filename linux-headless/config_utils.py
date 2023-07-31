import json

def load_config():
    """
    Load configuration data from a JSON file.

    Reads the contents of 'config.json' file and parses it as a JSON object.
    The 'config.json' file is assumed to be present in the same directory
    as this script and should contain key-value pairs for configuration settings.

    Returns:
        dict: A dictionary containing the configuration data.

    Raises:
        FileNotFoundError: If 'config.json' is not found in the current directory.
        JSONDecodeError: If 'config.json' contains invalid JSON data.

    Example:
        # config.json
        {
            "username": "your_username",
            "password": "your_password",
            "api_key": "your_api_key"
        }

        # Python script
        config = load_config()
        print(config["username"])  # Output: "your_username"
        print(config["api_key"])   # Output: "your_api_key"
    """
    with open('config.json', 'r') as file:
        return json.load(file)
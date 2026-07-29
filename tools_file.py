import json

def json_file_to_dict(file_path, key_field='id', value_field='name'):
    """
    Reads a JSON file and returns its content as a dictionary.
    
    Args:
        file_path (str): The path to the JSON file.
        key_field (str): The field to use as the key in the returned dictionary.
        value_field (str): The field to use as the value in the returned dictionary.

    Returns:
        dict: The content of the JSON file as a dictionary.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        return {item[key_field]: item[value_field] for item in data}
    
    return data
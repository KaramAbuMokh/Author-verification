import os


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found at the specified path.")
        print(f"Specified file path: {file_path}")
        print(f"Current file path: {os.getcwd()}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

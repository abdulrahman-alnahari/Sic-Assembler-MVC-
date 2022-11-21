def read_file(file_name, error_message):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
    except:
        data = error_message

    return data
def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print("File Content:\n", content)
        file.close()
    except FileNotFoundError:
        print("Error: File not found")
def read_file(filename):
    try:
        file = open(filename, "r")
        print(file.read())
        file.close() 
    except:
        print("File Not Found")
        
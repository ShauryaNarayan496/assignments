# this code is reading a file and printing the content 
def read_file(filename):
    try:
        file = open(filename, "r")
        print(file.read())
        file.close() 
    except:
        print("File Not Found")
        
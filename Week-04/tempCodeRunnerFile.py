def listFiles():
    files = [ f for f in os.listdir() if f ]
    return files 
def Identify_files():
    pass
for file in listFiles():
    print(os.stat(file))
from FileSystem import FileSystem


class File(FileSystem):

    def __init__(self, name):
        self.name = name
    
    def ls(self):
        print(f"""Name of file:{self.name}""")
    
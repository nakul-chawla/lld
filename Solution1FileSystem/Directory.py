from FileSystem import FileSystem


class Directory(FileSystem):


    def __init__(self, name):
        self.name = name
        self.direc = []

    def add(self,fl):
        self.direc.append(fl)

    def ls(self):
        print(f"""Name of directory:{self.name}""")

        for x in self.direc:
            x.ls()
        
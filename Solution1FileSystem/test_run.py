from FileSystem import FileSystem
from File import File
from Directory import Directory


directory = Directory("Movie")

new_file = File("Border")

directory.add(new_file)

new_directory = Directory("Comedy Movie")
new_movie = File("Hulchal")
new_directory.add(new_movie)


directory.add(new_directory)

directory.ls()

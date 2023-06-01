from typing import NamedTuple
import pickle


class Archive_Data(NamedTuple):
    csv_file_name:str
    space_file_name:str
    input_dict:dict 
    file_create:bool
    change_archive: bool    


class Archive:
    def __init__(self, change_archive):
        self.__change_archive = change_archive
        self.__archive = []
    
    def __str__(self):
        return str(self.__change_archive)
    
    def dump(self, data):
        self.__archive.append(data)
        with open('data.pickle', 'wb') as file:
            pickle.dump(self.__archive, file)
    
    @classmethod
    def load(cls):
        with open('data.pickle', 'rb') as file:
            data = pickle.load(file)
        archive = cls(data[0].change_archive)
        archive.__archive = data
        return archive
    

# Create an Archive instance and dump some data
archive = Archive(change_archive=True)
archive.dump(Archive_Data(csv_file_name='data1.csv', space_file_name='data1.txt', input_dict={'key': 'value1'}, file_create=True, change_archive=True))
archive.dump(Archive_Data(csv_file_name='data2.csv', space_file_name='data2.txt', input_dict={'key': 'value2'}, file_create=False, change_archive=False))

# Load the data and iterate over it
archive_loaded = Archive.load()
for data in archive_loaded._Archive__archive:
    print(data)

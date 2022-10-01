#!/usr/bin/python3
"""
Serialization and deserialization of instances
"""
import json


class FileStorage:
    """
    Serializes and deserializes instances to and from json
    """
    __file_path = './file.json'
    __objects = dict()

    def all(self):
        """Returns the dictionary '__objects'
        """
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the 'obj' with the key '<object class name>.id'
        """
        self.__objects["{}.{}".format(obj['__class__'], obj['id'])] = obj

    def save(self):
        """Serializes '__objects' to the json file (__file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the json file to '__objects' onlty if the file path exists, otherwise do nothing
        """
        with open(self.__file_path, "r", encoding="utf-8") as f:
             self.__objects = json.load(f)



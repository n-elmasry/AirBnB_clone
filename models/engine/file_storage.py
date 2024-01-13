#!/usr/bin/python3
'''FileStorage that serializes instances to a JSON file and deserializes JSON file to instances'''
import json
from os.path import isfile


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """__init__"""
        pass

    # Public instance methods
    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to JSON file'''
        objs = self.__objects
        dict_obj = {}
        for obj_key, obj_value in objs.items():
            dict_obj[obj_key] = obj_value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict_obj, f)
    """
   def reload(self):
    if not isfile(self.__file_path):
        return False
    else:
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                dict_obj = json.loads(file_content)
                for key, value in dict_obj.items():
                    cls_name = value['__class__']
                    cls = getattr(__import__('models.' + cls_name, fromlist=[cls_name]), cls_name)
                    try:
                        instance = cls(**value)
                        self.__objects[key] = instance
                    except Exception:
                        pass
        except Exception as e:
            print(f"Error loading file: {e}")

        """



    def reload(self):
        """deserializes the JSON file to __objects"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    file_content = f.read()
                    dict_obj = json.loads(file_content)
                    for key, values in dict_obj.items():
                        cls_name, obj_id = key.split('.')
                        cls = getattr(models, cls_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass


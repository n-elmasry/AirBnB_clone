#!/usr/bin/python3
'''FileStorage serializes instances and deserializes JSON file to instances'''
import json
from models.base_model import BaseModel
from models.user import User
from os.path import isfile


class FileStorage:
    """serializes instances and deserializes JSON file to instance"""
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
                    cls_n = value['__class__']
                    lst = fromlist=[cls_name]
                    cls = getattr(__import__('models.' + cls_name, lst), cls_n)
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
                        # cls = getattr(models, cls_name)
                        # instance = cls(**values)
                        # FileStorage.__objects[key] = instance
                        cls = self.classes.get(cls_name)
                        if cls:
                            instance = cls(**values)
                            FileStorage.__objects[key] = instance
                except Exception:
                    pass

    def delete(self, obj=None):
        '''Delete obj if it is in __objects'''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)


FileStorage.classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
}

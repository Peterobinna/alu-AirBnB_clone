import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self, *args):
        dict = {}
        for key, obj in FileStorage.__objects.items():
                dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
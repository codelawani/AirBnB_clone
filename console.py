#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
"""This module contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Defines command interpreter class"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        arg = line.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            newModel = BaseModel()
            storage.new(newModel)
            storage.save()
            print(newModel.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        arg = line.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print('** instance id missing **')
            return
        model_dict = storage.reload()
        model_info = f"{arg[0]}.{arg[1]}"
        # checkid = model_dict.find(f"{modelName}.{baseid}")
        if model_info not in model_dict:
            print("** no instance found **")
        else:
            objdict = model_dict[model_info]
            obj = BaseModel(**objdict)
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = line.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        model_info = f"{arg[0]}.{arg[1]}"
        model_dict = storage.reload()
        checkdict = model_dict.pop(model_info, None)
        if not checkdict:
            print("** no instance found **")
        else:
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split()
        if args and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            modeldict = storage.reload()
            models = modeldict.values()
            objdicts = [model for model in models]
            objs = []
            for dict in objdicts:
                objs.append(BaseModel(**dict).__str__())
            print(objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        arg = line.split()
        if len(arg) < 1:
            print("** class name missing **")
            return
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        elif len(arg) < 3:
            print("** attribute name missing **")
            return
        elif len(arg) < 4:
            print("** value missing **")
            return
        class_name = arg[0]
        class_id = arg[1]
        attribute_name = arg[2]
        # if isinstance(arg[3], str):
        try:
            attribute_value = int(arg[3])
        except:
            try:
                attribute_value = float(arg[3])
            except:
                attribute_value = str(arg[3]).strip('\'"')
        models_dict = storage.all()

        model_info = f"{class_name}.{class_id}"
        if model_info not in models_dict:
            print("** no instance found **")
        else:
            objdict = models_dict[model_info]
            print(attribute_value)
            print(type(attribute_value))
            objdict[attribute_name] = attribute_value
            # del models_dict[model_info]
            print(objdict)
            newModel = BaseModel(**objdict)
            newModel.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

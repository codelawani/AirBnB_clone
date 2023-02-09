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
        basedict = storage.reload()
        model_info = f"{arg[0]}.{arg[1]}"
        # checkid = basedict.find(f"{modelName}.{baseid}")
        if model_info not in basedict:
            print("** no instance found **")
        else:
            objdict = basedict[model_info]
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
        if line.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            modeldict = storage.reload()
            models = modeldict.values()
            objdicts = [model for model in models]
            objs = []
            for dict in objdicts:
                objs.append(BaseModel(**dict).__str__())
            print(objs)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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
            new = BaseModel()
            basedict = new.to_dict()
            with open("file.json", 'a') as f:
                json.dump(basedict, f)
            print(new.id)

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
        with open("file.json") as jsonfile:
            basedict = json.load(jsonfile)

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

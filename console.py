#!/usr/bin/python3
import cmd
import json
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
        if len(arg) != 1:
            print("** class name missing **")
            return
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            json.dumps(new, "file.json")
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        arg = line.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

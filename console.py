#!/usr/bin/python3
import cmd
from models.engine import file_storage
from models.base_model import BaseModel
from shlex import split


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb)"
    a_classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, line):
        """uses conrol D to quit"""

        print()
        return True

    def do_create(self, line):
        """Creates a new instance"""
        mstring = line.split()
        if not line:
            print("** class name missing **")
            return False
        if mstring[0] not in self.a_classes:
            print("** class doesn't exist **")
            return False
        if mstring[0] in self.a_classes:
            obj = self.a_classes[mstring[0]]()
            print(obj.id)
            obj.save()

    def do_show(self, line):
        """String presentation of an instance based on class name"""
        if not line:
            return False
        mstring = line.split()
        if mstring[0] not in self.a_classes:
            print("** class name missing **")
            return False
        if mstring[0] not in self.a_classes:
            print("** class doesn't exist **")

    def postloop(self):
        """Prints a new line after loop"""
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

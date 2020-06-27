#!/usr/bin/python3
"""
The command interpreter
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
import models

classes = ["BaseModel", "FileStorage"]

class HBNBCommand(cmd.Cmd):
    
    """
    HBNBCommand
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Ctrl + D command to exit the program (End of File).
        """
        print()
        return True

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        This does nothing. An empty line + ENTER shouldn’t execute anything.
        """
        pass

    def do_create(self, arg):
        """do_create
        Creates a new instance of class BaseModel.
        Arg:
            arg (class): name.
        Syntax:
            cretate <class_name>
        Example:
            $ create BaseModel
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            new_instance = BaseModel()
            new_instance.save() 
            print(new_instance.id)
        else:
            print("** class doesn't exist **")
            
    def do_show(self, arg):
        """do_show
        Prints the string representation of an instance
        based on the class name and id
        Args:
            arg (class): class's name (instance) for display id.
        Syntax:
            show <class_name> <id>
        Example:
            $ show BaseModel 1234-1234-1234
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_obj = models.storage.all()
            for key, value in all_obj.items():
                id_current = key.split('.')
                if id_current[1] == args[1]:
                    print(all_obj[key])
                    return
            print("** no instance found **")        

    def do_destroy(self, args):
        pass

    def do_all(self, args):
        pass

    def do_update(self, args):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

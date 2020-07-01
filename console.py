#!/usr/bin/python3
"""
The command interpreter
"""
import cmd
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    'BaseModel': BaseModel, 'Amenity': Amenity,
    'State': State, 'Place': Place, 'Review': Review,
    'User': User, 'City': City
    }


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Ctrl + D command to exit the program (End of File).
        """
        return True

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
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
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """do_show
        Prints the string representation of an instance
        based on the class name and id
        Args:
            arg (class): class's name (instance) and id.
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

    def do_destroy(self, arg):
        """do_destroy
        Deletes an instance based on the class name and id
        Args:
            arg (class): class's name (instance) and id.
        Syntax:
            destroy <class_name> <id>
        Example:
            $ destroy BaseModel 1234-1234-1234
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            idx = "{}.{}".format(args[0], args[1])
            all_obj = models.storage.all()
            if idx in all_obj:
                all_obj.pop(idx)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """do_all
        Prints all string representation of all instances
        based or not on the class name
        Args:
            arg (class): class's name (instance) or nothing.
        Syntax:
            all or all <class_name>
        Example:
            $ all
            (...)
            $ all BaseModel
        """
        args = shlex.split(arg)
        all_obj = models.storage.all()
        new_list = []
        for key, value in all_obj.items():
            new_list.append(str(all_obj[key]))
        if len(args) == 0:
            print(new_list)
        elif args[0] in classes:
            new_list = []
            for key, value in all_obj.items():
                obj_current = key.split('.')
                if obj_current[0] == args[0]:
                    new_list.append(str(all_obj[key]))
            print(new_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """do_update
        Updates an instance based on the class name and id
        by adding or updating attribute
        Args:
            arg (class): class's name (instance), id, key and value.
        Syntax:
            update <class_name> <id> <key> <value>
        Example:
            $ all BaseModel 1234-1234-123 email "example@holbertonschool.com"
        """
        args = shlex.split(arg)
        all_obj = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = "{}.{}".format(args[0], args[1])
            if obj in all_obj:
                obj_new_attribute = all_obj[obj]
                try:
                    tmp = eval(args[3])
                    if type(tmp) == int or type(tmp) == float:
                        args[3] = tmp
                except:
                    pass
                setattr(obj_new_attribute, args[2], args[3])
                obj_new_attribute.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

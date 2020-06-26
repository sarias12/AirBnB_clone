#!/usr/bin/python3
"""
The command interpreter
"""
import cmd
import sys


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

    def do_create(self, name):
        pass

    def do_show(self, args):
        pass

    def do_destroy(self, args):
        pass

    def do_all(self, args):
        pass

    def do_update(self, args):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

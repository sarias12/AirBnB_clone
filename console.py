#!/usr/bin/python3
'''[summary]
'''
import cmd
import sys


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def emptyline(self):
        '''[summary]
        '''
        pass

    def do_quit(self, list):
        '''Quit command to exit the program
        '''
        print()
        return True

    def do_EOF(self, line):
        '''[summary]
        '''
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

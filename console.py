#!/usr/bin/python3
"""This module for HBNBCommand class that inherits from Cmd class
from cmd module cmd.Cmd to make a command interpriter
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """This  is a simple command interprete"""

    prompt = "(hbnb) "

    def emptyline(self):
        """This method for an empty line + ENTER shouldn't execute anything"""
        pass

    def do_EOF(self, line):
        """This method handle the end of file"""
        return True

    def do_quit(self, line):
        """This method handle the end of file to exit from the program"""
        return True

    def do_create(self, line):
        """This method creates a new instance of BaseModel
        saves it to the JSON file
        and prints the id
        """ 
        self.comnd = line.split()
        if (len(self.comnd) < 2):
            print('** class name missing **')
        elif (self.comnd[2]):
            print("** class doesn't exist **")
        else:
            storage.save()
            #print id            

    def do_show(self):
        """This method prints the string representation of an instance
        based on the class name and id
        """

    def do_destroy(self):
        """This method deletes an instance based on the class name
        and id (save the change into the JSON file)
        """

    def do_all(self):
        """This method prints all string representation of all instances
        based or not on the class name
        """

    def do_update(self):
        """This method Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()

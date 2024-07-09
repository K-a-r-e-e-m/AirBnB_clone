#!/usr/bin/python3
"""This module for HBNBCommand class that inherits from Cmd class
from cmd module cmd.Cmd to make a command interpriter
"""

import shlex
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        args = line.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in storage.class_map:
            print("** class doesn't exist **")
        else:
            instance = storage.class_map[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """This method prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        all_objects = storage.all()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in storage.class_map:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in all_objects:
            print('** no instance found **')
        else:
            print(all_objects[f'{args[0]}.{args[1]}'])

    def do_destroy(self, line):
        """This method deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        args = line.split()
        all_objects = storage.all()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in storage.class_map:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in all_objects:
            print('** no instance found **')
        else:
            del (all_objects[f'{args[0]}.{args[1]}'])

    def do_all(self, line):
        """This method prints all string representation of all instances
        based or not on the class name
        """
        args = line.split()
        all_objects = storage.all()
        if len(args) < 1:
            print([str(val) for obj, val in all_objects.items()])
        elif args[0] not in storage.class_map:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj, val in all_objects.items():
                obj_name_dot_id = obj.split('.')
                obj_name = obj_name_dot_id[0]
                if obj_name == args[0]:
                    obj_list.append(str(val))
            print(obj_list)
        # print([
        #       str(val) for obj, val in all_objects.items()
        #       if obj.split('.')[0] == args[0]
        # ])

    def do_update(self, line):
        """This method Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)
        """
        # shlex --> Split the string (line) using like shell syntax
        # shlex is a smart parser input that respect the quotes
        args = shlex.split(line)
        all_objects = storage.all()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in storage.class_map:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in all_objects:
            print('** no instance found **')
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            obj = all_objects[f'{args[0]}.{args[1]}']
            setattr(obj, args[2], args[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()

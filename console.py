#!/usr/bin/python3
"""This module for HBNBCommand class that inherits from Cmd class
from cmd module cmd.Cmd to make a command interpriter
"""

import cmd
from models import storage
import shlex


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
            del all_objects[f'{args[0]}.{args[1]}']
            storage.save()  # Save changes to JSON file

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
        if type(line) is str:
            args = shlex.split(line)
        else:
            args[2] = line.key()
            args[3] = line.value()
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
            storage.save()  # Save changes to the JSON file

    def default(self, line):
        '''called on an input line when command prefix is not recognized'''
        if '.' in line and '(' in line and ')' in line:
            args = line.split()
            # ex: User.update(id, attr)
            class_name, method_call = line.split('.')
            # class_name = 'User',  method_call = 'update(id, attr)'
            method_name, args_str = method_call.split('(')
            # method_name = 'update', args_str = 'id, attr)'
            args_str = args_str.strip(')')
            # args_str = 'id, attr'
            args = [arg.strip() for arg in args_str.split(',')]
            # args = [id, attr]

            if class_name in storage.class_map:
                if method_name == 'all':
                    self.do_all(class_name)
                elif method_name == 'count':
                    self.do_count(class_name)
                elif method_name == 'show':
                    self.do_show(f'{class_name} {args[0]}')
                elif method_name == 'destroy':
                    self.do_destroy(f'{class_name} {args[0]}')
                elif method_name == 'update':
                    if len(args) == 3:
                        self.do_update(f'{class_name} {args[0]} {args[1]}' +
                                       f' {args[2]}')
                    elif len(args) == 2:
                        args[1] = dict(args[1])
                        for key, val in args[1].items():
                            self.do_update(f'{class_name} {args[0]} {key}'
                                           f'{val}')
                else:
                    return cmd.Cmd.default(self, line)
            else:
                return cmd.Cmd.default(self, line)
        else:
            return cmd.Cmd.default(self, line)

    def do_count(self, class_name):
        '''Count number of instances'''
        count = 0
        all_objects = storage.all()
        for obj in all_objects:
            if class_name in obj:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

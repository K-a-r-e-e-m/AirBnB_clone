import cmd

class HBNBCommand(cmd.Cmd):
    """Tis  is a simple command interpreter"""

    prompt = "(hbnb)"

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """This method handle the end of file"""
        return True

    def do_quit(self, line):
        """This method handle the end of file to exit from the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

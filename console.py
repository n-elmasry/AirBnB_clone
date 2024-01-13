#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys
from shlex import split


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand """

    prompt = "(hbnb) "

    def __init__(self, *args, **kwargs):
        '''Initialization'''
        super().__init__(*args, **kwargs)
        self.file_storage = FileStorage()

    # handling quit
    def do_quit(self, args):
        """Quit command to exit the program

        """
        sys.exit()

    # handling EOF
    def do_EOF(self, args):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        sys.exit()

    def do_help(self, args):
        """help"""
        cmd.Cmd.do_help(self, args)

    # an empty line + ENTER shouldn’t execute anything
    def emptyline(self):
        """Handles an empty line; do nothing."""
        pass

    # task 7 starts here
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if len(args) < 2:
            print('** class name missing **')
        elif args[1] not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[args[1]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints str representation of instance based on class name and id"""
        arguments = line.split()
        if len(arguments) == 0:
            print('** class name missing **')
            return

        class_name = arguments[0]
        if class_name not in storage.classes:
                print("** class doesn't exist **")
                return

        if len(arguments) < 2:
            print('** instance id missing **')
            return

        instance_id = arguments[1]
        key = "{}.{}".format(class_name, instance_id)

        instances = storage.all()
        if key not in instances:
            print('** no instance found **')
        else:
            print(instances[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print('** class name missing **')
        else:
            arguments = args.split()
            if arguments[0] not in HBNBCommand.FileStorage.classes:
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print('** instance id missing **')
            else:
                key = "{}.{}".format(arguments[0], arguments[1])
                instances = storage.all()

                if key not in instances:
                    print('** no instance found **')
                else:
                    del instances[key]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances"""
        from models import storage
        storage.reload()
        instances = storage.all()

        if not args or args in storage.classes:
            for instance in instances.values():
                print(instance)
        else:
            print("** class doesn't exist **")

            # task 7 ends here


# HBNBCommand().cmdloop()


if __name__ == '__main__':
    # cmd = HBNBCommand()
    # if not sys.stdin.isatty():
    # for line in sys.stdin:
    # HBNBCommand.onecmd(line.strip())
    # else:
    HBNBCommand().cmdloop()

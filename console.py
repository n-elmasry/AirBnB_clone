#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
import sys


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand """

    prompt = "(hbnb) "

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

    # an empty line + ENTER shouldn’t execute anything
    def emptyline(self):
        """Handles an empty line; do nothing."""
        pass

    # task 7 starts here
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not args:
            print('** class name missing **')
        elif args not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        else:
            new_instance = globals()[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints str representation of instance based on class name and id"""
        if not args:
            print('** class name missing **')
        elif args.split()[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        elif len(args.split()) < 3:
            print('** instance id missing **')
        else:
            class_name, instance_id = args.split()[0], args.split()[1]
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
        elif args.split()[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        elif len(args.split()) < 3:
            print('** instance id missing **')
        else:
            class_name, instance_id = args.split()[0], args.split()[1]
            key = "{}.{}".format(class_name, instance_id)
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

        if not args or args == 'BaseModel' or args == 'User':
            for instance in instances.values():
                print(instance)
        else:
            print("** class doesn't exist **")

            # task 7 ends here


HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

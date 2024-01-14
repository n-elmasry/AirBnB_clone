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
    clsz = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

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
        if not args:
            print('** class name missing **')
        elif args not in HBNBCommand.clsz:
            print("** class doesn't exist **")
        else:
            """
            new_instance = globals()[args]()
            new_instance.save()
            print(new_instance.id)
            """
            new_instance = eval(args.split()[0] + '()')
            if isinstance(new_instance, BaseModel):
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """Prints str representation of instance based on class name and id"""
        if not args:
            print('** class name missing **')
        elif args.split()[0] not in HBNBCommand.clsz:
            print("** class doesn't exist **")
        if len(args.split()) < 2:
            print('** instance id missing **')
        else:
            class_name, instance_id = args.split()[0], args.split()[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all(class_name)

            if key not in instances:
                print('** no instance found **')
            else:
                print(instances[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print('** class name missing **')
        elif args.split()[0] not in HBNBCommand.clsz:
            print("** class doesn't exist **")
        elif len(args.split()) < 2:
            print('** instance id missing **')
        else:
            class_name, instance_id = args.split()[0], args.split()[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all(class_name)

            if key not in instances:
                print('** no instance found **')
            else:
                del instances[key]
                storage.save()
    """
    def do_all(self, args):
        storage.reload()
        instances = storage.all()

        if not args or args.lower() == 'basemodel':
            for instance in instances.values():
                print(instance.__str__())
        elif args.lower() in HBNBCommand.clsz:
            for key, instance in instances.items():
                class_name = key.split('.')[0]
                if class_name == args.lower():
                    print(instance.__str__())
        else:
            print("** class doesn't exist **")
    """
    def do_all(self, args):
        """Prints all string representation of all instances"""
        storage.reload()
        instances = storage.all()

        if not args or args.lower() == 'basemodel':
            result = [instance.__str__() for instance in instances.values()]
            print(result)

        elif args.split()[0] in HBNBCommand.clsz:
            result = [
                instance.__str__()
                for key, instance in storage.all(args.split()[0]).items()
                # if key.split('.')[0] == args.lower()
            ]
            print(result)
        else:
            print("** class doesn't exist **")

            # task 7 ends here
    def do_update(self, args):
        '''Update Console instance'''
        if not args:
            print('** class name missing **')
        else:
            if split(args)[0] not in self.clsz:
                print("** class doesn't exist **")
            elif len(split(args)) < 2:
                print('** instance id missing **')
            else:
                key = "{}.{}".format(split(args)[0], split(args)[1])
                instances = storage.all(split(args)[0])
                if key not in instances:
                    print('** no instance found **')
                elif len(split(args)) < 3:
                    print('** attribute name missing **')
                elif len(split(args)) < 4:
                    print('** value missing **')
                else:
                    setattr(instances[key], split(args)[2], split(args)[3])
                    instances[key].save()

    def do_count(self, args):
        '''Retrieve number of class instances'''
        if not args or args[0] not in HBNBCommand.clsz:
            print("** class name missing **")
            return
        instances = storage.all(args[0])
        print(len(instances))

    def do_update_dict(self, args):
        '''Update instance and class'''
        if not args:
            print('** class name missing **')
        elif args.split()[0] not in self.clsz:
            print("** class doesn't exist **")
        elif len(args.split()) < 2:
            print('** instance id missing **')
        elif len(args.split()) < 3:
            print('** dictionary missing **')
        else:
            class_name, instance_id = args.split()[0].split()[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all(class_name)

            if key not in instances:
                print('** no instance found **')
            else:
                try:
                    dict_attribute = eval(args.split()[2])
                    for key, value in dict_attribute.items():
                        setattr(instances[key], key, valye)
                    instances[key].save()
                except Exception as e:
                    print('** invalid dictionary format **')

# HBNBCommand().cmdloop()


if __name__ == '__main__':
    # cmd = HBNBCommand()
    # if not sys.stdin.isatty():
    # for line in sys.stdin:
    # HBNBCommand.onecmd(line.strip())
    # else:
    HBNBCommand().cmdloop()

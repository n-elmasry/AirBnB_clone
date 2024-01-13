#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import models
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
        if len(args) < 2:
            print('** class name missing **')
        elif args[1] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints str representation of instance based on class name and id"""
        if len(args) < 2:
            print('** class name missing **')
        elif args[1] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) < 3:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args[1], args[2])
            instances = models.file_storage.all()

            if key not in instances:
                print('** no instance found **')
            else:
                print(instances[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if len(args) < 2:
            print('** class name missing **')
        elif args[2] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) < 3:
            print('** instance id missing **')
        else:
            key = "{}.{}".format(args[2], args[3])
            instances = models.file_storage.all()

            if key not in instances:
                print('** no instance found **')
            else:
                del instances[key]
                models.file_storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances"""
        from models import storage
        storage.reload()
        instances = storage.all()

        if len(args) < 3 or args[2] == 'BaseModel':
            for instance in instances.values():
                print(instance)
        else:
            print("** class doesn't exist **")

            # task 7 ends here


HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

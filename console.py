#!/usr/bin/env python3
"""
Module: console
Description: Console application for the airbnb clone.
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console application dealing with basic operations
       such as creating new instances, deleting, printing, updating,
       and getting specific information about instances.
       Note: msg >--< message
             rep. >--< representation

    Attributes:
        prompt (str): prompt of choice for the cmd application.
        CLASSES (dict): dictionary with all classes created.
    Methods:
        do_quit(self, command: str) -> useful when needing to exit
                                       the cmd application.
        help_quit(self) -> Help message on quit command.
        do_EOF(self, command: str) -> Implements EOF command.
        help_EOF(self) -> Help message on EOF conditions.
        do_create(self, args: str) -> Created a new instance of a
                                      particular class.
        help_create(self) -> Help message on create command.
        do_show(self, args: str) -> Prints all instances.
        help_show(self) -> Help message on show command.
        help_destroy(self) -> Deletes a particular instance and updates
                              the json file with all instanced created.
        do_all(self, args: str) -> Prints all instance.
        help_all(self) -> Help message on all command.
        do_update(self, args: str) -> Updates instances based on
                                      attributes/value pair.
        help_update(self) -> Help message on update command.
        emptyline(self) -> Ignored empty line + ENTER command.
    """

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""
    CLASSES = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def preloop(self) -> None:
        """Does something if isatty is false."""
        if not sys.__stdin__.isatty():
            print("(hbnb)")
        return None

    def do_quit(self, command: str) -> bool:
        """Performs quit operation with formatting.
        Args:
            command (str): string of arguments passed along
                           with the quit command.
        Returns:
            Nothing.
        """
        return True

    def help_quit(self) -> None:
        """Prints help message on quit command."""
        print("Exit program execution with formatting.\n")
        return None

    def do_EOF(self, command: str) -> bool:
        """Performs end-of-file operations.
        Args:
            command (str): string of arguments.
        Return:
            Nothing.
        """
        print()
        return True

    def help_EOF(self) -> None:
        """Prints help message on EOF command."""
        print("Exit program execution without formatting.\n")
        return None

    def do_create(self, args: str) -> None:
        """Creates a new instance of any class defined.
        Args:
            args (str): string of arguments associated
                        with the create command.
        Returns:
            Nothing.
        """
        args = args.strip().split(" ")
        classToCreate = args[0]
        if len(args) == 0:
            """no argument passes to command"""
            print("** class name missing **")
            return
        if classToCreate not in self.CLASSES:
            # print our beloved error msg
            print("** class doesn't exist **")
            return
        instance = self.CLASSES[classToCreate]()
        instance.save()
        print(instance.id)
        return None

    def help_create(self) -> None:
        """Help msg for create command."""
        print("Creates new instance of any class defined.")
        print("Usage: create <class_name>\n")
        return None

    def do_show(self, args: str) -> None:
        """Prints string rep. of created instance.
        Args:
            args (str): string with arguments to the
                        show command.
        Returns:
            Nothing.
        """
        args = args.strip().split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instanceToShow = args[0]
        if instanceToShow not in self.CLASSES:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key = f"{instanceToShow}.{instance_id}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")
        return None

    def help_show(self) -> None:
        """Shows help msg on show command."""
        print("Prints string rep. of an instance based \
            on classname and id")
        print("Usage: show <class_name> <instance_id>\n")
        return None

    def do_destroy(self, args: str) -> None:
        """Deletes an instance based on class name and instance
           id of any predefined class object.
        Args:
            args (str): string with arguments associated with
                        the destroy command.
        Returns:
            Nothing.
        """
        args = args.strip().split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        try:
            storage.delete(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")
        return None

    def help_destroy(self) -> None:
        """Help msg on destroy command."""
        print("Deletes an instance based on class name and instance \
            id of a predefined class.")
        print("Usage: destroy <class_name> <instance_id>")
        return None

    def do_all(self, args: str) -> None:
        """Prints string rep. of all instances based on classname.
        Args:
            args (str): string with arguments associated with
                        the all command.
        Returns:
            Nothing.
        """
        args = args.strip().split(" ")
        my_class = args[0]
        my_list = []
        if len(args) == 0:
            for key, value in storage.all().items():
                # convert object to string.
                obj = str(value)
                my_list.append(obj)
        elif len(args) == 1:
            class_name = args[0]
            if class_name not in self.CLASSES:
                # error msg.
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    # check if key matches class name
                    classname = key.split('.')[0]
                    if classname != my_class:
                        continue
                    else:
                        # convert value to string.
                        obj = str(value)
                        my_list.append(obj)
        print(my_list)
        return None

    def help_all(self) -> None:
        """Help msg on all command."""
        print("Prints string rep. of all instances.")
        print("Usage: all <class_name> OR all (without classname)\n")
        return None

    def do_update(self, args: str) -> None:
        """Updates an instance of a particular class.
        Args:
            args (str): string with arguments associated with
                        update command.
        Returns:
            Nothing.
        """
        args = args.strip().split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        attribute = args[2]
        value = args[3]
        if value[0] == '"':
            value = ''.join([x for x in value if x != '"'])
        key = f"{class_name}.{instance_id}"
        # check if instance with id exists.
        if key not in storage.all():
            print("** no instance found **")
            return
        mydict = storage.all()[key]
        mydict.__dict__.update({attribute: value})
        mydict.save()
        return None

    def help_update(self) -> None:
        """Help msg on update command."""
        print("Updates an instance of a particular class per id.")
        print("Usage: update <class name> <id> <attribute name> \
            \"<attribute value>\"\n")
        return None

    def emptyline(self):
        """Ignores empty line + ENTER."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

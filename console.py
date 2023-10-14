#!/usr/bin/python3

"""
    Implementation of the console for the alx AirBnB project
"""
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
        The entry point of the command interpreter
    """

    prompt = ("(hbnb)")

    def do_quit(self, args):
        """
            Command to quite and exit the program
        """
        return True
    
    def do_EOF(self, args):
        """
            Exits after receiving the EOF signal
        """

        return True
    
    def do_create(self, args):
        """
            Create a new instance of the BaseModel class and
            saves it to the JSON file
        """

        if len(args) == 0:
            print("***class name is missing***")
            return
        
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except:
            print("***** class doesn't exist ***")
        
    def do_show(self, args):
        """
            Prints the string representation of an instance based
            on the class name and id given as args
        """

        args = shlex.split(args)
        if len(args) == 0:
            print("***class name missing***")
            return
        if len(args) == 1:
            print("***instance id missing***")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print(" ***class doesn't exist***")
            return
        key = args[0] + '.' + args[1]
        key = args[0] + '.' + args[1]

        try: 
            value = obj_dict[key]
            print(value)
        except KeyError:
            print(" ***no instance found***")

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id.
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()
    
    def do_all(self, args):
        """"
            Returns all string representation of all instances
            based on the class name.
        """
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()

        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)

        print(obj_list)
    
    def do_update(self, args):
        """
            Update an instance based on the class name and id sent as args
        """

        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing**")
            return
        elif len(args) == 2:
            print("** attributes name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()




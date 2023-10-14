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
            


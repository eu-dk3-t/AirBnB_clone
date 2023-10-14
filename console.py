#!/usr/bin/python3

"""
    Implementation of the console for the alx AirBnB project
"""
import cmd
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

#!/usr/bin/python3
"""
Starts a commandline interpreter
"""
import cmd
from __init__ import storage
import base_models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """do nothing when empty line"""
        pass
    def help_help(self):
        """Returns the description of a command
        """
        print("Return the description of a command")

    def do_create(self, class_name):
        """Creates a new instance of the BaseModel class, saves it to a json file and prints its id
        """
        if class_name:
            if class_name == 'BaseModel':
               new_instance = base_models.BaseModel()
               new_instance = new_instance.to_dict()
               storage.new(new_instance)
               storage.save()
               print(new_instance['id'])
            else:
                print("**class doesn't exist**")
        else:
            print("**class name missing**")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                arg_list = line.split()
                class_name, instance_id = arg_list[0], arg_list[1]
                if class_name == "BaseModel":
                    for val in storage.all().values():
                        if val["__class__"] == class_name and val["id"] == instance_id:
                            print("[{}] ({}) {}".format(val["__class__"], val["id"], val))
                            break
                    else:
                        print("**No instance found**")
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        else:
            try:
                arg_list = line.split()
                class_name, instance_id = arg_list[0], arg_list[1]
                if class_name == "BaseModel":
                    available_instances = storage.all()
                    for key,val in available_instances.items():
                        if val["__class__"] == class_name and val["id"] == instance_id:
                            del available_instances[key]
                            storage.save()
                            break
                    else:
                        print("**No instance found**")
                else:
                    print("** class doesn't exist **")
            except IndexError:
                print("** instance id missing **")


    def do_EOF(self, line):
        """Quit command to exit the command
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

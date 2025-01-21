import cmd

from models.base_model import BaseModel
from models import storage


class_dict = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Quit command to exit the program\n"""
        exit()

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        exit()

    def do_create(self, args):
        """create <class name> - Creates a new instance of BaseModel, saves it and prints the id"""
        if not args:
            print("** class name missing **")
        elif args not in class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = class_dict[args]() 
            new_instance.save()
            print(new_instance.id)
    def do_show(self, args):
        """show <class name> <id> - Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_dict:
                print("** class doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            else:
                for k, v in storage.all().items():
                    if v.id == args[1]:
                        print(v)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """destroy <class name> <id> - Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_dict:
                print("** class doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            else:
                for k, v in storage.all().items():
                    if v.id == args[1]:
                        del storage.all()[k]
                        storage.save()
                    else:
                        print("** no instance found **")
    
    def do_all(self, args):
        """all - Prints all instances"""
        if not args:
            for k, v in storage.all().items():
                print(v)
        else:
            
            if args not in class_dict:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if v.__class__.__name__ == args:
                        print(v)
    
    def do_update(self, args):
        """update <class name> <id> <attribute name> "<attribute value>" - Updates an instance based on the class name and id by adding or updating attribute """
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_dict:
                print("** class doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            elif not args[2]:
                print("** attribute name missing **")
            elif not args[3]:
                print("** value missing **")
            else:
                for k, v in storage.all().items():
                    if v.id == args[1]:
                        setattr(v, args[2], args[3])
                        storage.save()
                    else:
                        print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
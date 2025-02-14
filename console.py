import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    intro = 'Welcome to the HBNB command interpreter. Type help or ? to list commands.'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the command interpreter."""
        print('Exiting HBNB command interpreter.')
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF signal."""
        print('Exiting HBNB command interpreter.')
        return True

    def emptyline(self):
        """Override empty line behavior to do nothing."""
        pass

    def do_help(self, arg):
        """Display help for commands."""
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
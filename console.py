#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd


class CmdInterpreter(cmd.Cmd):
    """Defines the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass

    def do_quit(self, line):
        """Exit when reciving quit"""
        print("")
        return True

    def do_EOF(self, line):
        """Exit when reaching EOF"""
        print("")
        return True


if __name__ == '__main__':
    CmdInterpreter().cmdloop()

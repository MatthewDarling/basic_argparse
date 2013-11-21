import argparse, sys

def print_and_exit(string):
    class PrintAction(argparse.Action):
        """An argparse action to print your module's docstring."""
        def __call__(self, parser, namespace, values, option_string=None):
            print(string)
            sys.exit(0)
    return PrintAction

def init_parser(prog_name, version, date, doc):
    parser = argparse.ArgumentParser(add_help=False)
    info = parser.add_mutually_exclusive_group()
    info.add_argument("-h", "--help", action="help", 
                      help="Print this message and exit.")
    #I like this format a bit better than the default option
    info.add_argument("-v", "--version", action="version", 
                      version="{} version {}, "
                      "from {}.".format(prog_name, version, date),
                      help="Print the program's version and exit.")
    info.add_argument("-d", "--doc", action=print_and_exit(doc), nargs=0, 
                      help="Print the program's docstring and exit.")
    return parser

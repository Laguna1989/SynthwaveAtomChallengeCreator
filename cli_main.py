import logging
import os
import sys
from arguments_from_string import handle_atom_call

# create logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

def main():
    command_string = ''
    for arg in sys.argv[1:]:          # skip sys.argv[0] since the question didn't ask for it
        if ' ' in arg:
            command_string+= "'{}' ".format(arg) ;   # Put the quotes back in
        else:
            command_string+="{} ".format(arg) ;      # Assume no space => no quotes

    # arg_string = command_string
    # print(arg_string)

    print(handle_atom_call(command_string, logger))


if __name__ == "__main__":
    main()

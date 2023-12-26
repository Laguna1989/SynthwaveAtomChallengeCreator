from atom_arguments import AtomArguments, get_mode_from_string, get_chords_from_string
import argparse
import shlex
import sys
from io import StringIO

from atom_instructions import get_atom_instruction_string
from sanitize import is_sane_input


def create_parser():
    parser = argparse.ArgumentParser(description='Parsing arguments for atom instructor.',
                                     prog='!Atom')
    parser.add_argument("-t", "--tempo", help='Use a specific tempo given in bpm.')
    parser.add_argument("-d", "--drums",
                        help='Use a specific drum machine. DRUMS should be given as a string. '
                             'If DRUMS contains spaces, please add quotation marks, e.g. "Linn Linndrum".')
    parser.add_argument("-k", "--key", help='Use a specific key.',
                        choices=["ab", "a", "a#", "bb", "b", "c", "c#", "db", "d", "d#", "eb", "e", "f", "f#", "gb",
                                 "g",
                                 "g#"], type=str.casefold)
    parser.add_argument("-m", "--mode", help='Use a specific mode.',
                        choices=['ionian', 'aeolian', 'dorian', 'mixolydian', 'lydian', 'phrygian'], type=str.casefold)
    parser.add_argument("-c", "--chords",
                        help='Use a specific chord progression. '
                             'CHORDS should be given as a string. '
                             'Individual chords are expected as roman numerals.'
                             'Chords can be separated by commas, e.G. "I, IV7, iisus4, I"')
    return parser


def get_arguments_from_string(message_content: str):
    split_content = message_content.split()
    args_string = ""
    if len(split_content) > 1:
        args_string = " ".join(split_content[1:])

    parser = create_parser()
    args = parser.parse_args(shlex.split(args_string))

    aa = AtomArguments()
    if args.tempo:
        aa.tempo = int(args.tempo)
    if args.drums:
        aa.drums = args.drums
    if args.key or args.mode:
        aa.mode = get_mode_from_string(args.key, args.mode)
    if args.chords:
        aa.chords = get_chords_from_string(args.chords)

    return aa


def get_parser_help_string():
    parser = create_parser()
    # redirect print to mystdout
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    # perform printing action
    parser.print_help()
    # restore original cout
    sys.stdout = old_stdout
    version_string = "version: `SWACC_VERSION` \n"
    return version_string + "```\n" + mystdout.getvalue() + "```\n"


def handle_atom_call(content, logger):
    error_message = ":exclamation: AtomInstructor collapses"

    if not is_sane_input(content):
        return error_message

    if content.startswith((
            '!atomhelp',
            '!atom help',
            '!Atomhelp',
            '!Atom help'
    )):
        if logger:
            logger.info("!atomhelp called")
        return get_parser_help_string()

    if content.startswith(('!atom', '!Atom', '!ATOM')):
        content_is_long_enough_for_parameters = (len(content) > 5)
        if content_is_long_enough_for_parameters:
            if content[5] != ' ':
                # for any invalid !atom call, do not print an error message
                return ""

        if logger:
            logger.info("!atom called")
        try:
            args = get_arguments_from_string(content)
            return "Here are your instructions:\n\n" + get_atom_instruction_string(args)
        except:
            if logger:
                logger.error("!atom failed: '" + content + "'")
            return error_message
    return ""

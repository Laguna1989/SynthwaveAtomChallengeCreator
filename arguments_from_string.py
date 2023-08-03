from atom_arguments import AtomArguments, get_mode_from_string, get_chords_from_string
import argparse
import shlex


def create_parser():
    parser = argparse.ArgumentParser(description='Parsing arguments for atom instructor.',
                                     prog='!Atom')
    parser.add_argument("-t", "--tempo", help='Use a specific tempo given in bpm.')
    parser.add_argument("-d", "--drums",
                        help='Use a specific drum machine. DRUMS should be given as a string. '
                             'If DRUMS contains spaces, please add quotation marks, e.g. "Linn Linndrum".')
    parser.add_argument("-k", "--key", help='Use a specific key.',
                        choices=['c', 'd', 'e', 'f', 'g', 'a', 'b'], type=str.casefold)
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

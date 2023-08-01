from atom_arguments import AtomArguments, get_mode_from_string, get_chords_from_string
import argparse
import shlex


def get_arguments_from_string(message_content: str):
    split_content = message_content.split()
    args_string = ""
    if len(split_content) > 1:
        args_string = " ".join(split_content[1:])

    parser = argparse.ArgumentParser(description='Parsing arguments for atom instructor')
    parser.add_argument("-t", "--tempo")
    parser.add_argument("-d", "--drums")
    parser.add_argument("-m", "--mode")
    parser.add_argument("-c", "--chords")

    args = parser.parse_args(shlex.split(args_string))

    aa = AtomArguments()
    if args.tempo:
        aa.tempo = int(args.tempo)
    if args.drums:
        aa.drums = args.drums
    if args.mode:
        aa.mode = get_mode_from_string(args.mode)
    if args.chords:
        aa.chords = get_chords_from_string(args.chords)

    return aa

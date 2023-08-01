import random


def get_random_tempo():
    return str(random.randint(75, 140))


def get_tempo(args):
    if args.tempo:
        return args.tempo
    return get_random_tempo()


def get_timing():
    return "4/4"


def get_track_duration():
    return "60-90s"

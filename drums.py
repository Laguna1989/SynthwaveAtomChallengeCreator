import random


def get_random_drums():
    drums_array = [
        "E-mu Drumulator",

        "Korg DDD-1",

        "Linn 9000",
        "Linn LinnDrum",
        "Linn LM-1",

        "Oberheim DMX",

        "Roland CR76",
        "Roland R8",
        "Roland TR-626",
        "Roland TR-707",
        "Roland TR-808",
        "Roland TR-909",

        "SCI DrumTraks",

        "Simmons SDSV",

        "Yamaha RX5",
        "Yamaha RY30"
    ]
    return random.choice(drums_array)


def get_drums(args):
    if args.drums:
        return args.drums
    return get_random_drums()

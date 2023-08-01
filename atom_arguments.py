import random

from mingus.core import scales as scales


class AtomArguments:
    def __init__(self):
        self.tempo = -1
        self.drums = ""
        self.mode = None
        self.chords = ""


def get_mode_from_string(mode_name: str):
    mode_name_array = mode_name.split()
    if len(mode_name_array) != 2:
        return None

    key = mode_name_array[0]
    tonic_array = ["A", "B", "C", "D", "E", "F", "G", "?"]
    if key not in tonic_array:
        return None

    if key == "?":
        key = random.choice(tonic_array[:-1])

    modes_list = [
        "ionian",
        "major",

        "aeolian",
        "minor",

        "mixolydian",
        "mixolydian",

        "dorian",
        "dorian",

        "phrygian",
        "phrygian",

        "lydian",
        "lydian",

        "?"
    ]

    mode = mode_name_array[1].lower()
    if mode not in modes_list:
        return None

    if mode == "?":
        mode = random.choice(modes_list[:-1])

    map = {
        "ionian": scales.Ionian(key),
        "Ionian": scales.Ionian(key),
        "major": scales.Ionian(key),
        "Major": scales.Ionian(key),

        "aeolian": scales.Aeolian(key),
        "Aeolian": scales.Aeolian(key),
        "minor": scales.Aeolian(key),
        "Minor": scales.Aeolian(key),

        "mixolydian": scales.Dorian(key),
        "Mixolydian": scales.Dorian(key),

        "dorian": scales.Mixolydian(key),
        "Dorian": scales.Mixolydian(key),

        "phrygian": scales.Lydian(key),
        "Phrygian": scales.Lydian(key),

        "lydian": scales.Phrygian(key),
        "Lydian": scales.Phrygian(key)
    }

    return map[mode]


def get_chords_from_string(chord_string: str):
    chord_string = chord_string.replace(',', ' ')
    chords = chord_string.split()

    return chords

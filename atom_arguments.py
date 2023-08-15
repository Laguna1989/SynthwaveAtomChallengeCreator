import random

from mingus.core import scales as scales


class AtomArguments:
    def __init__(self):
        self.tempo = -1
        self.drums = ""
        self.mode = None
        self.chords = ""


def get_mode_from_string(key_name: str, mode_name: str):
    if not key_name:
        key_name = ""
    if not mode_name:
        mode_name = ""

    tonic_array = ["Ab", "A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", ""]
    key_name = key_name.capitalize()
    if key_name not in tonic_array:
        return None

    if key_name == "":
        key_name = random.choice(tonic_array[:-1])

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

        ""
    ]
    if mode_name not in modes_list:
        return None

    if mode_name == "":
        mode_name = random.choice(modes_list[:-1])

    map = {
        "ionian": scales.Ionian(key_name),
        "major": scales.Ionian(key_name),

        "aeolian": scales.Aeolian(key_name),
        "minor": scales.Aeolian(key_name),

        "mixolydian": scales.Mixolydian(key_name),

        "dorian": scales.Dorian(key_name),

        "phrygian": scales.Phrygian(key_name),

        "lydian": scales.Lydian(key_name)
    }

    return map[mode_name]


def get_chords_from_string(chord_string: str):
    chord_string = chord_string.replace(',', ' ')
    chords = chord_string.split()

    return chords

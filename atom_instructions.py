import random
from mingus.core import scales as scales, chords as chords

def get_random_mode():
    tonic_array = ["A", "B", "C", "D", "E", "F", "G"]
    tonic = random.choice(tonic_array)

    modes_array = [
        scales.Ionian(tonic),
        scales.Aeolian(tonic),
        scales.Dorian(tonic),
        # scales.Mixolydian(tonic),
        # scales.Lydian(tonic),
        # scales.Phrygian(tonic)
    ]
    mode = random.choice(modes_array)

    return mode


def get_note_from_scale(notes, index):
    return notes[index % len(notes)]


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num


def get_chord_from_scale(mode, chord):
    notes_in_scale = mode.ascending()[:-1]
    chord = chord.strip()

    base_chord = chord
    if chord.endswith("7"):
        base_chord = base_chord[:-1]
    base_index = romanToInt(base_chord.upper()) - 1
    indices = [base_index, base_index + 2, base_index + 4]

    if chord.endswith("7"):
        indices.append(base_index + 6)
    return list(map(lambda i: get_note_from_scale(notes_in_scale, i), indices))


def get_random_tempo():
    return str(random.randint(75, 140))


def get_random_drums():
    drums_array = [
        "E-mu Drumulator",
        "Korg DDD-1",
        "Linn Linn9000",
        "Linn LinnDrum",
        "Oberheim DMX",
        "Roland R8",
        "Roland TR-626",
        "Roland TR-707",
        "Roland TR-808",
        "Roland TR-909",
        "SCI DrumTraks",
        "Simmons SDSV",
        "Yamaha RX5"
    ]
    return random.choice(drums_array)


def get_random_chord_progression(mode: str):
    ionian_progression_array = [
        ["I", "IV", "V"],
        ["I", "IV", "V7"],
        ["I7", "IV", "V"],
        ["I7", "IV", "V7"],

        ["I", "vi", "IV", "V"],
        ["I", "vi7", "IV", "V"],
        ["I", "vi", "IV", "V7"],
        ["I", "vi7", "IV", "V7"],

        ["I", "iii", "I", "V"],
        ["I", "iii", "I7", "V"],

        ["I", "ii", "IV", "V"],
        ["I", "ii", "IV", "V7"]
    ]

    aeolian_progression_array = [
        ["i", "VII", "v"],
        ["i", "VI", "iv", "v"],
        ["i7", "VI", "iv", "v"],
        ["i", "VI", "iv7", "v"],
        ["i", "iv", "v", "iv"],
        ["i", "VI", "III7", "v"],
        ["i7", "v", "VI"]
    ]

    ## TODO
    mixolydian_progression_array = [
        ["I", "VII", "IV"]
    ]

    dorian_progression_array = [
        ["i7", "IV7", "VII"],
        ["i7", "V", "VII"],
        ["i7", "V", "VII", "III"],
        ["i", "VII", "ii"],
        ["i7", "VII", "ii"],
        ["i", "VII", "ii7"],
        ["i7", "VII", "ii7"]
    ]

    ## TODO
    phrygian_progression_array = [
        ["i", "II", "III"]
    ]
    ## TODO
    lydian_progression_array = [
        ["I", "II", "IV"]
    ]

    map = {
        "ionian": ionian_progression_array,
        "aeolian": aeolian_progression_array,
        "mixolydian": mixolydian_progression_array,
        "dorian": dorian_progression_array,
        "phrygian": phrygian_progression_array,
        "lydian": lydian_progression_array
    }

    mode_str = mode.split()[1]
    return random.choice(map[mode_str])


def print_to_string(*args, **kwargs):
    newstr = ""
    for a in args:
        newstr+=str(a)+' '
    return newstr


def get_atom_instruction_string() -> str:
    output_string = ""
    output_string += print_to_string("* **Tempo:**", get_random_tempo(), "bpm") + "\n"
    output_string += print_to_string("* **Timing:** 4/4") + "\n"
    output_string += print_to_string("* **Total length:** 60-90s") + "\n"

    output_string += print_to_string("* **Drums:**", get_random_drums()) + "\n"

    mode = get_random_mode()
    key = mode.name.split(" ")[0]
    mode_name = mode.name.split(" ")[1]
    output_string += print_to_string("* **Key:**", key) + "\n"
    output_string += print_to_string("* **Mode:**", mode_name) + "\n"
    output_string += print_to_string("\t* **Notes in scale:**", mode.ascending()) + "\n"

    chord_progression = get_random_chord_progression(mode.name)
    output_string += print_to_string("* **chord progression:**", chord_progression) + "\n"
    for chord in chord_progression:
        chord_notes_array = get_chord_from_scale(mode, chord)
        output_string += print_to_string(" * **", chord, "**,", chords.determine(chord_notes_array, True, True, True)[0],
                                         ", notes: ",
                                         chord_notes_array) + "\n"


    return output_string.replace("'", "")

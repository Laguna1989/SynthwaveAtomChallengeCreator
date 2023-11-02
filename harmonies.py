import random

from mingus.core import scales as scales

from atom_arguments import AtomArguments


def get_random_mode():
    tonic_array = ["Ab", "A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#"]
    tonic = random.choice(tonic_array)

    modes_array = [
        scales.Ionian(tonic),
        scales.Aeolian(tonic),
        scales.Dorian(tonic),
        scales.Mixolydian(tonic),
        scales.Lydian(tonic),
        scales.Phrygian(tonic)
    ]
    mode = random.choice(modes_array)

    return mode


def get_mode(args):
    if args.mode:
        return args.mode
    return get_random_mode()


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


def get_chord_from_scale(notes_in_scale, chord):
    chord = chord.strip()

    base_chord = chord
    if "sus2" in base_chord:
        base_chord = base_chord[:-4]
    if "sus4" in base_chord:
        base_chord = base_chord[:-4]
    if "7" in base_chord:
        base_chord = base_chord[:-1]

    base_index = romanToInt(base_chord.upper()) - 1
    indices = [base_index, base_index + 2, base_index + 4]

    if "7" in chord:
        indices.append(base_index + 6)
    if "sus4" in chord:
        indices[1] += 1
    if "sus2" in chord:
        indices[1] -= 1
    return list(map(lambda i: get_note_from_scale(notes_in_scale, i), indices))


def get_random_chord_progression(mode: str, args: AtomArguments):
    if args.chords:
        return args.chords

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
        ["I", "ii", "IV", "V7"],

        ["I", "iv", "VI", "V"],

        ["I", "V", "vi", "iv"],
        ["I", "IV", "ii", "V"],
        ["I", "iii", "vi", "V"],
        ["I", "iii", "vi", "V"],
    ]

    aeolian_progression_array = [
        ["i", "VII", "v"],
        ["i", "VII", "v", "isus2"],

        ["i", "VI", "iv", "v"],
        ["i7", "VI", "iv", "v"],
        ["i", "VI", "iv7", "v"],
        ["i", "iv", "v", "iv"],

        ["i", "VI", "III7", "v"],

        ["i7", "v", "VI"],
        ["i7", "v", "VI", "i7sus4"],

        ["i", "iii", "VII", "iv"],
        ["i7", "iii", "VII", "iv"],
        ["i", "iii", "VII7", "iv"],
        ["i7", "iii", "VII7", "iv"],
        ["i7", "v", "VI", "i7sus4"],

        ["i", "VII", "VI", "v"],
        ["i", "III", "VII", "iv"],
        ["i", "v", "VI", "VII"],
        ["i7", "v", "VI", "VII"],
    ]

    mixolydian_progression_array = [
        ["I", "VII", "IV"],

        ["I", "IV", "VII", "IV"],

        ["I", "IV", "VII", "I"],

        ["I", "VII", "v", "IV"],
        ["I", "VII", "v", "vsus2", "IV"],
        ["I", "VII", "v", "v", "IVsus2"],

        ["I", "VII", "IV", "v"],

        ["I", "v", "VII"],
        ["I", "v", "v", "I"],
        ["I", "v7", "VII"],

        ["I", "VII", "IV", "I"],
        ["I", "VII", "IV", "I7"],
        ["I", "VII", "ii", "I"],
        ["I7", "VII", "ii", "I"],
    ]

    dorian_progression_array = [
        ["i7", "IV7", "VII"],
        ["i7", "V", "VII"],
        ["i7", "V", "VII", "III"],
        ["i", "VII", "ii"],
        ["i7", "VII", "ii"],
        ["i", "VII", "ii7"],
        ["i7", "VII", "ii7"],

        ["i", "VII", "III", "IV"],
        ["i", "III", "IV", "IV7"],
        ["i", "ii", "III", "ii"],
        ["i7", "ii", "III", "ii"],
        ["i", "v", "iv", "i"],
        ["i", "v", "iv", "i7"],
    ]

    lydian_progression_array = [
        ["I", "II", "I", "II"],
        ["I", "II", "I", "II7"],

        ["I", "II", "IV"],

        ["I", "II", "IV", "IVsus4"],

        ["I", "II", "vii", "I"],
        ["I7", "II", "vii", "I"],

        ["I", "I", "II", "V"],
        ["I7", "I", "II", "V"],
        ["I", "ii", "vii", "iii"],
        ["I", "V", "iii", "II"],
    ]

    phrygian_progression_array = [
        ["i", "II", "III"],
        ["i7", "II", "III"],
        ["i", "IIsus2", "III"],

        ["i", "VII", "III", "II"],
        ["i7", "VII", "III", "II"],
        ["i", "VII", "III7", "II"],
        ["i", "VII", "III7", "IIsus2"],

        ["i", "VII", "II", "III"],
        ["i7", "VII", "II", "III"],
        ["i", "VII", "II", "III7"],

        ["i", "II", "i", "vii"],
        ["i7", "II", "i", "vii"],
        ["i", "III", "vii", "II"],
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

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


def get_random_tempo():
    return str(random.randint(75, 140))


def get_random_drums():
    drums_array = [
        "E-mu Drumulator",

        "Korg DDD-1",

        "Linn 9000",
        "Linn LinnDrum",
        "Linn LM-1"

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
        ["i", "VII", "v", "isus2"],

        ["i", "VI", "iv", "v"],
        ["i7", "VI", "iv", "v"],
        ["i", "VI", "iv7", "v"],
        ["i", "iv", "v", "iv"],

        ["i", "VI", "III7", "v"],

        ["i7", "v", "VI"],
        ["i7", "v", "VI", "i7sus4"]
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


def get_modifier_percussion_element():
    percussion_instrument_array = [
        "clap",
        "shaker",
        "tambourin",
        "conga",
        "cowbell",
        "side snare"
    ]

    ryhthm_array = [
        "the groove",
        "a fill"
    ]

    return "**Rhythm:** Include a " + random.choice(percussion_instrument_array) + " in " + random.choice(ryhthm_array)


def get_modifier_hihat_pattern():
    type_array = [
        "continuous",
        "boken"
    ]

    beat_array = [
        "4th",
        "8th",
        "16th",
        "32th"
    ]

    random_value = random.randint(0, 100)
    hh_type = "closed"
    if random_value < 30:
        hh_type = open

    return "**Rhythm:** Include a " + random.choice(beat_array) + " " + random.choice(
        type_array) + " " + hh_type + " hihat in your groove"


def get_modifier_melody_pentatonic(mode):
    map = {
        "ionian": "major",
        "aeolian": "minor",
        "mixolydian": "major",
        "dorian": "minor",
        "phrygian": "minor",
        "lydian": "major"
    }

    mode_str = mode.name.split()[1]
    return "Use the pentatonic " + map[mode_str] + " scale"


def get_modifier_melody_scale(mode):
    mod_array = [
        get_modifier_melody_pentatonic(mode),
        "Only use chord tones",
        "Start on the Tonic",
        "End on the Tonic",
        "Start on a non-chord tone",
        "End on a non-chord tone"
    ]

    return "**Melody**: " + random.choice(mod_array)


def get_modifier_melody_range(mode):
    mod_array = [
        "Use only one octave",
        "Use at least two octaves",
        "Create an ascending melody",
        "Create a descending melody"
    ]

    return "**Melody**: " + random.choice(mod_array)


def get_modifiers(mode):
    modifier_array = []

    random_value = random.randint(0, 100)
    if random_value < 33:
        modifier_array.append(get_modifier_percussion_element())

    random_value = random.randint(0, 100)
    if random_value < 33:
        modifier_array.append(get_modifier_hihat_pattern())

    random_value = random.randint(0, 100)
    if random_value < 50:
        modifier_array.append(get_modifier_melody_scale(mode))

    random_value = random.randint(0, 100)
    if random_value < 50:
        modifier_array.append(get_modifier_melody_range(mode))

    return modifier_array


def print_to_string(*args, **kwargs):
    newstr = ""
    for a in args:
        newstr += str(a) + ' '
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
        chord_notes_array = get_chord_from_scale(mode.ascending()[:-1], chord)
        output_string += print_to_string(" * **", chord, "**,",
                                         chords.determine(chord_notes_array, True, True, True)[0],
                                         ", notes: ",
                                         chord_notes_array) + "\n"
    output_string += print_to_string("* **Modifiers:** \n")
    mods = get_modifiers(mode)
    if not mods:
        output_string += " * None\n"
    else:
        for mod in mods:
            output_string += print_to_string(" * ", mod) + "\n"

    return output_string.replace("'", "")

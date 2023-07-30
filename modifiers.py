import random


def get_modifier_percussion_element():
    percussion_instrument_array = [
        "clap",
        "shaker",
        "tambourin",
        "conga",
        "cowbell",
        "side snare",
    ]

    ryhthm_array = [
        "the groove",
        "a fill"
    ]

    return "**Rhythm:** Include a " + random.choice(percussion_instrument_array) + " in " + random.choice(ryhthm_array)


def get_modifier_drum_pattern():
    type_array = [
        "",
        "syncopated"
    ]

    beat_array = [
        "4th",
        "8th",
        "16th",
        "32th"
    ]

    # dirty hack to have entries in the array twice to increase their chance of getting picked
    instrument_array = [
        "closed hihat",
        "closed hihat",
        "open hihat",
        "snare",
        "snare",
        "kick"
    ]

    return "**Rhythm:** Include a " + random.choice(beat_array) + " " + random.choice(
        type_array) + " " + random.choice(instrument_array) + "  in your groove"


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
        "End on a non-chord tone",
        "End with a resolution using the tonic on a strong beat"
    ]

    return "**Melody**: " + random.choice(mod_array)


def get_modifier_melody_range(mode):
    mod_array = [
        "Use only one octave",
        "Use at least two octaves",
        "Create an ascending melody",
        "Use chord tones on strong beats",
        "Use non-chord-tones on weak beats",
        "Create a descending melody"
    ]

    return "**Melody**: " + random.choice(mod_array)


def get_modifier_melody_pattern():
    melody_pattern_array = [
        "A | A | B | A",
        "A | B | B | A",
        "A | A | A | B",
        "A | B | A | C",
        "A | B | C | A",
        "A | A | B | C",
    ]

    return "**Melody Pattern:** Write a melody with the pattern " + random.choice(melody_pattern_array)


def get_modifier_bass_pattern():
    beat_array = [
        "8th",
        "16th"
    ]
    type_array = [
        "rolling",
        "broken",
        "syncopated"
    ]

    return "**Bass pattern:** Use a " + random.choice(type_array) + " " + random.choice(beat_array) + " pattern"


def get_modifier_support_element():
    support_element_array = [
        "Ascending arp",
        "Descending arp",
        "Chords with rhythm",
        "Chords",
        "Pads"
    ]

    return "**Supporting Element:** " + random.choice(support_element_array)


def get_modifiers(mode):
    modifier_array = []

    random_value = random.randint(0, 100)
    if random_value < 33:
        modifier_array.append(get_modifier_percussion_element())

    random_value = random.randint(0, 100)
    if random_value < 33:
        modifier_array.append(get_modifier_drum_pattern())

    random_value = random.randint(0, 100)
    if random_value < 50:
        modifier_array.append(get_modifier_melody_scale(mode))

    random_value = random.randint(0, 100)
    if random_value < 50:
        modifier_array.append(get_modifier_melody_range(mode))

    random_value = random.randint(0, 100)
    if random_value < 66:
        modifier_array.append(get_modifier_melody_pattern())

    random_value = random.randint(0, 100)
    if random_value < 25:
        modifier_array.append(get_modifier_bass_pattern())

    random_value = random.randint(0, 100)
    if random_value < 25:
        modifier_array.append(get_modifier_support_element())

    return modifier_array

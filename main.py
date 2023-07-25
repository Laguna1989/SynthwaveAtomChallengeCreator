import random


def get_random_mode():
    mode_array = [
        "A♭ Major", "A Major", "B♭ Major", "B Major", "C Major", "D♭ Major", "D Major", "E♭ Major", "E Major",
        "F Major", "F♯ Major", "G Major",

        "A Minor", "B♭ Minor", "B Minor", "C Minor", "C♯ Minor", "D Minor", "D♯ Minor", "E Minor", "F Minor",
        "F♯ Minor", "G Minor", "G♯ Minor",

        "A♭ Mixolydian", "A Mixolydian", "B♭ Mixolydian", "B Mixolydian", "C Mixolydian", "C♯ Mixolydian",
        "D Mixolydian", "E♭ Mixolydian", "E Mixolydian", "F Mixolydian", "F♯ Mixolydian", "G Mixolydian",

        "A Dorian", "B♭ Dorian", "B Dorian", "C Dorian", "C♯ Dorian", "D Dorian", "E♭ Dorian", "E Dorian",
        "F Dorian", "F♯ Dorian", "G Dorian", "G♯ Dorian",

        "A Phrygian", "A♯ Phrygian", "B Phrygian", "C Phrygian", "C♯ Phrygian", "D Phrygian", "D♯ Phrygian",
        "E Phrygian", "F Phrygian", "F♯ Phrygian", "G Phrygian", "G♯ Phrygian",

        "A♭ Lydian", "A Lydian", "B♭ Lydian", "B Lydian", "C Lydian", "D♭ Lydian", "D Lydian", "E♭ Lydian",
        "E Lydian", "F Lydian", "G♭ Lydian", "G Lydian"
    ]

    return random.choice(mode_array)


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
    aeolian_progression_array = [
        "i - VII - v",
        "i - VI - iv - v",
        "i - iv - v - iv",
        "i - VII - VI - iv,"
        "i - VI - III ,- v"
        "i - VII - VI",
        "i - VI - IV - v",
        "i - iv - v - III",
        "i - VI - III - iv",
        "i - VII - VI - III"
    ]

    ionian_progression_array = [
        "I - IV - V",
        "I - vi - IV - V",
        "I - V - vi - IV",
        "I - iii - vi - IV",
        "I - IV - vi - V",
        "I - vi - ii - V",
        "I - V - IV - I",
        "I - vi - IV",
        "I - iii - IV - V",
        "I - ii - IV - V"
    ]

    mixolydian_progression_array = [
        "I - VII - IV",
        "I - IV - VII - IV",
        "I - VII - v - IV",
        "I - VII - IV - v",
        "I - V - VII",
        "I - VII - ii - IV",
        "I - IV - v - VII",
        "I - VII - IV - VII",
        "I - V - VII - IV",
        "I - VII - vi - V"
    ]

    dorian_progression_array = [
        "ii - IV - v",
        "ii - IV - I - V",
        "ii - I - IV - V",
        "ii - v - IV - I",
        "ii - IV - vi - V",
        "ii - vi - IV - V",
        "ii - IV - v - IV",
        "ii - vi - IV",
        "ii - v - IV - vi",
        "ii - IV - vi - I"
    ]

    phrygian_progression_array = [
        "i - II - III",
        "i - VII - III - II",
        "i - II - III - iv",
        "i - VII - II - III",
        "i - II - VII - III",
        "i - III - iv",
        "i - VII - iv",
        "i - III - II",
        "i - II - VII - iv",
        "i - VII - iv - III"
    ]

    lydian_progression_array = [
        "I - II - IV",
        "I - II - V",
        "I - II - IV - V",
        "II - IV - V",
        "I - III - IV",
        "I - II - III - IV",
        "I - II - vi - V",
        "I - IV - V",
        "II - III - IV",
        "I - II - V - IV"
    ]

    map = {
        "Major": ionian_progression_array,
        "Minor": aeolian_progression_array,
        "Mixolydian": mixolydian_progression_array,
        "Dorian": dorian_progression_array,
        "Phrygian": phrygian_progression_array,
        "Lydian": lydian_progression_array
    }

    mode_str = mode.split()[1]
    return random.choice(map[mode_str])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("tempo: ", get_random_tempo(), "bpm")
    print("timing: 4/4")
    mode = get_random_mode();
    print("mode: ", mode)
    print("total length: 60-90s")
    print("drums: ", get_random_drums())
    print("chord progression: ", get_random_chord_progression(mode))

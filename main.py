import random
import mingus.core.scales as scales

def get_random_mode():

    tonic_array = ["A", "B", "C", "D", "E", "F", "G"]
    tonic = random.choice(tonic_array)

    modes_array = [scales.Ionian(tonic), scales.Aeolian(tonic), scales.Dorian(tonic), scales.Mixolydian(tonic), scales.Lydian(tonic), scales.Phrygian(tonic)]
    mode = random.choice(modes_array)

    return mode.name



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
    ]

    dorian_progression_array = [
        "i7 - IV7 - VII",
    ]

    phrygian_progression_array = [
        "i - II - III"
    ]

    lydian_progression_array = [
        "I - II - IV",
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("tempo: ", get_random_tempo(), "bpm")
    print("timing: 4/4")
    mode = get_random_mode();
    print("mode: ", mode)
    print("total length: 60-90s")
    print("drums: ", get_random_drums())
    print("chord progression: ", get_random_chord_progression(mode))

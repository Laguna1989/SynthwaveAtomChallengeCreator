from mingus.core import chords as chords

from drums import get_random_drums
from harmonies import get_random_mode, get_chord_from_scale, get_random_chord_progression
from modifiers import get_modifiers
from timings import get_random_tempo, get_timing, get_track_duration


def print_to_string(*args, **kwargs):
    newstr = ""
    for a in args:
        newstr += str(a) + ' '
    return newstr


def get_atom_instruction_string() -> str:
    output_string = ""
    output_string += print_to_string("* **Tempo:**", get_random_tempo(), "bpm") + "\n"
    output_string += print_to_string("* **Timing:**", get_timing()) + "\n"
    output_string += print_to_string("* **Total length:**", get_track_duration()) + "\n"

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

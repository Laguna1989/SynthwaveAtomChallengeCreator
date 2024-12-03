from mingus.core import chords as chords

from atom_arguments import AtomArguments
from drums import get_drums
from harmonies import get_chord_from_scale, get_random_chord_progression, get_mode
from modifiers import get_modifiers
from timings import get_timing, get_track_duration, get_tempo


def print_to_string(*args, **kwargs):
    newstr = ""
    for a in args:
        newstr += str(a) + ' '
    return newstr


def get_atom_instruction_string(args: AtomArguments) -> str:
    output_string = ""

    output_string += print_to_string("* **Tempo:**", get_tempo(args), "bpm") + "\n"
    output_string += print_to_string("* **Timing:**", get_timing()) + "\n"
    output_string += print_to_string("* **Total length:**", get_track_duration()) + "\n"

    output_string += print_to_string("* **Drums:**", get_drums(args)) + "\n"

    mode = get_mode(args)
    key = mode.name.split(" ")[0]
    mode_name = mode.name.split(" ")[1]
    output_string += print_to_string("* **Key:**", key) + "\n"
    output_string += print_to_string("* **Mode:**", mode_name) + "\n"
    output_string += print_to_string("  * **Notes in scale:**", mode.ascending()) + "\n"

    chord_progression = get_random_chord_progression(mode.name, args)
    output_string += print_to_string("* **chord progression:**", chord_progression) + "\n"
    for chord in chord_progression:
        chord_notes_array = get_chord_from_scale(mode.ascending()[:-1], chord)
        determined_chords = chords.determine(chord_notes_array, True, True, True)
        determined_chord_name = "[...]"
        if determined_chords:
            determined_chord_name = determined_chords[0]
        output_string += print_to_string(f"  * **{chord}** -",
                                         determined_chord_name,
                                         "- notes: ",
                                         chord_notes_array) + "\n"
    output_string += print_to_string("* **Modifiers:**") + "\n"
    mods = get_modifiers(mode)
    if not mods:
        output_string += " * None\n"
    else:
        for mod in mods:
            output_string += print_to_string("  * ", mod) + "\n"

    return output_string.replace("'", "")

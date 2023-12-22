import pytest

from arguments_from_string import handle_atom_call
from atom_arguments import AtomArguments, get_mode_from_string, get_chords_from_string
from atom_instructions import get_atom_instruction_string


@pytest.mark.parametrize("content", ["", "atom", "!atöm", "!blatom", "!ato", "!atomhlep"])
def test_handle_atom_call_with_invalid_input(content):
    result = handle_atom_call(content, None)
    assert result == ""


@pytest.mark.parametrize("content", [
    "!atom",
    "!atom --mode aeolian",
    "!atom -k C",
    "!ATOM -k Bb",
    "!Atom --tempo 90 --drums 'Roland R8'",
    "!Atom --k C -m dorian",
    "!Atom --chords 'I, vi7, IV, V7'"
])
def test_handle_atom_call_with_valid_atom_input(content):
    result = handle_atom_call(content, None)
    assert result.startswith("Here are your instructions:\n")


@pytest.mark.parametrize("content", [
    "!atom h",
    "!atom -mode aeolian",
    "!atom -k Y",
    "!ATOM -k zz"
])
def test_handle_atom_call_with_valid_atom_input_and_invalid_arguments(content):
    result = handle_atom_call(content, None)
    assert result.startswith(":exclamation:")


@pytest.mark.parametrize("content", [
    "!atomhelp",
])
def test_handle_atom_call_with_valid_atomhelp_input(content):
    result = handle_atom_call(content, None)
    assert result


def test_get_instructions_with_args_tempo():
    args = AtomArguments()
    args.tempo = 99

    instructions = get_atom_instruction_string(args)

    assert "99 bpm" in instructions


def test_get_instructions_with_args_drums():
    args = AtomArguments()
    args.drums = "IBimsDrums"

    instructions = get_atom_instruction_string(args)

    assert "IBimsDrums" in instructions


def test_get_instructions_with_args_mode_CMaj():
    args = AtomArguments()
    key_string = "C"
    mode_string = "Major".casefold()
    args.mode = get_mode_from_string(key_string, mode_string)

    instructions = get_atom_instruction_string(args)

    assert "**Key:** C" in instructions
    assert "**Mode:** ionian" in instructions


def test_get_instructions_with_args_mode_CMin():
    args = AtomArguments()
    key_string = "C"
    mode_string = "minor"
    args.mode = get_mode_from_string(key_string, mode_string)

    instructions = get_atom_instruction_string(args)

    assert "**Key:** C" in instructions
    assert "**Mode:** aeolian" in instructions


@pytest.mark.parametrize("mode_name", ["X", "Y", "Bla Blubb", "? Blubb", "Bla ?"])
def test_get_mode_from_string_invalid_input(mode_name):
    assert get_mode_from_string("C", mode_name) is None
    assert get_mode_from_string(mode_name, "aeolian") is None


@pytest.mark.parametrize("key_name, mode_name", [
    ("C", "ionian"),
    ("C#", "ionian"),
    ("D", "ionian"),
    ("E", "ionian"),
    ("F", "ionian"),
    ("G", "ionian"),
    ("A", "ionian"),
    ("B", "ionian"),
    ("C", "Ionian"),
    ("C", "Major"),
    ("C", "major"),
    ("C", "minor"),
    ("C", "Minor"),
    ("C", "Aeolian"),
    ("C", "aeolian"),
    ("C#", "dorian"),
    ("C#", "lydian"),
    ("C#", "mixolydian"),
    ("C#", "phrygian")
])
def test_get_mode_from_string_valid_input(key_name, mode_name):
    assert get_mode_from_string(key_name, mode_name.casefold()) is not None


@pytest.mark.parametrize("chord_string, expected_chords", [
    ("I", ["I"]),
    ("I II", ["I", "II"]),
    ("I, II", ["I", "II"]),
    ("i, VII", ["i", "VII"])
])
def test_get_chords_from_string(chord_string, expected_chords):
    result_chords = get_chords_from_string(chord_string)
    assert result_chords == expected_chords

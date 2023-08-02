import pytest

from atom_arguments import AtomArguments, get_mode_from_string, get_chords_from_string
from atom_instructions import get_atom_instruction_string


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
    mode_string = "Major"
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
    ("C", "aeolian")
])
def test_get_mode_from_string_valid_input(key_name, mode_name):
    assert get_mode_from_string(key_name, mode_name) is not None


@pytest.mark.parametrize("chord_string, expected_chords", [
    ("I", ["I"]),
    ("I II", ["I", "II"]),
    ("I, II", ["I", "II"]),
    ("i, VII", ["i", "VII"])
])
def test_get_chords_from_string(chord_string, expected_chords):
    result_chords = get_chords_from_string(chord_string)
    assert result_chords == expected_chords

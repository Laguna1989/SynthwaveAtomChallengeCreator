import pytest

from mingus.core import scales as scales

from arguments_from_string import get_arguments_from_string
from atom_arguments import get_mode_from_string, get_chords_from_string


def test_arguments_from_string_empty_string():
    atom_arguments = get_arguments_from_string("")
    assert atom_arguments.tempo == -1
    assert atom_arguments.drums == ""
    assert atom_arguments.mode is None
    assert atom_arguments.chords == ""


@pytest.mark.parametrize("tempo", ["30", "100", "120", "1000"])
def test_arguments_from_string_tempo(tempo):
    atom_arguments = get_arguments_from_string("!atom -t " + tempo)
    assert atom_arguments.tempo == int(tempo)
    assert atom_arguments.drums == ""
    assert atom_arguments.mode is None
    assert atom_arguments.chords == ""


@pytest.mark.parametrize("drums", [
    "drumA",
    "Drum B",
    "My Fancy Drums With Lots of Spaces",
    "1000"
])
def test_arguments_from_string_drums(drums):
    atom_arguments = get_arguments_from_string("!atom -d '" + drums + "'")
    assert atom_arguments.tempo == -1
    assert atom_arguments.drums == drums
    assert atom_arguments.mode is None
    assert atom_arguments.chords == ""


@pytest.mark.parametrize("mode", [
    "ionian", "aeolian", "dorian", "mixolydian", "lydian", "phrygian"
])
def test_arguments_from_string_mode(mode):
    atom_arguments = get_arguments_from_string("!atom -m '" + mode + "'")
    assert atom_arguments.tempo == -1
    assert atom_arguments.drums == ""
    assert mode in atom_arguments.mode.name
    assert atom_arguments.chords == ""


@pytest.mark.parametrize("key", [
    "C", "D", "E", "F", "G", "A", "B"
])
def test_arguments_from_string_key(key):
    atom_arguments = get_arguments_from_string("!atom -k '" + key + "'")
    assert atom_arguments.tempo == -1
    assert atom_arguments.drums == ""
    assert key in atom_arguments.mode.name
    assert atom_arguments.chords == ""


@pytest.mark.parametrize("chords", [
    "I, II, III",
    "i, i7 i7sus2"
])
def test_arguments_from_string_chords(chords):
    atom_arguments = get_arguments_from_string("!atom -c '" + chords + "'")
    assert atom_arguments.tempo == -1
    assert atom_arguments.drums == ""
    assert atom_arguments.mode is None
    assert atom_arguments.chords == get_chords_from_string(chords)

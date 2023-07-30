import mingus.core.scales
import pytest

from harmonies import get_chord_from_scale

# C D E F G A B
c_ionian_notes = mingus.core.scales.Ionian("C").ascending()[:-1]

# B C# D# E F# G# A# B
b_ionian_notes = mingus.core.scales.Ionian("B").ascending()[:-1]


@pytest.mark.parametrize("chord, expected_notes_in_chord",
                         [("I", ["C", "E", "G"]),
                          ("i", ["C", "E", "G"]),
                          ("II", ["D", "F", "A"]),
                          ("ii", ["D", "F", "A"]),
                          ("III", ["E", "G", "B"]),
                          ("iii", ["E", "G", "B"]),
                          ("IV", ["F", "A", "C"]),
                          ("iv", ["F", "A", "C"]),
                          ("V", ["G", "B", "D"]),
                          ("v", ["G", "B", "D"]),
                          ("VI", ["A", "C", "E"]),
                          ("vi", ["A", "C", "E"]),
                          ("VII", ["B", "D", "F"]),
                          ("vii", ["B", "D", "F"])
                          ])
def test_get_chord_from_c_ioninan_scale_valid(chord, expected_notes_in_chord):
    notes_in_chord = get_chord_from_scale(c_ionian_notes, chord)
    assert notes_in_chord == expected_notes_in_chord


@pytest.mark.parametrize("chord, expected_notes_in_chord",
                         [("Isus2", ["C", "D", "G"]),
                          ("IIsus2", ["D", "E", "A"]),
                          ("IIIsus2", ["E", "F", "B"]),
                          ("IVsus2", ["F", "G", "C"]),
                          ("Vsus2", ["G", "A", "D"]),
                          ("VIsus2", ["A", "B", "E"]),
                          ("VIIsus2", ["B", "C", "F"]),
                          ])
def test_get_sus2_chord_from_c_ioninan_scale_valid(chord, expected_notes_in_chord):
    notes_in_chord = get_chord_from_scale(c_ionian_notes, chord)
    assert notes_in_chord == expected_notes_in_chord


@pytest.mark.parametrize("chord, expected_notes_in_chord",
                         [("Isus4", ["C", "F", "G"]),
                          ("IIsus4", ["D", "G", "A"]),
                          ("IIIsus4", ["E", "A", "B"]),
                          ("IVsus4", ["F", "B", "C"]),
                          ("Vsus4", ["G", "C", "D"]),
                          ("VIsus4", ["A", "D", "E"]),
                          ("VIIsus4", ["B", "E", "F"]),
                          ])
def test_get_sus4_chord_from_c_ioninan_scale_valid(chord, expected_notes_in_chord):
    notes_in_chord = get_chord_from_scale(c_ionian_notes, chord)
    assert notes_in_chord == expected_notes_in_chord


@pytest.mark.parametrize("chord, expected_notes_in_chord",
                         [("I7", ["C", "E", "G", "B"]),
                          ("II7", ["D", "F", "A", "C"]),
                          ("III7", ["E", "G", "B", "D"]),
                          ("IV7", ["F", "A", "C", "E"]),
                          ("V7", ["G", "B", "D", "F"]),
                          ("VI7", ["A", "C", "E", "G"]),
                          ("VII7", ["B", "D", "F", "A"])
                          ])
def test_get_seventh_chord_from_c_ioninan_scale_valid(chord, expected_notes_in_chord):
    notes_in_chord = get_chord_from_scale(c_ionian_notes, chord)
    assert notes_in_chord == expected_notes_in_chord


@pytest.mark.parametrize("chord, expected_notes_in_chord",
                         [("I7sus4", ["C", "F", "G", "B"]),
                          ("II7sus4", ["D", "G", "A", "C"]),
                          ("III7sus4", ["E", "A", "B", "D"]),
                          ("IV7sus4", ["F", "B", "C", "E"]),
                          ("V7sus4", ["G", "C", "D", "F"]),
                          ("VI7sus4", ["A", "D", "E", "G"]),
                          ("VII7sus4", ["B", "E", "F", "A"]),
                          ])
def test_get_7_sus4_chord_from_c_ioninan_scale_valid(chord, expected_notes_in_chord):
    notes_in_chord = get_chord_from_scale(c_ionian_notes, chord)
    assert notes_in_chord == expected_notes_in_chord


# B C# D# E F# G# A#
@pytest.mark.parametrize("chord, expected_notes_in_chord",
                         [("I", ["B", "D#", "F#"]),
                          ("i", ["B", "D#", "F#"]),
                          ("II", ["C#", "E", "G#"]),
                          ("ii", ["C#", "E", "G#"]),
                          ("III", ["D#", "F#", "A#"]),
                          ("iii", ["D#", "F#", "A#"]),
                          ("IV", ["E", "G#", "B"]),
                          ("iv", ["E", "G#", "B"]),
                          ("V", ["F#", "A#", "C#"]),
                          ("v", ["F#", "A#", "C#"]),
                          ("VI", ["G#", "B", "D#"]),
                          ("vi", ["G#", "B", "D#"]),
                          ("VII", ["A#", "C#", "E"]),
                          ("vii", ["A#", "C#", "E"])
                          ])
def test_get_chord_from_b_ioninan_scale_valid(chord, expected_notes_in_chord):
    notes_in_chord = get_chord_from_scale(b_ionian_notes, chord)
    assert notes_in_chord == expected_notes_in_chord

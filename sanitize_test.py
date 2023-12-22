import pytest

from sanitize import is_sane_input


@pytest.mark.parametrize("test_input", [
    "!atom",
    "!atom --tempo 123",
    "!atom -k C", "!Atom --tempo 90 --drums 'Roland R8'",
    "!Atom --k C -m dorian",
    "!Atom --chords 'I, vi7, IV, V7'",
    "!atomhelp",
    "!Atomhelp"
])
def test_is_sane_input_returns_true_on_valid_input(test_input):
    assert is_sane_input(test_input) == True


@pytest.mark.parametrize("test_input", [
    15,
    "!atom .",
    "!atom §",
    "!atom $",
    "!atom %",
    "!atom &",
    "!atom :",
    "!atom ; rm -rf *",
    "!atom )",
    "!atom (",
    "!atom \\",
    "!atom /",
    "!atom ?",
    "!atom [",
    "!atom ]",
    "!atom {",
    "!atom }",
    "!atom |",
    "!atom >",
    "!atom <",
    "!atom °",
    "!atom ^",
    "!atom ´",
    "!atom `"
])
def test_is_sane_input_returns_false_on_invalid_input(test_input):
    assert is_sane_input(test_input) == False

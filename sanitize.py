import re


def is_sane_input(message):
    if not isinstance(message, str):
        return False

    disallowed_chars = ['.', ';', ':', '*', ")", '(', '\\', '/', '?', '§', '$', '%', '&', '[', ']', '{', '}', '|', '<',
                        '>', '°', '^', '´', '`']

    if any(c in message for c in disallowed_chars):
        return False
    return True

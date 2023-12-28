
# Logical functions

import sys

# Global variables
exponents_map = {'BYTES': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
unit = 'GB'

# Constants
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
DEFAULT = "\033[0m"  # Reset

def check_argv():
    global unit
    if len(sys.argv) == 1:
        unit = 'GB' # Default
    elif check_unit_input(sys.argv[1]):
        unit = sys.argv[1].upper()
    else:
        print("input is wrong! Must select from\
        ['BYTES', 'KB', 'MB', 'GB', 'TB']")

def check_unit_input():
    global exponents_map, unit
    unit_upper = unit.upper()

    if unit_upper in exponents_map:
        return True
    else:
        return False

def size_format(size):
    global exponents_map, unit

    if unit not in exponents_map:
        raise ValueError("Must select from   ['BYTES', 'KB', 'MB', 'GB', 'TB']")
    else:
        res = size / 1024 ** exponents_map[unit]
        return str(round(res, 3)) + unit

def get_font_color(percentage):
    if percentage <= 25:
        return GREEN
    elif percentage <= 50:
        return YELLOW
    else:
        return RED

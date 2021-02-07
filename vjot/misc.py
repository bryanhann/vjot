import sys
import pathlib

# Define the root directory of the project
ROOT = pathlib.Path(__file__).parent.parent

# Import 'SAMPLE_INFO' object
sys.path = [str(ROOT/'sample')] + sys.path
from metadata import SAMPLE
del sys.path[0]

assert ROOT    # this name is defined in our namespace
assert SAMPLE  # this name is defined in our namespace

def unique_sorted(seq): return sorted(list(set(seq)))
def stamp4path(path): return path.name.split('.')[0]
def stamps4path(path): return unique_sorted(map(stamp4path, path.glob('*T*')))

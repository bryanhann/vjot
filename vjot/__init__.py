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

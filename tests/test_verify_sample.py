##!/usr/bin/env python3

import sys
import os

from vjot import SAMPLE
from vjot.misc import stamps4path

def test_stamps4path3():
    assert stamps4path(SAMPLE.path) == SAMPLE.stamps




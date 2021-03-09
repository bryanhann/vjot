#!/usr/bin/env python3

import string
from datetime import datetime
from pathlib import Path
import os

from vjot.stamp import *
VJOT_RAW = Path(os.environ['VJOT_RAW'])

def __paths4dt(root):
    acc = {}
    for path in root.glob('**/*'):
        dt=stamp4path(path).dt()
        if not dt in acc: acc[dt]=[]
        acc[dt].append(path)
    return acc

PATHS_4_DT=__paths4dt(VJOT_RAW)



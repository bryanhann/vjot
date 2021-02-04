##!/usr/bin/env python3
import os

def unique_sorted(seq): return sorted(list(set(seq)))
def stamp4path(path): return path.name.split('.')[0]
def stamps4path(path): return unique_sorted(map(stamp4path, path.glob('*')))


def test_stamps4path(SAMPLE_STAMPS,paths):
    assert SAMPLE_STAMPS == stamps4path(paths.sample)


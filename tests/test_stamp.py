import itertools
import datetime
import pytest
from vjot.stamp import _Stamp
from vjot.constants import PATHS_4_DT as DICT



def test_PATHS_4_DT():
    keys = [ key for key in DICT.keys() if key ]
    keys.sort()
    for key in keys + [None]:
        print(key)
        for x in DICT[key]:
            print('\t', x)

def test_Stamp_mangled_string():
    full = datetime.datetime(2020,11,12,13,14,15)
    assert _Stamp('#2020!11 12-T-)1(3X-14-15').dt() == full
    assert _Stamp('#2020!11 12-T-)1(3T-14-15').dt() == full
    assert _Stamp('#2020!11 12-T-)1(3t-14-15').dt() == full
    assert _Stamp('#2020!11 12-t-)1(3X-14-15').dt() == full
    assert _Stamp('#2020!11 12-t-)1(3T-14-15').dt() == full
    assert _Stamp('#2020!11 12-X-)1(3T-14-15').dt() == None

def test_Stamp_date_time():
    date = datetime.date(2020,11,12)
    time = datetime.time(13,14,15)
    full = datetime.datetime(2020,11,12,13,14,15)
    assert _Stamp('2020-11-12-T-13-14-15').dt() == full
    assert _Stamp('2020-11-12-T-13-14-15').date_time() == (date, time)
    assert _Stamp('2020-11-12-T-xxxxxxxx').date_time() == (date, None)
    assert _Stamp('2020-11-12-T'         ).date_time() == (date, None)
    assert _Stamp('2020-11-12'           ).date_time() == (None, None)
    assert _Stamp('xxxxxxxxxx-T-13-14-15').date_time() == (None, time)
    assert _Stamp(           'T-13-14-15').date_time() == (None, time)
    assert _Stamp(             '13-14-15').date_time() == (None, None)

def test_Stamp_raw_XXX():
    """Test invariants of .raw_date(), .raw_time(), and .raw_tee(), against a variety of strings.
    """
    for product in itertools.product( ['a',''], ['t','T',''], ['b',''], ['t','T',''], ['c',''] ):
        stamp = _Stamp( ''.join(product) )
        assert stamp == stamp.raw_date() + stamp.raw_time()
        assert stamp.raw_time().startswith(stamp.raw_tee())
        assert stamp.raw_tee() in ['T', 't', '']
        assert not 'T' in stamp.raw_date()
        assert not 't' in stamp.raw_date()

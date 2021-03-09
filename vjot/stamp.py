
import string
from datetime import datetime
from pathlib import Path
import os

def stamp4path(path):
    return _Stamp(path.name.split('.')[0])

def string_keep(_str, keepers):
    acc = [char for char in _str if char in keepers]
    return ''.join(acc)

def chop_targets(string,targets):
    def post_assert( string, targets, left, right ):
        assert left + right == string
        for ch in targets:
            assert not ch in left
        assert right=='' or right[0] in targets
    def find_target(string,targets):
        for ii, ch in enumerate(string):
            if string[ii] in targets:
                return ii
        return len(string)
    ii = find_target(string,targets)
    left, right = string[:ii], string[ii:]
    post_assert( string, targets, left, right )
    return left, right


#def __chop_targets(string,targets):
#    ii = _find_target(string,targets)
#    return string[:ii], string[ii:]


def _pos4str4targets(_str,_targets):
    for ii, char in enumerate(_str):
        if char in _targets:
            return ii
    return len(_str)


def date4yyyymmdd(yyyymmdd):
    try: return datetime.strptime(yyyymmdd, "%Y%m%d").date()
    except ValueError: return None
def time4hhmmss(hhmmss):
    try: return datetime.strptime(hhmmss, "%H%M%S").time()
    except ValueError: return None

class _Stamp(str):
    def __init__(self,string):
        str.__init__(string)
        date, time = chop_targets(self, 'tT')
        self._rawdate = date
        self._rawtime = time
        self._yyyymmdd = string_keep(date, '0123456789')
        self._hhmmss = string_keep(time, '0123456789')
        if self.isvalid():
            self._date = date4yyyymmdd(self._yyyymmdd)
            self._time = time4hhmmss(self._hhmmss)
        else:
            self._date = None
            self._time = None

    def isvalid(self): return self._rawtime != ''
    def raw_tee(self): return self.raw_time()[:1]
    def raw_date(self): return self._rawdate
    def raw_time(self): return self._rawtime
    def date(self): return self._date
    def time(self): return self._time
    def date_time(self): return self.date(), self.time()

    def dt(self):
        date=self.date()
        time=self.time()
        if date and time:
            return datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)
        else:
            return None


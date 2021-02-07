"""
The namespace SAMPLE will hold two names:
    SAMPLE.path  : the path to the folder containing the sample files
    SAMPLE.stamps : a list of the folder's relavent timestamps.
"""

import pathlib

class __Namespace(): pass

SAMPLE = __Namespace()

SAMPLE.path = pathlib.Path(__file__).parent

SAMPLE.stamps="""
20200923T193234
20200923T193330
20200923T195246
20200923T195906
20200924T190944
20200924T191456
20200924T191636
20200924T191802
20200924T192626
""".split()


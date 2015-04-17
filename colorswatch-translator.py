#!/usr/bin/python

#   Copyright (c) 2015 Martin F. Falatic
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""

"""

from __future__ import print_function

from collections import OrderedDict
import re


def TranslateColorTable(infile):
    ''' Usage: TranslateColorTable("tkcolors") '''
    DofL = OrderedDict()
    with open(infile) as f:
        for line in f:
            m = re.match(r"^(.+?)\t(.+?)\t(.+?)\t(.+?)$", line)
            if m:
                name = m.group(1)
                red = int(m.group(2))
                grn = int(m.group(3))
                blu = int(m.group(4))
                rgb = '{0:02X}{1:02X}{2:02X}'.format(red, grn, blu)
                if rgb in DofL.keys():
                    DofL[rgb].append(name)
                else:
                    DofL[rgb] = [name]
    print('COLORS_DICT = OrderedDict([')
    for d in DofL:
        print('    (\'{0}\', {1}),'.format(d, repr(DofL[d])))
    print('])')

if __name__ == "__main__":
    TranslateColorTable("colors_tk.orig")

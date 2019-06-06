# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/FiveFingerSilver
# License: GNU AGPL, version 3 or later; https://www.gnu.org/licenses/agpl.txt

# Based on Anki 2.0.52 src
# No difference with 2.1.8 src


from anki.stats import *
from anki.hooks import wrap
from anki.lang import _



# From: anki.stats.CollectionStats
# Mod: added range and type 3
def _easeInfo(self, eases, _old):
    TYPES = {0: [0, 0], 1: [0, 0], 2: [0,0], 3: [0, 0]}
    #TODO: Rename TYPES, must not be global

    for (type, ease, cnt) in eases:
        if ease == 1:
            TYPES[type][0] += cnt
        else:
            TYPES[type][1] += cnt
    i = []
    for type in range(4):
        (bad, good) = TYPES[type]
        tot = bad + good
        try:
            pct = good / float(tot) * 100
        except:
            pct = 0
        i.append(_(
            "Correct: <b>%(pct)0.2f%%</b><br>(%(good)d of %(tot)d)") % dict(
            pct=pct, good=good, tot=tot))
    return ("""
<center><table width=%dpx><tr><td width=50></td><td align=center>""" % self.width +
            "</td><td align=center>".join(i) +
            "</td></tr></table></center>")

CollectionStats._easeInfo=wrap(CollectionStats._easeInfo, _easeInfo, 'around')

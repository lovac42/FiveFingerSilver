# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/FiveFingerSilver
# License: GNU AGPL, version 3 or later; https://www.gnu.org/licenses/agpl.txt
# Version: 0.0.1

# Based on Anki 2.0.52 src
# No difference with 2.1.8 src


from anki.stats import *
from anki.hooks import wrap


# From: anki.stats.CollectionStats
# Mod: fixed learning stats for plan9/0/X
def _eases(self, _old):
    lims = []
    lim = self._revlogLimit()
    if lim:
        lims.append(lim)
    if self.type == 0:
        days = 30
    elif self.type == 1:
        days = 365
    else:
        days = None
    if days is not None:
        lims.append("id > %d" % (
            (self.col.sched.dayCutoff-(days*86400))*1000))
    if lims:
        lim = "where " + " and ".join(lims)
    else:
        lim = ""
    return self.col.db.all("""
select (case
when type in (0,2) then 0
when lastIvl < 21 then 1
else 2 end) as thetype,
ease, count() from revlog %s
group by thetype, ease
order by thetype, ease""" % lim)

CollectionStats._eases=wrap(CollectionStats._eases, _eases, 'around')


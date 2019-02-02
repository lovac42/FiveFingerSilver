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
# Mod: added button 0 label for rememorize 
def easeGraph(self, _old):
    # 3 + 4 + 4 + spaces on sides and middle = 15
    # yng starts at 1+3+1 = 5
    # mtr starts at 5+4+1 = 10
    d = {'lrn':[], 'yng':[], 'mtr':[]}
    types = ("lrn", "yng", "mtr")
    eases = self._eases()
    for (type, ease, cnt) in eases:
        if type == 1:
            ease += 5
        elif type == 2:
            ease += 10
        n = types[type]
        d[n].append((ease, cnt))
    ticks = [[0,'ReM'],[1,1],[2,2],[3,3],[4,4],
             [5,'ReM'],[6,1],[7,2],[8,3],[9,4],
             [10,'ReM'],[11, 1],[12,2],[13,3],[14,4]]
    txt = self._title(_("Answer Buttons"),
                      _("The number of times you have pressed each button."))
    txt += self._graph(id="ease", data=[
        dict(data=d['lrn'], color=colLearn, label=_("Learning")),
        dict(data=d['yng'], color=colYoung, label=_("Young")),
        dict(data=d['mtr'], color=colMature, label=_("Mature")),
        ], type="barsLine", conf=dict(
            xaxis=dict(ticks=ticks, min=-1, max=15)),
        ylabel=_("Answers"))
    txt += self._easeInfo(eases)
    return txt

CollectionStats.easeGraph=wrap(CollectionStats.easeGraph, easeGraph, 'around')


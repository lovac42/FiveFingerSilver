# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/FiveFingerSilver
# License: GNU AGPL, version 3 or later; https://www.gnu.org/licenses/agpl.txt

# Based on Anki 2.0.52 src
# No difference with 2.1.8 src


from anki.stats import *
from anki.hooks import wrap


TYPES=("lrn", "yng", "mtr", 'rel')

# 5 + 5 + 5 + 5 = 20 (0 based)
TICKS=[[0,'ReM'],[1,1],[2,2],[3,3],[4,4], #lrn
       [5,'ReM'],[6,1],[7,2],[8,3],[9,4], #young
       [10,'ReM'],[11, 1],[12,2],[13,3],[14,4], #mature
                  [16,1],[17,2],[18,3],[19,4]]  #lapsed


# From: anki.stats.CollectionStats
# Mod: added button 0 label for rememorize 
# Mod2: separated relearn stats
def easeGraph(self, _old):
    EASES=self._eases()
    d = {'lrn':[], 'yng':[], 'mtr':[], 'rel': []}
    for (type, ease, cnt) in EASES:
        # if cnt <= 0: return "" #not sure why this was used in the addon:ReLrn stats
        n=TYPES[type]
        ease+=5*type
        d[n].append((ease, cnt))

    txt = self._title(_("Answer Buttons"),
                      _("The number of times you have pressed each button."))

    txt += self._graph(id="ease", data=[
        dict(data=d['lrn'], color=colLearn, label=_("Learning")),
        dict(data=d['yng'], color=colYoung, label=_("Young")),
        dict(data=d['mtr'], color=colMature, label=_("Mature")),
        dict(data=d['rel'], color=colRelearn, label=_("Relearn")),
        ], type="barsLine", conf=dict(
            xaxis=dict(ticks=TICKS, min=-1, max=20)),
        ylabel=_("Answers"))

    txt += self._easeInfo(EASES)
    return txt


CollectionStats.easeGraph=wrap(CollectionStats.easeGraph, easeGraph, 'around')


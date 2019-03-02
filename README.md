# FiveFingerSilver: Fix answer button graph


This addon is used to fix the answer button graph label and stats for ReMemorize and Plan9/0. But since this addon conflicts with another addon and that one is not yet available for 2.1, I went ahead and added those ideas into this addon.

<img src="https://github.com/lovac42/FiveFingerSilver/blob/master/screenshots/graphs.png?raw=true">

## Credits:
Relearn Stats 1.0 C 2014-2015 by Teemu Pudas https://ankiweb.net/shared/info/1999018922



## V1-V2 logging inconsistencies:
For learning cards, in V1 there are 3 buttons, the good button is mapped to ease2. But in V2, hard button repeats, we have 4 grading buttons, and the good button is mapped to ease3.

(Still with me?)

In anki.stats.py, when generating stats, it uses old code for V1. So ease4 and ease3 are counted as ease3. The old stats data from V1 and the new stats for V2 will be merged, so the hard button (v2) and the good button (v1) are merged as one bar on the graph. And the good button (v1) and the easy button (v2) are merged as one bar.

<b>To see what I mean. Start out with V1, grade 3 cards as again, good, and easy. Look at stats. Then switch over to V2, grade 4 cards as again, hard, good, and easy. Look at stats again. Good btn stats (V1) is merged with hard btn stats (V2) and the same for the other grades.</b>

Fixing this was not the intention of this addon, just be aware that data from V1 and V2 will skew the stats for learning cards and the old stats from V1 will interfere with the new stats after switching to V2 for at least a month before it tapers off.

(And I will not even bother to go into details about filter deck logging inconsistencies between V1-V2. With these findings, we can forget about any sort of accurate matrix schedulers.)

And lets hope nobody has any bright ideas about dual switching between V2 on 2.1 and V1 on 2.0. No...


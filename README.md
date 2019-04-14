# FiveFingerSilver: Fix answer button graph

## About:
This addon is used to fix the answer button graph label and stats for ReMemorize and Plan9/0. But since this addon conflicts with another addon and that one is not yet available for 2.1, I went ahead and added those ideas into this addon.

<img src="https://github.com/lovac42/FiveFingerSilver/blob/master/screenshots/graphs.png?raw=true">

## Credits:
Relearn Stats 1.0 C 2014-2015 by Teemu Pudas https://ankiweb.net/shared/info/1999018922



## V1-V2 Logging Inconsistencies:
### Update: This problem was fixed in the recent stable release v2.1.11 which auto updates the old button mappings in the review logs.

For learning cards, in V1 there are 3 buttons, the good button is mapped to ease2. But in V2, hard button repeats, we have 4 grading buttons, and the good button is mapped to ease3. When generating stats, the good button on V1 is aligned to the hard button on V2. The easy btn on V1 is aligned to the good btn on V2.

(Still with me?)

<b>To see what I mean,</b> start out with V1 on a new profile, grade 3 cards as again, good, and easy. Look at the stats. Then switch over to V2, grade 4 cards as again, hard, good, and easy. Look at the stats again. The good btn count (V1) will be merged with the hard btn count (V2) and the same for the other grades.

Fixing this was not the intention of making this addon, just be aware that data from V1 and V2 will skew the stats for learning cards and the old stats from V1 will interfere with the new stats after switching to V2 for at least a month before it tapers off. To be clear, this isn't to say that V2 is incorrect, it's just annoying to switch over like switching from QWERTY to DVORAK. Perhapse someone could write an addon to convert the review log to the new format? We could call it "Humpty Dumpty: Used Only Once".


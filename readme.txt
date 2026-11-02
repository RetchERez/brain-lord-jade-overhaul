Brain Lord - Jade Overhaul
Version 1.0

The original game, with four additional fairy companions

All 13 original individual fairies keep their original stats, prices and sources
Rapid, Ward, Frost and Poison bring the total to 17
There is no added shop or shopkeeper
The opening treasure gives Crimson alone, just as in the original game
Life stays with its original Silver Plaque exchange

INSTALL

Use brain_lord_jade_overhaul_v10.bps

- Apply the BPS patch once to an unmodified headerless Brain Lord USA ROM
- Use a separate filename for your patched game and its saves
- Start a new game to make all four new treasures available
- Keep saves from earlier 12-fairy builds and emulator save states separate

Original ROM size: 1,572,864 bytes
Original ROM CRC32: AC443D87
Original ROM SHA-256:
f4666355e7fea434843dc6d5119673bd6c23e69b884aac0b382ff036997e52b5

Patched ROM SHA-256:
b87a74e86bcbe4e206a5863a90318247da8c023c8ab4c68aca19d7c70844018d

The ROM is not expanded
This player archive contains only the BPS patch and this readme

WHAT CHANGES

- Four new fairies with their own equipped sprites and inventory Jade icons
- Four existing optional treasure rewards now hold the new Jades
- Each collected blue sphere gives 50 EXP to each equipped eligible fairy
- The naming question identifies the Jade whose fairy you are naming

Original shops, starting money, equipment, keys, puzzles and story gates stay native
Enemy placement, blue-sphere drops and original fairy training thresholds stay native
No extra random sphere roll or extra one-time sphere reward is added
You can still equip at most two fairies
Enemies keep their normal colors, including enemies affected by Poison

ALL 17 FAIRY JADE LOCATIONS

The names below are the default fairy names
You can rename each fairy when you receive its Jade
Original merchant appearances and stock conditions follow the original story

- Life Jade - Ason - The original Silver Plaque exchange in Toronto
- Crimson Jade - Ifrie - The original treasure in the house north of Arcs
- Foundation Jade - Golem - Its original secret treasure in the Tower of Light
- Power Jade - Sarah - The original fairy merchants in Arcs and Toronto
- Lightning Jade - Pilulu - The original fairy merchants in Arcs and Toronto
- Anger Jade - Yak - The original fairy merchants in Arcs and Toronto
- Water Jade - Domul - The original fairy merchants in Arcs and Toronto
- Deceased Jade - Kass - The original fairy merchants in Arcs and Toronto
- Light Jade - Pazun - Its original treasure in Abell
- Second Lightning Jade - Jima - The original Toronto fairy merchant
- Second Anger Jade - Griffin - The original Toronto fairy merchant
- Second Water Jade - Priss - The original Toronto fairy merchant
- Second Crimson Jade - Gala - The original Toronto fairy merchant
- Rapid Jade - Zeph - The optional upper Tower of Light chest that originally held a Warp Gate
- Ward Jade - Aegis - The optional four-chest side chamber in Abell, replacing its Apple
- Poison Jade - Briar - The optional chest in the fourth regular Abell map, replacing a Warp Gate
- Frost Jade - Rime - The optional chest in the first regular Ice Castle map, replacing a Warp Gate

Ward's Abell chamber is reached through the existing descent from the third map
Poison's chest can be opened from above while facing down
The other rewards in these rooms are unchanged
Keep the four new Jades, since each comes from one treasure chest
Opening a chest with a full bag does not consume its reward

The original second Lightning, Anger, Water and Crimson fairies are separate companions
They retain their original powers and separate names, levels and EXP
They are not replaced by the new fairies

THE FOUR NEW FAIRIES

Rapid - Purple speed-cut Jade and small purple shots
Starts near Crimson's pace and becomes faster through training
Its level 1 cooldown is 150 to 181 game ticks
Its level 19 cooldown is 64 to 95 game ticks
Shots use half its raw fairy power, rounded down with a minimum of one
It starts with two-damage shots
Purple accents may briefly fall back to teal if a scene has no spare sprite palette

Ward - Gold shield-cut Jade and a protective fairy
Blocks one valid enemy contact hit when charged, then recharges
Starts uncharged and takes about 10 seconds to recharge at level 1
Recharge improves to about 5 seconds at level 19
Entering a room or summoning again starts a fresh recharge
A block plays the native shield-deflection sound and gives a brief escape grace
Ward does not attack and does not stop ordinary ranged shots or every hazard

Frost - Cyan ice-crystal Jade and an icy projectile
Uses Crimson's native cooldown range of 128 to 255 game ticks
Shots use half its raw fairy power, rounded up
It starts with two-damage shots
Slows one ordinary enemy to half movement speed
Slow lasts 5 seconds at level 1 and improves to an 8-second cap
A small cyan aura marks the slow
Bosses and boss parts are not slowed
Enemy attack timers and AI keep running

Poison - Green thorn-cut Jade, a thorn-winged fairy and small thorn shots
The thorn applies poison to one ordinary enemy and has no impact damage
A fresh application lasts 6 active seconds and can deliver three ticks
Each tick comes 2 active seconds apart
Tick damage is 2 at levels 1 through 3, then rises by one every three levels
Tick damage reaches its cap of 7 at level 16 and stays capped through level 19
Repeated hits refresh the duration without stacking damage or restarting the tick clock
Poisoning another enemy replaces the previous target
Ticks do not stagger the enemy and respect its normal invulnerability window
Each nonlethal tick uses the normal hit sound and brief damage blink or flash
Lethal ticks use the enemy's normal death sequence
Its short hit protection matches Rapid and Frost, without adding knockback
Bosses and boss parts are immune
Recall and room changes clear the effect
Poison does not recolor enemies

SHARED TRAINING

- Either equipped fairy can collect the blue sphere
- Each eligible equipped fairy gets 50 EXP, never 100 from one sphere
- A single equipped fairy gets 50 EXP
- Reserve fairies do not gain EXP
- A capped partner does not increase the other fairy's award
- The native level 19 cap remains in place

Most fairies need four spheres per level
The original Crimson fairy Ifrie and Deceased fairy Kass need three
Light fairy Pazun needs two
The second Crimson fairy Gala retains its original four-sphere threshold
Both companions can level from the same pickups
Two simultaneous level gains share one notification
Deceased starts at its original level 1 and needs training before its first revival

SAVES

The four new fairy records are stored inside each native save block
Both native save slots, their backups, copy and erase are supported
A vanilla battery save can load, but already opened replacement chests cannot grant new Jades
A new game is recommended for the complete experience
Saves from the earlier 12-fairy build are not compatible with this roster

FOCUSED TESTING

- Begin a new game and check that the first Jade treasure gives Crimson alone
- Check the Jade name in its naming question
- Find a new Jade at one of the four locations above and name its fairy
- Equip two different fairies and collect a blue sphere to check shared training
- For Ward, wait for a full recharge and compare one blocked contact with a hit during recharge
- For Frost, compare an ordinary enemy's movement and then confirm a boss is unaffected
- For Poison, use a durable ordinary enemy and allow time for its separate damage ticks
- Save normally, restart the emulator and use Continue to check both equipped fairies

VERIFICATION

Checked with Linux headless emulation, native menus and battery saves, source comparisons
and seeded mathematical simulations of all 17 fairies and 136 legal pairs
Both slot orders are covered by native combat and room-reload tests
No full campaign playthrough was performed
Mathematical scenarios model declared player actions and encounter geometry, not every room's AI
Debug images and private checkpoints are not included

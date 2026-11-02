# Release verification

| Result | Coverage |
| --- | --- |
| 26 native groups | Storage, new game, names, treasures, combat, feedback, EXP, menus, icons, saves, rooms and story-data invariants |
| 66 unit tests | Profile, patch format, build guards and supporting tools |
| 9 model regressions | Original stats, Poison clocks, collision phases, body-contact exclusion and source binding |
| 136 legal pairs | 2,448 canonical scenario/level configurations, plus reverse slot orders |
| 272 native slot orders | Combat, recall and native room reload |
| 1,128 EXP cases | Either collector, both slots, caps, recalled/duplicate status and simultaneous level gains |
| 16 native feedback cases | Crimson, Rapid, Frost and Poison in both slots with exclusive/shared palettes |
| 10 live phase cases | Actual target and owner callbacks, overlapping hits and exact recovery boundaries |

The numerical grid uses six declared encounter scenarios at levels 1, 7 and 19,
with 160 seeded trials per canonical configuration and 64 per reverse order.
It also includes 306 solo configurations and 1,404 original-pair comparisons
whose metric arrays are identical between vanilla and this profile.
These are conditional encounter models, not an emulation of every native room AI.

The native room-entry comparison completed 745 of 749 entries in both vanilla
and the patched game, with the same four incomplete fixtures in each. This is
not a claim that all story prerequisites were traversed. No full campaign
playthrough or real-console certification was performed.

The BPS was reapplied with both the project decoder and an independent decoder,
producing the exact target and a valid SNES checksum. The ROM is not expanded.

- Target SHA-256: `b87a74e86bcbe4e206a5863a90318247da8c023c8ab4c68aca19d7c70844018d`
- Target CRC32: `599D0B43`
- ZIP SHA-256: `2a43d0c4dc1d73148f7febf75a2dda5cef3f46e1b4ff2441f3ff2eca4089d1cb`

The public GIFs come from the final target, using prepared encounters. Poison's
capture contains native damage flashes in the actual rendered pixels and no
player HP changes. Screenshots are unscaled 256×224 RGB frames. Debug images,
private checkpoints, saves and ROMs are excluded from this repository.

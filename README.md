# field_planner
```
usage: Generate draw tools objects.

        Anchor arguments needs to be comma-separated and quoted. I.E. -a "59.866552,17.666234"

        Portal list file must contain comma-separated lines.


       [-h] -a1 ANCHOR_1 [ANCHOR_1 ...] [-a2 ANCHOR_2 [ANCHOR_2 ...]] -l LIST
       [LIST ...]

optional arguments:
  -h, --help            show this help message and exit
  -a1 ANCHOR_1 [ANCHOR_1 ...], --anchor_1 ANCHOR_1 [ANCHOR_1 ...]
                        Coordinates to anchor. Must be comma-separated
  -a2 ANCHOR_2 [ANCHOR_2 ...], --anchor_2 ANCHOR_2 [ANCHOR_2 ...]
                        Coordinates to first anchor. must be comma-separated
  -l LIST [LIST ...], --list LIST [LIST ...]
                        Path to file with comma-separated coordinates list.
```
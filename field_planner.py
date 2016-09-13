#!/usr/bin/env python
import argparse
import sys

TEMPLATE_FIELD = "{\"type\":\"polyline\",\"latLngs\":[{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s}],\"color\":\"#a24ac3\"}"
TEMPLATE_LINK = "{\"type\":\"polyline\",\"latLngs\":[{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s}],\"color\":\"#a24ac3\"}"


try:
    parser = argparse.ArgumentParser(
        """Generate draw tools objects.


        Anchor arguments needs to be comma-seperated and quoted. I.E. -a "59.866552,17.666234"

        Portal list file must contain comma-seperated lines.

        """)

    parser.add_argument('-a1', '--anchor_1', nargs='+', help="Coordinates to anchor. Must be comma-seperated", required=True)
    parser.add_argument('-a2', '--anchor_2', nargs='+', help="Coordinates to first anchor. must be comma-seperated")
    parser.add_argument('-l', '--list', nargs='+', help="Path to file with comma-separated coordinates list.", required=True)
    args = parser.parse_args()
except Exception:
    sys.exit(1)


anchor_1 = args.anchor_1[0].split(",")
if not args.anchor_2:
    anchor_2 = False
else:
    anchor_2 = args.anchor_2[0].split(",")
list = args.list[0]




class FieldDrawer:

    def __init__(self, anchor_1, anchor_2, portal_list):
        self.portal_list = portal_list

    def parse_portal_list(self):
        with open(self.portal_list, "r") as portal_list:
            portal_list = portal_list.readlines()
            list_cnt = 0
            list_len = len(portal_list)

            print("["),
            for row in portal_list:

                if not anchor_2:
                    print(TEMPLATE_LINK % (anchor_1[0],
                                           anchor_1[1],
                                           row.split(",")[-2].strip("\n"),
                                           row.split(",")[-1].strip("\n")
                                           )),
                else:
                    print(TEMPLATE_FIELD % (anchor_1[0],
                                            anchor_1[1],
                                            row.split(",")[-2].strip("\n"),
                                            row.split(",")[-1].strip("\n"),
                                            anchor_2[0],
                                            anchor_2[1],
                                            anchor_1[0],
                                            anchor_1[1]
                                           )),
                if list_cnt != list_len -1:
                    list_cnt += 1
                    print(",")
        print("]")

    def generate(self):
        self.parse_portal_list()


if __name__ == "__main__":

    fd = FieldDrawer(anchor_1, anchor_2, list)

    fd.generate()


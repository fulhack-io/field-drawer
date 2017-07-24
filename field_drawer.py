#!/usr/bin/env python
import argparse
import sys
import simplejson as json

TEMPLATE_FIELD = "{\"type\":\"polyline\",\"latLngs\":[{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s}],\"color\":\"#a24ac3\"}"
TEMPLATE_LINK = "{\"type\":\"polyline\",\"latLngs\":[{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s}],\"color\":\"#a24ac3\"}"


try:
    parser = argparse.ArgumentParser(
        """Generate draw tools objects.


        Anchor arguments needs to be comma-separated and quoted. I.E. -a "59.866552,17.666234"

        Portal list file must contain comma-separated lines.

        """)

    parser.add_argument('-a1', '--anchor_1', nargs='+', help="Coordinates to anchor. Must be comma-separated", required=True)
    parser.add_argument('-a2', '--anchor_2', nargs='+', help="Coordinates to first anchor. must be comma-separated")
    parser.add_argument('-l', '--list', nargs='+', help="Path to file with comma-separated coordinates list.", required=False)
    parser.add_argument('-t', '--type', nargs='+', choices=['csv', 'json'])
    args = parser.parse_args()
except Exception as e:
    print(e)
    sys.exit(1)


anchor_1 = args.anchor_1[0].split(",")
if not args.anchor_2:
    anchor_2 = False
else:
    anchor_2 = args.anchor_2[0].split(",")
portal_list_f = args.list[0]
input_type = args.type[0]


class FieldDrawer:

    def __init__(self, a1, a2, portal_list_f):
        self.portal_list_f = portal_list_f
        self.anchor_1 = a1
        self.anchor_2 = a2

    def parse_portal_list_json(self):
        try:
            with open(self.portal_list_f) as pl:
                portal_list = json.loads(pl.read())
        except Exception as e:
            raise e

        list_cnt = 0
        list_len = len(portal_list)

        print("[", end=''),
        for a in portal_list:
            if a["type"] != "marker":
                print("Only type marker is supported.")
                sys.exit(1)
            if not anchor_2:
                print(TEMPLATE_LINK % (self.anchor_1[0],
                                       self.anchor_1[1],
                                       a["latLng"]["lat"],
                                       a["latLng"]["lng"],
                                       )),
            else:
                print(TEMPLATE_FIELD % (self.anchor_1[0],
                                        self.anchor_1[1],
                                        a["latLng"]["lat"],
                                        a["latLng"]["lng"],
                                        self.anchor_2[0],
                                        self.anchor_2[1],
                                        self.anchor_1[0],
                                        self.anchor_1[1]
                                        ), end=''),
            if list_cnt != list_len - 1:
                list_cnt += 1
                print(",")

        print("]")

    def parse_portal_list_csv(self):
        try:
            with open(self.portal_list_f) as pl:
                portal_list = pl.readlines()
        except Exception as e:
            print("Unable to read portal list.")
            print(e)

        list_cnt = 0
        list_len = len(portal_list)

        print("[", end=''),
        for row in portal_list:
            if not anchor_2:
                print(TEMPLATE_LINK % (self.anchor_1[0],
                                       self.anchor_1[1],
                                       row.split(",")[-2].strip("\n"),
                                       row.split(",")[-1].strip("\n")
                                       )),
            else:
                print(TEMPLATE_FIELD % (self.anchor_1[0],
                                        self.anchor_1[1],
                                        row.split(",")[-2].strip("\n"),
                                        row.split(",")[-1].strip("\n"),
                                        self.anchor_2[0],
                                        self.anchor_2[1],
                                        self.anchor_1[0],
                                        self.anchor_1[1]
                                        )),
            if list_cnt != list_len - 1:
                list_cnt += 1
                print(",")

        print("]", end='')

    def generate(self):
        if input_type == 'csv':
            self.parse_portal_list_csv()
        elif input_type == 'json':
            self.parse_portal_list_json()


if __name__ == "__main__":

    fd = FieldDrawer(anchor_1, anchor_2, portal_list_f)
    fd.generate()


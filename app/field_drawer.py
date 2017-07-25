#!/usr/bin/env python
import argparse
import sys
import simplejson as json

TEMPLATE_FIELD = "{\"type\":\"polyline\",\"latLngs\":[{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s},{\"lat\":%s,\"lng\":%s}],\"color\":\"#a24ac3\"}"

class FieldDrawer:

    def __init__(self, a1, a2, portal_list_f):
        self.portal_list_f = portal_list_f
        self.anchor_1 = a1
        self.anchor_2 = a2

    def parse_portal_list_json(self):
        try:
            portal_list = json.loads(self.portal_list_f)
        except Exception as e:
            return e

        list_cnt = 0
        list_len = len(portal_list)

        res = "["
        for a in portal_list:
            if a["type"] != "marker":
                return "Unable to parse portal list. Ensure type is only marker."

            try:
                res += TEMPLATE_FIELD % (self.anchor_1.split(',')[0],
                                        self.anchor_1.split(',')[1],
                                        a["latLng"]["lat"],
                                        a["latLng"]["lng"],
                                        self.anchor_2.split(',')[0],
                                        self.anchor_2.split(',')[1],
                                        self.anchor_1.split(',')[0],
                                        self.anchor_1.split(',')[1]
                                        )
            except Exception as e:
                return "Unable to generate, verify that the following key exist: {}".format(e)
            if list_cnt != list_len - 1:
                list_cnt += 1
                res += ",\n"
        res += "]"

        return res

    def generate(self):
        return self.parse_portal_list_json()


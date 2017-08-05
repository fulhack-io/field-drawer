#!/usr/bin/env python
import simplejson as json


class FieldDrawer:

    def __init__(self, a1, a2, portal_list_f, include_markers, draw_color):
        self.portal_list_f = portal_list_f
        self.anchor_1_lat = a1.split(',')[0]
        self.anchor_1_lng = a1.split(',')[1]
        self.anchor_2_lat = a2.split(',')[0]
        self.anchor_2_lng = a2.split(',')[1]
        self.include_markers = include_markers
        self.color = draw_color

    def parse_portal_list_json(self):
        try:
            portal_list = json.loads(self.portal_list_f)
        except Exception as e:
            return e

        # Draw baseline
        res = '[{{"type":"polyline","latLngs":[{{"lat":{},"lng":{}}},{{"lat":{},"lng":{}}}],"color":"#{}"}},\n'.format(self.anchor_1_lat,
                                                                                                                       self.anchor_1_lng,
                                                                                                                       self.anchor_2_lat,
                                                                                                                       self.anchor_2_lng,
                                                                                                                       self.color)
        # Draw field
        for portal in portal_list:
            print(portal)
            if portal["type"] == "marker":
                try:
                    res += '{{"type":"polyline","latLngs":[{{"lat":{},"lng":{}}},{{"lat":{},"lng":{}}},{{"lat":{},"lng":{}}}],"color":"#{}"}},\n'.format(self.anchor_1_lat,
                                                                                                                                                         self.anchor_1_lng,
                                                                                                                                                         portal["latLng"]["lat"],
                                                                                                                                                         portal["latLng"]["lng"],
                                                                                                                                                         self.anchor_2_lat,
                                                                                                                                                         self.anchor_2_lng,
                                                                                                                                                         self.color)
                    # Draw markers
                    if self.include_markers:
                        res += '{{"type":"marker","latLng":{{"lat":{},"lng":{}}},"color":"#{}"}},\n'.format(portal["latLng"]["lat"],
                                                                                                            portal["latLng"]["lng"],
                                                                                                            self.color)

                except Exception as e:
                    return "Unable to generate, verify that the following key exist: {}".format(e)

        res += "]"
        res = res.replace(',\n]', ']').replace(',]', ']')
        return res

    def generate(self):
        return self.parse_portal_list_json()

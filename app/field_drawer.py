#!/usr/bin/env python
import simplejson as json
import ast


class FieldDrawer:

    def __init__(self, a1, a2, draw_tools_export, include_markers, generate_markers, include_all_polylines, polyline_color, marker_color):
        self.portal_list_f = draw_tools_export
        self.anchor_1_lat = a1.split(',')[0]
        self.anchor_1_lng = a1.split(',')[1]
        self.anchor_2_lat = a2.split(',')[0]
        self.anchor_2_lng = a2.split(',')[1]
        self.include_markers = include_markers
        self.generate_markers = generate_markers
        self.include_all_polylines = include_all_polylines
        self.color = polyline_color
        self.polyline_color = polyline_color
        self.marker_color = marker_color

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
                                                                                                                       self.polyline_color)
        # Draw field
        for portal in portal_list:
            if portal["type"] == "marker":
                try:
                    res += '{{"type":"polyline","latLngs":[{{"lat":{},"lng":{}}},{{"lat":{},"lng":{}}},{{"lat":{},"lng":{}}}],"color":"#{}"}},\n'.format(self.anchor_1_lat,
                                                                                                                                                         self.anchor_1_lng,
                                                                                                                                                         portal["latLng"]["lat"],
                                                                                                                                                         portal["latLng"]["lng"],
                                                                                                                                                         self.anchor_2_lat,
                                                                                                                                                         self.anchor_2_lng,
                                                                                                                                                         self.polyline_color)
                    # Draw markers
                    if self.include_markers:
                        res += '{{"type":"marker","latLng":{{"lat":{},"lng":{}}},"color":"#{}"}},\n'.format(portal["latLng"]["lat"],
                                                                                                            portal["latLng"]["lng"],
                                                                                                            self.marker_color)

                except Exception as e:
                    return "Unable to generate, verify that the following key exist: {}".format(e)

            elif portal["type"] == "polyline":
                if self.include_all_polylines:
                    res += str(portal).replace(' ', '').replace('\'', '"') + ',\n'

                if self.generate_markers and len(portal["latLngs"]) == 3:
                    res += '{{"type":"marker","latLng":{{"lat":{},"lng":{}}},"color":"#{}"}},\n'.format(portal["latLngs"][1]["lat"],
                                                                                                        portal["latLngs"][1]["lng"],
                                                                                                        self.marker_color)

        res += "]"
        res = res.replace(',\n]', ']').replace(',]', ']')
        res = ast.literal_eval(res)
        new_res = []
        for item in res:
            if item not in new_res:
                new_res.append(item)

        return str(new_res).replace(' ', '').replace('\'', '"')

    def generate(self):
        return self.parse_portal_list_json()


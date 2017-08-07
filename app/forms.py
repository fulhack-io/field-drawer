from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Optional

class DrawForm(FlaskForm):
    anchor1 = StringField('Anchor 1', validators=[Optional()])
    anchor2 = StringField('Anchor 2', validators=[Optional()])
    draw_tools_export = TextAreaField(u'Draw Tools export. (Can contain markers and polyline)',
                                      validators=[DataRequired()],
                                      render_kw={"rows": 10, "cols": 100}
                                      )
    include_markers = BooleanField(u'Include Markers from export', validators=[Optional()])
    generate_markers= BooleanField(u'Generate markers from export (Adds a marker parsed from the second index of latLngs)', validators=[Optional()])
    include_all_polylines = BooleanField(u'Include all polylines from export', validators=[Optional()])
    parse_anchors = BooleanField(u'Attempt to parse anchors from export (Requires first polyline to be the baseline)')
    polyline_color = StringField('Polyline color')
    marker_color = StringField('Marker color')

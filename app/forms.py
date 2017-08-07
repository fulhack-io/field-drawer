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
    include_markers = BooleanField(u'Include Markers from export.', validators=[Optional()])
    generate_markers= BooleanField(u'Generate missing markers from export.', validators=[Optional()])
    include_all_polylines = BooleanField(u'Include all polyliens from export.', validators=[Optional()])
    parse_anchors = BooleanField(u'Parse anchors from export (Requires first polyline to be the baseline.)')
    draw_color = StringField('Draw color')

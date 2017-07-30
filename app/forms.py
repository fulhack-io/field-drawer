from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Optional

class DrawForm(FlaskForm):
    anchor1 = StringField('Anchor 1', validators=[Optional()])
    anchor2 = StringField('Anchor 2', validators=[Optional()])
    portal_list = TextAreaField(u'Portal list',
                                validators=[DataRequired()],
                                render_kw={"rows": 10, "cols": 100}
                                )
    include_markers = BooleanField(u'Include Markers', validators=[Optional()])
    parse_anchors = BooleanField(u'Parse anchors from portal list (Requires first polyline to be baseline)')
    draw_color = StringField('Draw color')

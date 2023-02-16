from wtforms import (
    Form,
    StringField,
    IntegerField,
    DateField,
    SelectField,
    validators,
)


class TimelineForm(Form):
    startDate = DateField(
        "startDate",
        format="%Y-%m-%d",
        validators=[validators.DataRequired()]
    )
    endDate = DateField(
        "endDate",
        format="%Y-%m-%d",
        validators=[validators.DataRequired()]
    )
    Type = SelectField(
        "Type",
        choices=[("cumulative", "Cumulative"), ("usual", "Usual")],
        validators=[validators.DataRequired()],
    )
    Grouping = SelectField(
        "Grouping",
        choices=[
            ("weekly", "Weekly"),
            ("bi-weekly", "Bi-Weekly"),
            ("monthly", "Monthly"),
        ],
        validators=[validators.DataRequired()],
    )
    stars = IntegerField(validators=[validators.Optional()])
    asin = StringField(validators=[validators.Optional()])
    brand = StringField(validators=[validators.Optional()])
    source = StringField(validators=[validators.Optional()])

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        if self.startDate.data > self.endDate.data:
            self.startDate.errors.append("Start date must be before end date")
            return False

        return True

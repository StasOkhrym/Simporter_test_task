from wtforms import (
    Form,
    StringField,
    DateField,
    SelectField,
    FieldList,
    FormField,
    validators,
)


class FilterForm(Form):
    attr = StringField("Attribute")
    value = StringField("Value")


class TimelineForm(Form):
    start_date = DateField(
        "Start Date",
        format="%Y-%m-%d",
        validators=[validators.DataRequired()]
    )
    end_date = DateField(
        "End Date",
        format="%Y-%m-%d",
        validators=[validators.DataRequired()]
    )
    type = SelectField(
        "Type",
        choices=[("cumulative", "Cumulative"), ("usual", "Usual")],
        validators=[validators.DataRequired()],
    )
    grouping = SelectField(
        "Grouping",
        choices=[
            ("weekly", "Weekly"),
            ("bi-weekly", "Bi-Weekly"),
            ("monthly", "Monthly"),
        ],
        validators=[validators.DataRequired()],
    )
    filters = FieldList(FormField(FilterForm))

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        if self.start_date.data > self.end_date.data:
            self.start_date.errors.append("Start date must be before end date")
            return False

        return True

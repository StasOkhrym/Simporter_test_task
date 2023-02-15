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
    VALID_COLUMNS = ("asin", "id", "brand", "source", "stars")

    attr = StringField("Attribute")
    value = StringField("Value")

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        if self.attr.data not in self.VALID_COLUMNS:
            self.attr.errors.append(f"Invalid attribute {self.attr.data}")
            return False

        return True


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
    # filters = FieldList(FormField(FilterForm))

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        if self.startDate.data > self.endDate.data:
            self.startDate.errors.append("Start date must be before end date")
            return False

        return True

from wtforms import (
    Form,
    StringField,
    DateField,
    SelectField,
    FieldList,
    FormField,
)


class FilterForm(Form):
    attr = StringField("Attribute")
    value = StringField("Value")


class TimelineForm(Form):
    start_date = DateField("Start Date", format="%Y-%m-%d")
    end_date = DateField("End Date", format="%Y-%m-%d")
    type = SelectField(
        "Type", choices=[("cumulative", "Cumulative"), ("usual", "Usual")]
    )
    grouping = SelectField(
        "Grouping",
        choices=[
            ("weekly", "Weekly"),
            ("bi-weekly", "Bi-Weekly"),
            ("monthly", "Monthly"),
        ],
    )
    filters = FieldList(FormField(FilterForm))

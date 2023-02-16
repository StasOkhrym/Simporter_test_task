from flask import Blueprint, request, jsonify
from flask import current_app

from api.utils import retrieve_possible_values, retrieve_from_db
from api.forms import TimelineForm

api = Blueprint("api", __name__)


@api.route("/info", methods=["GET"])
def get_info():
    possible_values = retrieve_possible_values(
        database=current_app.config["CONNECTION_STRING"],
        table_name=current_app.config["TABLE_NAME"]
    )

    return jsonify({"info": possible_values})


@api.route("/timeline", methods=["GET"])
def get_timeline():
    form = TimelineForm(request.args)
    if form.validate():
        data = retrieve_from_db(
            database=current_app.config["CONNECTION_STRING"],
            table_name=current_app.config["TABLE_NAME"],
            parameters=form.data,
        )
        return jsonify({"timeline": data})
    else:
        return jsonify({"errors": form.errors})

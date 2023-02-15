from flask import Blueprint, request, jsonify

from api.data_retriever import retrieve_from_df
from api.forms import TimelineForm

api = Blueprint('api', __name__)


@api.route("/info",  methods=['GET'])
def get_info():
    return "Success"


@api.route("/timeline",  methods=['GET'])
def get_timeline():
    form = TimelineForm(request.args)
    if form.validate():
        data = retrieve_from_df(form.data)
        return jsonify({"timeline": data})
    else:
        return {"errors": form.errors}

from flask import request

import tools

bp = tools.MyBlueprint("cons", "wc_construction", host="weirdcease.com")

@bp.route("/")
@bp.route("/<anything>")
def home(*args):
    return bp.render("construction.html")
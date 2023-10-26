from flask import request

import tools

bp = tools.MyBlueprint("cons", "wc_construction", host="weirdcease.com")

@bp.route("/<anything>")
def home(anything):
    return bp.render("construction.html")
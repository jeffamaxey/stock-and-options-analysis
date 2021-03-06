from flask import Blueprint, render_template
from flask_login import current_user, login_required

fundamental_analysis_bp = Blueprint("fundamental", __name__)


@fundamental_analysis_bp.route("/fundamental-analysis")
@login_required
def fundamental_analysis():
    return render_template("fundamental-analysis-page.html", user=current_user)


@fundamental_analysis_bp.route("/fundamental-analysis/result")
@login_required
def fundamental_analysis_result():
    return render_template("fundamental-analysis-page2.html", user=current_user)



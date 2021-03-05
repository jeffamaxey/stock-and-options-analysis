from flask import Blueprint, render_template
from flask_login import current_user, login_required

technical_analysis_bp = Blueprint("technical", __name__)


@technical_analysis_bp.route("/technical-analysis")
@login_required
def technical_analysis():
    return render_template("technical-analysis-page.html", user=current_user)


@technical_analysis_bp.route("/technical-analysis/result")
@login_required
def technical_analysis_result():
    return render_template("technical-analysis-page2.html", user=current_user)

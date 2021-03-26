from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

technical_analysis_bp = Blueprint("technical", __name__)


@technical_analysis_bp.route("/technical-analysis", methods=["GET", "POST"])
@login_required
def technical_analysis():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-15")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-115")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-125")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-135")

        data_source = request.form.get("data-source15")
        if data_source is None:
            data_source = request.form.get("data-source115")
        if data_source is None:
            data_source = request.form.get("option-style129")
        if data_source is None:
            data_source = request.form.get("data-source125")

    return render_template("technical-analysis-page.html", user=current_user)


@technical_analysis_bp.route("/technical-analysis/result", methods=["GET", "POST"])
@login_required
def technical_analysis_result():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-19")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-119")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-129")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-139")

        data_source = request.form.get("data-source19")
        if data_source is None:
            data_source = request.form.get("data-source119")
        if data_source is None:
            data_source = request.form.get("option-style139")
        if data_source is None:
            data_source = request.form.get("data-source129")

    return render_template("technical-analysis-page2.html", user=current_user)


@technical_analysis_bp.route("/technical-analysis/export")
@login_required
def technical_analysis_export():
    return redirect(url_for("technical.technical_analysis"))

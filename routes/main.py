from flask import Blueprint, render_template, request

# Import calculator logic
from calculators.emi import calculate_emi
from calculators.gst import calculate_gst
from calculators.percentage import calculate_percentage
from calculators.age import calculate_age
from calculators.bmi import calculate_bmi
from calculators.sip import calculate_sip
from calculators.cgpa import calculate_cgpa


main = Blueprint("main", __name__)


# 🏠 HOME
@main.route("/")
def home():
    return render_template("home.html")


# 💰 EMI
@main.route("/emi-calculator", methods=["GET", "POST"])
def emi():
    result = interest = principal = error = None

    if request.method == "POST":
        result, interest, principal, error = calculate_emi(request.form)

    return render_template("emi.html",
                           result=result,
                           interest=interest,
                           principal=principal,
                           error=error)


# 🧾 GST
@main.route("/gst-calculator", methods=["GET", "POST"])
def gst():
    gst_amount = total = amount = error = None

    if request.method == "POST":
        gst_amount, total, amount, error = calculate_gst(request.form)

    return render_template("gst.html",
                           gst_amount=gst_amount,
                           total=total,
                           amount=amount,
                           error=error)


# 📊 PERCENTAGE
@main.route("/percentage-calculator", methods=["GET", "POST"])
def percentage():
    result = error = None

    if request.method == "POST":
        result, error = calculate_percentage(request.form)

    return render_template("percentage.html",
                           result=result,
                           error=error)


# 🎂 AGE
@main.route("/age-calculator", methods=["GET", "POST"])
def age():
    years = months = days = None

    if request.method == "POST":
        years, months, days = calculate_age(request.form)

    return render_template("age.html",
                           years=years,
                           months=months,
                           days=days)


# 🏋️ BMI
@main.route("/bmi-calculator", methods=["GET", "POST"])
def bmi():
    bmi_value = category = None

    if request.method == "POST":
        bmi_value, category = calculate_bmi(request.form)

    return render_template("bmi.html",
                           bmi=bmi_value,
                           category=category)
@main.route("/sip-calculator", methods=["GET", "POST"])
def sip():
    result = None
    error = None

    if request.method == "POST":
        result, error = calculate_sip(request.form)

    return render_template("sip.html",
                           result=result,
                           error=error)
@main.route("/cgpa-calculator", methods=["GET", "POST"])
def cgpa():
    result = None
    error = None

    if request.method == "POST":
        result, error = calculate_cgpa(request.form)

    return render_template("cgpa.html",
                           result=result,
                           error=error)
@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/privacy")
def privacy():
    return render_template("privacy.html")

@main.route("/terms")
def terms():
    return render_template("terms.html")
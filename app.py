from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)


# 🏠 HOME
@app.route("/")
def home():
    return render_template("home.html")


# 💰 EMI CALCULATOR
@app.route("/emi-calculator", methods=["GET", "POST"])
def emi():
    result = None
    interest = None
    principal_value = None
    error = None

    if request.method == "POST":
        try:
            principal = float(request.form.get("principal"))
            rate = float(request.form.get("rate"))
            time = int(request.form.get("time"))

            if principal <= 0:
                error = "Loan amount must be greater than 0"
            elif rate < 0 or rate > 100:
                error = "Interest rate must be between 0 and 100"
            elif time <= 0:
                error = "Time must be greater than 0"
            else:
                r = rate / (12 * 100)

                if rate == 0:
                    emi_value = principal / time
                else:
                    emi_value = (principal * r * (1 + r)**time) / ((1 + r)**time - 1)

                result = round(emi_value, 2)

                total_payment = result * time
                interest = round(total_payment - principal, 2)
                principal_value = principal

        except:
            error = "Invalid input"

    return render_template(
        "emi.html",
        result=result,
        interest=interest,
        principal=principal_value,
        error=error
    )


# 🧾 GST CALCULATOR
@app.route("/gst-calculator", methods=["GET", "POST"])
def gst():
    gst_amount = None
    total = None
    amount = None
    error = None

    if request.method == "POST":
        try:
            amount = float(request.form.get("amount"))
            gst_rate = float(request.form.get("gst"))

            if amount < 0:
                error = "Amount cannot be negative"
            elif gst_rate < 0 or gst_rate > 100:
                error = "GST must be between 0 and 100"
            else:
                gst_amount = round((amount * gst_rate) / 100, 2)
                total = round(amount + gst_amount, 2)

        except:
            error = "Invalid input"

    return render_template(
        "gst.html",
        gst_amount=gst_amount,
        total=total,
        amount=amount,
        error=error
    )


# 📊 PERCENTAGE CALCULATOR
@app.route("/percentage-calculator", methods=["GET", "POST"])
def percentage():
    result = None
    error = None

    if request.method == "POST":
        try:
            part = float(request.form.get("part"))
            whole = float(request.form.get("whole"))

            if whole == 0:
                error = "Cannot divide by zero"
            elif part < 0 or whole < 0:
                error = "Values cannot be negative"
            else:
                result = round((part / whole) * 100, 2)

        except:
            error = "Invalid input"

    return render_template(
        "percentage.html",
        result=result,
        error=error
    )


# 🎂 AGE CALCULATOR
@app.route("/age-calculator", methods=["GET", "POST"])
def age():
    years = None
    months = None
    days = None

    if request.method == "POST":
        try:
            dob = request.form.get("dob")
            birth_date = datetime.strptime(dob, "%Y-%m-%d")
            today = datetime.today()

            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day

            if days < 0:
                months -= 1
                days += 30

            if months < 0:
                years -= 1
                months += 12

        except:
            years = None
            months = None
            days = None

    return render_template(
        "age.html",
        years=years,
        months=months,
        days=days
    )


# 🏋️ BMI CALCULATOR
@app.route("/bmi-calculator", methods=["GET", "POST"])
def bmi():
    bmi_value = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.form.get("weight"))
            height_cm = float(request.form.get("height"))

            if height_cm <= 0:
                category = "Invalid height"
            else:
                height = height_cm / 100
                bmi_value = round(weight / (height ** 2), 2)

                if bmi_value < 18.5:
                    category = "Underweight"
                elif bmi_value < 25:
                    category = "Normal"
                elif bmi_value < 30:
                    category = "Overweight"
                else:
                    category = "Obese"

        except:
            bmi_value = None
            category = "Invalid input"

    return render_template(
        "bmi.html",
        bmi=bmi_value,
        category=category
    )


# 🚀 RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
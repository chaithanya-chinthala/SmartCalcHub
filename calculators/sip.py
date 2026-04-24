def calculate_sip(form):
    try:
        monthly = float(form.get("monthly"))
        rate = float(form.get("rate")) / 100 / 12
        years = int(form.get("years")) * 12

        if monthly <= 0 or rate <= 0 or years <= 0:
            return None, "Enter valid values"

        amount = monthly * (((1 + rate) ** years - 1) / rate) * (1 + rate)

        return round(amount, 2), None

    except:
        return None, "Invalid input"
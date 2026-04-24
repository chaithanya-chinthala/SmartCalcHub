def calculate_emi(form):
    try:
        principal = float(form.get("principal"))
        rate = float(form.get("rate"))
        time = int(form.get("time"))

        if principal <= 0:
            return None, None, None, "Invalid loan amount"

        r = rate / (12 * 100)

        if rate == 0:
            emi = principal / time
        else:
            emi = (principal * r * (1 + r)**time) / ((1 + r)**time - 1)

        emi = round(emi, 2)
        total = emi * time
        interest = round(total - principal, 2)

        return emi, interest, principal, None

    except:
        return None, None, None, "Invalid input"
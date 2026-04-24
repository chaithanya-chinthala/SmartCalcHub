def calculate_gst(form):
    try:
        amount = float(form.get("amount"))
        gst_rate = float(form.get("gst"))

        gst_amount = round((amount * gst_rate) / 100, 2)
        total = round(amount + gst_amount, 2)

        return gst_amount, total, amount, None

    except:
        return None, None, None, "Invalid input"
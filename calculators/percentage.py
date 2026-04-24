def calculate_percentage(form):
    try:
        part = float(form.get("part"))
        whole = float(form.get("whole"))

        if whole == 0:
            return None, "Cannot divide by zero"

        result = round((part / whole) * 100, 2)

        return result, None

    except:
        return None, "Invalid input"
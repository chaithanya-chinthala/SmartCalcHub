def calculate_bmi(form):
    try:
        weight = float(form.get("weight"))
        height_cm = float(form.get("height"))

        if height_cm <= 0:
            return None, "Invalid height"

        height = height_cm / 100
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return bmi, category

    except:
        return None, "Invalid input"
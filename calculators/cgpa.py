def calculate_cgpa(form):
    try:
        cgpa = float(form.get("cgpa"))

        if cgpa < 0 or cgpa > 10:
            return None, "CGPA must be between 0 and 10"

        percentage = cgpa * 9.5

        return round(percentage, 2), None

    except:
        return None, "Invalid input"
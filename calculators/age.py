from datetime import datetime

def calculate_age(form):
    try:
        dob = form.get("dob")
        birth = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()

        years = today.year - birth.year
        months = today.month - birth.month
        days = today.day - birth.day

        if days < 0:
            months -= 1
            days += 30

        if months < 0:
            years -= 1
            months += 12

        return years, months, days

    except:
        return None, None, None
def calculate_days_passed(current_day, last_watered_day):
    return current_day - last_watered_day


def check_priority(current_day, last_watered_day, water_interval):
    days_passed = calculate_days_passed(current_day, last_watered_day)

    if days_passed > water_interval:
        return "HIGH"
    elif days_passed == water_interval:
        return "MEDIUM"
    else:
        return "LOW"

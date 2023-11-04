from datetime import date, datetime

days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    current_year = today.year
    current_week = today.strftime("%U")  
    birthday_dict = {day: [] for day in days_of_week.values()}
    
    all_birthdays_past = True

    for user in users:
        name = user["name"]
        birthday = user.get("birthday").replace(year=today.year)

        if birthday:
            if birthday < today:
                birthday = birthday.replace(year=today.year + 1)
            week_number = birthday.strftime("%U")
            days_difference = (birthday - today).days

            if days_difference >= 0 and days_difference < 7:
                day_of_week = birthday.weekday()
                day_name = days_of_week.get(day_of_week)
                if day_name:
                    if days_difference > 0:  
                        all_birthdays_past = False

                if day_name in ['Saturday', 'Sunday']:
                    day_name = 'Monday'

                birthday_dict[day_name].append(name)

    if not birthday_dict['Saturday']:
        del birthday_dict['Saturday']
    if not birthday_dict['Sunday']:
        del birthday_dict['Sunday']

    # Удалить дни с пустыми списками
    empty_days = [day_name for day_name, users in birthday_dict.items() if not users]
    for day_name in empty_days:
        del birthday_dict[day_name]

    if all_birthdays_past:
        return {}
    else:   
        return birthday_dict

if __name__ == "__main__":
    users = [
        {"name": "Masha", "birthday": datetime(2023, 11, 9).date()},
        {"name": "Olya", "birthday": datetime(2023, 11, 4).date()},
        {"name": "Kolya", "birthday": datetime(2023, 11, 4).date()},
        {"name": "Sophia", "birthday": datetime(2023, 11, 5).date()},
        {"name": "Solomia", "birthday": datetime(2023, 11, 6).date()},
        {"name": "Sasha", "birthday": datetime(2023, 11, 7).date()},
        {"name": "Pasha", "birthday": datetime(2023, 11, 8).date()},
        {"name": "Oksana", "birthday": datetime(2023, 11, 15).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)

    for day_name, users in result.items():
        print(f"{day_name}: {', '.join(users)}")
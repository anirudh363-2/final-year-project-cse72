from datetime import datetime, timedelta

def get_dates_excluding_sundays(start_date, end_date):
    # Convert strings to datetime objects
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    # Generate a list of dates excluding Sundays
    dates = []
    current = start
    while current <= end:
        if current.weekday() != 6:  # 6 represents Sunday
            dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)

    print(dates)
    return dates[1:]

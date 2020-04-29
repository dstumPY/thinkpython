from datetime import date, timedelta


class Time:
    ""


def time_to_int(t1: Time) -> int:
    minutes = t1.hour * 60 + t1.minute
    seconds = minutes * 60 + t1.second
    return seconds


def int_to_time(seconds: int) -> Time:
    time = Time()
    time.hour, mod_min = divmod(seconds, 3600)
    time.minute, time.second = divmod(mod_min, 60)
    return time


def mult_time(t1: Time, mult_factor: int) -> Time:
    time_int = time_to_int(t1)
    time_int = time_int * mult_factor
    return int_to_time(time_int)


def dist_per_sec(t1: Time, dist: int) -> float:
    """Calculate distance per second for a given time instance

    Arguments:
        t1 {Time} -- time instance
        dist {int} -- distance in miles

    Returns:
        float -- average speed
    """
    time = time_to_int(t1)
    return dist / time


def get_curret_day_of_week() -> str:
    """
    Get date and curren day of week
    """    
    dt_today = date.today()
    day_of_week = {
        0: "Saturday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Sunday",
    }
    dow = day_of_week[dt_today.isoweekday()]
    print(f"Current date: {dt_today}")
    print(f"Day of week: {dow}")

def get_next_bd(bd: date) -> date:
    today = date.today()
    if (next_bd := date(today.year, bd.month, bd.day)) >= today:
        return next_bd
    else:
        return date(today.year +1, bd.month, bd.day)

def days_to_bday(bday_date: date):

    next_bd = get_next_bd(bday_date)
    age = (next_bd.year - bday_date.year) -1
    print(f"Today you are {age} years old.")

    remaining_days = (next_bd - date.today()).days
    print(f"There are {remaining_days} days remaining to your next birthday.")

if __name__ == "__main__":

    # time = Time()
    # time.hour = 1
    # time.minute = 0
    # time.second = 1
    # t = dist_per_sec(time, 24)
    # print(dist_per_sec(time, 24))

    # get_curret_day_of_week()

    bday = date(1988, 9, 11)
    days_to_bday(bday)

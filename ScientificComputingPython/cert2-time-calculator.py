def add_time(start, duration, start_day = ''):
    """
    Add a duration to a start time and return the new time.

    Parameters:
    start (str): The start time in the format 'HH:MM AM/PM'.
    duration (str): The duration to add in the format 'HH:MM'.
    start_day (str, optional): The starting day of the week. Defaults to ''.

    Returns:
    str: The new time in the format 'HH:MM AM/PM', optionally followed by the day of the week and the number of days later.

    Example:
    >>> add_time("3:00 PM", "3:10")
    '6:10 PM'
    >>> add_time("11:30 AM", "2:32", "Monday")
    '2:02 PM, Monday'
    >>> add_time("11:43 AM", "00:20")
    '12:03 PM'
    >>> add_time("10:10 PM", "3:30")
    '1:40 AM (next day)'
    >>> add_time("11:43 PM", "24:20", "Tuesday")
    '12:03 AM, Thursday (2 days later)'
    """
    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    start_day = start_day.lower()
    if start_day in weekdays:
        start_day_index = weekdays.index(start_day)
    else:
        start_day_index = False
        start_day = '' # in case someone enters random stuff

    period = start[-2:]
    hours, minutes = map(int, start[:-3].split(':'))

    if period == 'AM':
        hours = 0 if hours == 12 else hours
    else:
        hours = hours if hours == 12 else hours + 12

    add_hours, add_minutes = map(int, duration.split(':'))

    add_days = add_hours // 24

    new_hours = hours + add_hours % 24;
    new_minutes = minutes + add_minutes;

    new_period = 'AM'

    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60

    if new_hours >= 24:
        add_days += 1
        new_hours -= 24
    if new_hours >= 12:
        new_period = 'PM'
        new_hours -= 12
    if new_hours == 0:
        new_hours = 12

    new_time = f"{new_hours}:{new_minutes:02} {new_period}"

    if start_day:
        new_day_index = (start_day_index + add_days) % 7
        new_time += f", {weekdays[new_day_index].capitalize()}"

    if add_days == 1:
        new_time += ' (next day)'
    elif add_days > 1:
        new_time += f" ({add_days} days later)"

    return new_time

add_time('2:59 AM', '24:00', 'saturDay')

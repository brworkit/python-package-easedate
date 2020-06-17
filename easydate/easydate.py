"""Detailed descriptions will be added soon.
   At this time the code is enough.
"""

from datetime import datetime
from datetime import timedelta
from dateutil.parser import _parser

MONTHS_IN_YEAR = 12
TODAY = datetime.date
FORMATS = [
    '%Y-%m-%d',
    '%y-%m-%d',
    '%Y/%m/%d',
    '%y/%m/%d',
    "%d/%m/%Y",
    "%d-%m-%y",
    "%m/%d/%Y"
]

def __force_parse__(str_date):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    for fmt in FORMATS:
        try:
            return datetime.strptime(str_date, fmt).date()
        except Exception as e:
            print(f"format: {fmt} error: {e}")
    return str_date

def __formalize__(str_date):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    if isinstance(str_date, str):
        return parse(str_date)
    return str_date

def parse(str_date):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat.
    Final comments will be added soon.
    """
    return __force_parse__(str_date)

def str_to_date(str_date, input_format="%Y-%m-%d", output_format="%F"):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return parse(datetime.strptime(str_date, input_format).strftime(output_format))

def today():
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. 
    Final comments will be added soon.
    """
    return datetime.now().date()

def weekday(date, fmt="%A"):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = __formalize__(date)
    return date.strftime(fmt)

def add_day(date, days):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return __formalize__(date) + timedelta(days=days)

def diff_in_days(date, base_date = TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat.
    Final comments will be added soon.
    """
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return abs((date - base_date).days)

def diff_in_months(date, base_date = TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    from dateutil import relativedelta
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    result = relativedelta.relativedelta(date, base_date)
    return abs(result.years * MONTHS_IN_YEAR + result.months)

def diff_in_years(date, base_date = TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat.
    Final comments will be added soon.
    """
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return abs(date.year - base_date.year)

def is_after(date, base_date = TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return date > base_date

def is_before(date, base_date = TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat.
    Final comments will be added soon.
    """
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return date < base_date

def is_equal(date, base_date = TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return date == base_date







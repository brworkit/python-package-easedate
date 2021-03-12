"""Detailed descriptions will be added soon.
   At this time the code is enough.
"""

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

_MONTHS_IN_YEAR = 12
_TODAY = datetime.date
_FORMATS = [
    '%Y-%m-%d',
    '%y-%m-%d',
    '%Y/%m/%d',
    '%y/%m/%d',
    "%d/%m/%Y",
    "%d-%m-%y",
    "%m/%d/%Y"
]

def _force_parse(str_date):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    for output_format in _FORMATS:
        try:
            return datetime.strptime(str_date, output_format).date()
        except ValueError:
            return None

    return str_date

def _formalize(str_date):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    if isinstance(str_date, str):
        return parse(str_date)
    return str_date

def parse(str_date):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return _force_parse(str_date)

def str_to_date(str_date, input_format="%Y-%m-%d", output_format="%F"):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return parse(datetime.strptime(str_date, input_format).strftime(output_format))

def today():
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return datetime.now().date()

def weekday(date, output_format="%A"):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    return date.strftime(output_format)

def add_day(date, value):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return _formalize(date) + timedelta(days=value)


def add_month(date, value):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return _formalize(date) + relativedelta(months=value)


def add_year(date, value):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    return _formalize(date) + relativedelta(years=value)


def diff_in_days(date, base_date=_TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    base_date = _formalize(base_date)
    return abs((date - base_date).days)

def diff_in_months(date, base_date=_TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    base_date = _formalize(base_date)
    result = relativedelta(date, base_date)
    return abs(result.years * _MONTHS_IN_YEAR + result.months)

def diff_in_years(date, base_date=_TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    base_date = _formalize(base_date)
    return abs(date.year - base_date.year)

def is_after(date, base_date=_TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    base_date = _formalize(base_date)
    return date > base_date

def is_before(date, base_date=_TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    base_date = _formalize(base_date)
    return date < base_date

def is_equal(date, base_date=_TODAY):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    labore et dolore magna aliqua. Ut enim ad minim veniam,
    nisi ut aliquip ex ea commodo consequat. Duis aute irure
    esse cillum dolore eu fugiat nulla pariatur. Excepteur
    culpa qui officia deserunt mollit anim id est laborum.
    Final comments will be added soon.
    """
    date = _formalize(date)
    base_date = _formalize(base_date)
    return date == base_date

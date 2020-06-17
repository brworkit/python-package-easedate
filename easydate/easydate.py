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
    for fmt in FORMATS:
        try:
            return datetime.strptime(str_date, fmt).date()
        except Exception as e:
            print(f"format: {fmt} error: {e}")
    return str_date

def __formalize__(str_date):
    if isinstance(str_date, str):
        return parse(str_date)
    return str_date

def parse(str_date):
    return __force_parse__(str_date)

def str_to_date(str_date, input_format="%Y-%m-%d", output_format="%F"):
    return parse(datetime.strptime(str_date, input_format).strftime(output_format))

def today():
    return datetime.now().date()

def weekday(date, fmt="%A"):
    date = __formalize__(date)
    return date.strftime(fmt)

def add_day(date, days):
    return __formalize__(date) + timedelta(days=days)

def diff_in_days(date, base_date = TODAY):
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return abs((date - base_date).days)

def diff_in_months(date, base_date = TODAY):
    from dateutil import relativedelta
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    result = relativedelta.relativedelta(date, base_date)
    return abs(result.years * MONTHS_IN_YEAR + result.months)

def diff_in_years(date, base_date = TODAY):
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return abs(date.year - base_date.year)

def is_after(date, base_date = TODAY):
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return date > base_date

def is_before(date, base_date = TODAY):
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return date < base_date

def is_equal(date, base_date = TODAY):
    date = __formalize__(date)
    base_date = __formalize__(base_date)
    return date == base_date







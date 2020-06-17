# easydate
    
## Description
A python package for easy date use and conversions.

# Install 
    pip install easydate


# Currently Available functions

```

today()

parse(str_date)

str_to_date(str_date, input_format, output_format)

weekday(date, output_format)

add_day(date, value)

add_month(date, value)

add_year(date, value)

diff_in_days(date, base_date)

diff_in_months(date, base_date)

diff_in_years(date, base_date) 

is_after(date, base_date) 

is_before(date, base_date)

is_equal(date, base_date)

```

# Usage example 

```python

from easydate.easydate import *


result = str_to_date("22/03/2020", input_format="%d/%m/%Y")

print(result)

# 2020-03-22


result = parse("01/03/2020")

print(result)

# 2020-03-01


result = weekday("22/03/2020")

print(result)

# Sunday


result = weekday("22/03/2020", output_format="%a")

print(result)

# 0 (Sunday is indexed as 0 and Saturday is indexed as 7)


result = add_day("22/03/2020", value=1)

print(result)

# 2020-03-23


result = add_day("22/03/2020", value=-1)

print(result)

# 2020-03-21


result = add_month("22/03/2020", value=1)

print(result)

# 2020-04-23

```

## PyPi

[easydate](https://pypi.org/project/easydate)

## Author

[**2020 brworkit**](https://github.com/brworkit).

## License
[MIT License.](https://opensource.org/licenses/MIT)    

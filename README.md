# Easy JSON2JSON
    
## Description
A python package for easy date use.

# Install 
    pip install easydate

# Usage example 

## Case #1 Simple JSON
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

result = weekday("22/03/2020", fmt="%a")

print(result)

# 0 (Sunday is indexed as 0 and Saturday is indexed as 7)

result = add_day("22/03/2020", days=1)

print(result)

# 2020-03-23

```

## PyPi

[easydate](https://pypi.org/project/easydate)

## Author

[**2020 brworkit**](https://github.com/brworkit).

## License
[MIT License.](https://opensource.org/licenses/MIT)    

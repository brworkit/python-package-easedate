from datetime import datetime
from easydate.easydate import *

# TODO:
    # Human-intelligible date
    # https://strftime.org/  apply theses rules

def test_parse_from_dd_mm_yyyy_to_yyyy_mm_dd():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y")
    assert result == parse("2020-03-22")

def test_parse_from_dd_mm_yyyy_to_yy_mm_dd():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%y-%m-%d")
    assert result == parse("20-03-22")

def test_parse_from_dd_mm_yyyy_to_yyyy_mm_dd_slash():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%Y/%m/%d")
    assert result == parse("2020/03/22")

def test_parse_from_dd_mm_yyyy_to_yy_mm_dd_slash():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%y/%m/%d")
    assert result == parse("20/03/22")

def test_parse_from_dd_mm_yyyy_to_mm_dd_yyyy():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%m-%d-%Y")
    assert result == parse("03-22-2020")

def test_parse_from_dd_mm_yyyy_to_mm_dd_yy():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%m-%d-%y")
    assert result == parse("03-22-20")

def test_parse_from_dd_mm_yyyy_to_mm_dd_yyyy_slash():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%m/%d/%Y")
    assert result == parse("03/22/2020")

def test_parse_from_dd_mm_yyyy_to_mm_dd_yy_slash():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%m/%d/%y")
    assert result == parse("03/22/20")

def test_parse_from_dd_mm_yyyy_to_dd_mm_yyyy():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%d-%m-%Y")
    assert result == parse("22-03-2020")

def test_parse_from_dd_mm_yyyy_to_dd_mm_yy():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%d-%m-%y")
    assert result == parse("22-03-20")

def test_parse_from_dd_mm_yyyy_to_dd_mm_yyyy_slash():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%d/%m/%Y")
    assert result == parse("22/03/2020")

def test_parse_from_dd_mm_yyyy_to_dd_mm_yy_slash():
    result = str_to_date("22/03/2020", input_format="%d/%m/%Y", output_format="%d/%m/%y")
    assert result == parse("22/03/20")

def test_today_date():
    assert datetime.now().date() == today()

def test_today_date_name():
    assert today().strftime("%A") == weekday(today())

def test_today_date_name_from_str():
    assert "Wednesday" == weekday("2020-05-20")

def test_weekday_name():
    assert datetime.strptime("2020-06-01", '%Y-%m-%d').strftime("%A") == "Monday"

def test_weekday_index():
    assert datetime.strptime("2020-06-01", '%Y-%m-%d').strftime("%w") == "1"

def test_today_date_name_abbreviation():
    assert today().strftime("%a") == weekday(today(), formatting="%a")

def test_add_one_day():
    assert add_day("2020-06-01", 1) == datetime.strptime("2020-06-02", '%Y-%m-%d').date()

def test_add_two_days():
    assert add_day("2020-06-01", 2) == datetime.strptime("2020-06-03", '%Y-%m-%d').date()

def test_diff_in_days_zero():
    assert diff_in_days("2020-06-01", "2020-06-01") == 0

def test_diff_in_days_one():
    assert diff_in_days("2020-06-01", "2020-06-02") == 1

def test_diff_in_days_twenty():
    assert diff_in_days("2020-06-01", "2020-06-21") == 20

def test_diff_in_months_zero():
    assert diff_in_months("2020-06-01", "2020-06-01") == 0

def test_diff_in_months_one():
    assert diff_in_months("2020-06-01", "2020-07-01") == 1

def test_diff_in_months_twelve():
    assert diff_in_months("2020-06-01", "2021-06-01") == 12

def test_diff_in_years_zero():
    assert diff_in_years("2020-06-01", "2020-06-01") == 0

def test_diff_in_years_one():
    assert diff_in_years("2020-06-01", "2021-07-01") == 1

def test_diff_in_years_twelve():
    assert diff_in_years("2023-06-01", "2020-06-01") == 3

def test_is_after_by_days_false():
    assert is_after("2020-06-01", "2020-06-02") is False

def test_is_after_by_months_false():
    assert is_after("2020-05-01", "2020-06-01") is False

def test_is_after_by_years_false():
    assert is_after("2019-06-01", "2020-06-01") is False

def test_is_after_by_days_true():
    assert is_after("2020-06-03", "2020-06-02") is True

def test_is_after_by_months_true():
    assert is_after("2020-07-01", "2020-06-01") is True

def test_is_after_by_years_true():
    assert is_after("2021-06-01", "2020-06-01") is True

def test_is_before_by_days_false():
    assert is_before("2020-06-03", "2020-06-02") is False

def test_is_before_by_months_false():
    assert is_before("2020-07-01", "2020-06-01") is False

def test_is_before_by_years_false():
    assert is_before("2021-06-01", "2020-06-01") is False

def test_is_before_by_days_true():
    assert is_before("2020-06-01", "2020-06-02") is True

def test_is_before_by_months_true():
    assert is_before("2020-05-01", "2020-06-01") is True

def test_is_before_by_years_true():
    assert is_before("2019-06-01", "2020-06-01") is True

def test_is_equals_false():
    assert is_equal("2021-06-02", "2020-06-01") is False

def test_is_equals_true():
    assert is_equal("2020-06-01", "2020-06-01") is True

def test_parse_dd_mm_yy_bar():
    assert parse("01/05/2020") == parse("2020-05-01")

def test_parse_dd_mm_yy_bar_inverse():
    assert parse("2020/05/01") == parse("2020-05-01")
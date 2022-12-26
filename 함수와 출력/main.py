def days_in_month(enter_year, enter_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  for month in month_days:
    if is_leap(enter_year) and enter_month == True:
        month_days[enter_month-1] = 29
        return month_days[enter_month-1]
    else:
        return month_days[month-1]
import datetime
from dateutil.relativedelta import relativedelta


def get_years_months(my_date, num_months):
    cur_month = my_date.month
    cur_year = my_date.year

    result = []
    for i in range(num_months):
        if cur_month == 0:
            cur_month = 12
            cur_year -= 1
        result.append((cur_year, cur_month))
        cur_month -= 1

    return result

if __name__ == "__main__":
    import datetime
    result = get_years_months(datetime.date.today(), 1)
    print (result)


    print (type(result))
    for months in result:
        print (months)
        print (type(months))
        (month, day) = months
        print (month)
        print (day)

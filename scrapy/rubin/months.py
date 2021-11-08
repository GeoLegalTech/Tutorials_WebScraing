import datetime

def get_years_months(my_date, num_months):
    cur_month = my_date.month
    cur_year = my_date.year
    # print (type(cur_month))
    # x = "4"
    # print (x.strftime("%m"))

    result = []
    for i in range(num_months):
        print (cur_month)
        print (type(cur_month))
        print (len(str(cur_month)))
        print ("-----")
        if cur_month == 0:
            cur_month = 12
            cur_year -= 1

        elif len(str(cur_month)) == 1:
            cur_month -= 1
            cur_month = "0" + str(cur_month)
            print ("This is modified ----> " + cur_month)
        result.append((cur_year, cur_month))
        cur_month = int(cur_month)
        cur_month -= 1

    return result


x = get_years_months(datetime.date.today(), 3)
print (x)

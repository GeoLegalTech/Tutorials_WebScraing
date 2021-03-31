from urllib.parse import urlparse
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


# url = "https://schifferstadt.more-rubin1.de/sitzungskalender.php?"
# parts = urlparse(url)
# test = parts.netloc
# print (parts)
# print (test)
# print (parts.scheme + '://'+ test)
# # parts = parts._replace(query = 'skc_zeitraum=1&skc_ansicht=k&d_von=HOLA&d_bis=2021-01&koerperschaft=')
# # print (parts.geturl())


# url = "https://schifferstadt.more-rubin1.de/sitzungskalender.php?skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft="
# parts = urlparse(url)
# url =  parts.geturl()
# print (url)
# base_url = urlparse(base)
# base_url._replace(query="query=skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft=")
# base_url = base_url.geturl()
#
#
#
#

    # print (type(result))
    # for months in result:
    #     print (months)
    #     print (type(months))
    #     (month, day) = months
    #     print (month)
    #     print (day)

# if __name__ == "__main__":
#     import datetime
#     result = get_years_months(datetime.date.today(), 1)
#     print (result)


base_url = "https://schifferstadt.more-rubin1.de/sitzungskalender.php?skc_zeitraum=1&skc_ansicht=k&d_von=2021-01&d_bis=2021-01&koerperschaft="
months = get_years_months(datetime.date.today(), 4)
for month in months:
    (month, day) = month
    new_date = str(month) + "-" + str(day)
    url = urlparse(base_url)
    old_date = url.query.split('=')[3].split('&')[0]
    parts = url.query
    parts = parts.replace(old_date, new_date)
    url = url._replace(query=parts)
    url = url.geturl()
    print (url)

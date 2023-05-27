def mayan_date_convert(mayan_date):
    mayan_zero = [13, 20, 7, 16, 3]
    date_multiples = [144000, 7200, 360, 20, 1]
    date_diff = [None] * 5
    days = 1
    date = [1, 1, 2000]

    for i in range(5):
        date_diff[i] = mayan_date[i] - mayan_zero[i]

    for i in range(5):
        if date_multiples[i] * date_diff[i] != 0:
            days = days + date_multiples[i] * date_diff[i]

    while days != 0:

        if date[2] % 4 == 0:
            days_in_year = 366
            months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_year = 365
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


        if days - days_in_year >= 0:
            date[2] += 1
            days -= days_in_year
        else:
            for len_month in months:
                if days - len_month >= 0:
                    days -= len_month
                    date[1] += 1
                else:
                    date[0] = days
                    days = 0
                    break

    return date

mayan_date = input("Enter a mayan date: ")
mayan_date = mayan_date.split()
mayan_date = list(map(int, mayan_date))
print(mayan_date_convert(mayan_date))
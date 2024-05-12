def fix_age(age):
    ret_age = age

    if 13 <= age <= 19:

        if age != 15 or age != 16:
            ret_age = 0

    return ret_age

def filter_teens(a=13, b=13, c=13):
    ages = (a, b, c)
    sum = 0

    for i in ages:
        sum += fix_age(i)

    print(sum)


filter_teens()

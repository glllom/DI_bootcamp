RETIREMENT_MEN = 67
RETIREMENT_WOMEN = 62


def get_age(year, month, day):
    current_year = 2022
    current_month = 2
    return current_year - year - (month > current_month)


def can_retire(gender, date_of_birth):
    if gender == 'm':
        return get_age(*map(int, date_of_birth.strip().split('/'))) >= RETIREMENT_MEN
    elif gender == 'f':
        return get_age(*map(int, date_of_birth.strip().split('/'))) >= RETIREMENT_WOMEN
    else:
        raise Exception('Please, correct your gender')


gender, date_of_birth = input("Please input your gender('m' of 'f') and date of birth separated by comma."
                              "\nDate must be in format YYYY/MM/DD: ").strip().split(',')
try:
    if can_retire(gender, date_of_birth):
        print("You can retire.")
    else:
        print("You can't retire.")
except Exception as e:
    print(e)

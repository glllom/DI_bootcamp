def get_full_name(first_name, last_name, middle_name=None):
    return "".join([first_name.capitalize() + ' ', "" if not middle_name else
                middle_name.capitalize() + ' ', last_name.capitalize()])


print(get_full_name(first_name="bruce", last_name="lee"))
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))

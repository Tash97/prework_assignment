#question 1:
def hello(user_name):
    print("hello_" + user_name)

#question 2:
def first_odds():
    x = 1
    while x < 100:
        print(x)
        x += 1

#question 3:
def max_num_in_list(a_list):
    return (max(a_list))

#question 4:
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

#question 5:
def is_consecutive(a_list):
    if a_list == list(range(min(a_list), max(a_list) + 1)):
        return True
    else:
        return False

lists = [1, 2, 3, 4, 5]
print(is_consecutive(lists))


is_male = False
is_tall = True

# basic if statement
if is_male:
    print("You are a male")
else:
    print("You are a female")

# or condition
if is_male or is_tall:
    print("You are a male or tall")
else:
    print("you are not a male nor tall")

# and condition
if is_male and is_tall:
    print("you are a tall male")
else:
    print("you are either not a male or not tall")

# else if condition and not condition
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a male but not tall")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not a male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(2,3,4))

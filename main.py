def plus(num1, num2):
    if (type(num1) is int or type(num1) is float) and (type(num2) is int or type(num2) is float):
        return num1 + num2
    else:
        return None


print(plus(1, 5.2))

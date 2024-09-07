def get_multiplied_digits(number):
    str_number : str = str (number)
    first : int = int(str_number[0])

    if len(str_number) > 1:
        first *= get_multiplied_digits(int(str_number[1:]))
        return first
    else:
        return first

result = get_multiplied_digits(40203)
print("Произведение цифр этого числа: ", result)
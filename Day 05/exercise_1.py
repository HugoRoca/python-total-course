def distinct_return(num1, num2, num3):
    plus = num1 + num2 + num3
    new_list = [num1, num2, num3]
    big_number = max(new_list)
    small_number = min(new_list)

    if plus > 15:
        return big_number
    elif plus < 10:
        return small_number
    else:
        return plus - (big_number + small_number)


print(distinct_return(9, 2, 3))

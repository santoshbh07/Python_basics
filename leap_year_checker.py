def is_leap_year(year):
    def is_divisible_by_4():
        if year%4 == 0:
            return True
        else:
            return False
    
    def is_evenly_divisible_by_100():
        if year%100 == 0:
             return True
        else:
            return False
             
    def is_divisible_by_400():
        if year%400 == 0:
            return True
        else:
            return False
    
    condition_1 = is_divisible_by_4()
    condition_2 = is_evenly_divisible_by_100()
    condition_3 = is_divisible_by_400()

    if condition_1 and not condition_2:
        return True
    elif condition_1 and condition_2 and condition_3:
        return True
    else:
        return False

result = is_leap_year(2100)
print(result)
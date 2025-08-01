def is_armstrong_number(number):
    number_str = str(number)
    number_count = len(number_str)
    ArmNum = 0

    for i in range(number_count):
        ArmNum = ArmNum + int(number_str[i])**number_count
    
    if number == ArmNum:
        return True
    else:
        return False
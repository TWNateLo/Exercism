def convert(number):
    temp = ""
    if number%3 == 0:
        temp += "Pling"
    if number%5 == 0:
        temp += "Plang"
    if number%7 == 0:
        temp += "Plong"
    if number%3 != 0 and number%5 != 0 and number%7 != 0:
        temp = str(number)
    return temp

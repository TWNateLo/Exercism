def steps(number):
    if number<=0 or type(number)!=int:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number!=1:
        if number%2 == 0:
            number = number/2
            steps = steps + 1
        else:
            number = (number*3)+1
            steps = steps + 1
    return steps
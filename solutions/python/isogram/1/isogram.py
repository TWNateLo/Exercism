def is_isogram(string):
    string = string.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    isisogram = True
    for a in alphabet:
        if string.count(a) > 1:
            isisogram =  False
            break
        else:
            isisogram = True
    return isisogram
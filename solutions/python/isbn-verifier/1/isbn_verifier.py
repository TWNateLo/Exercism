def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False    
    elif all(isbn[9] != c for c in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X")):
        return False
    elif not isbn[0:9].isdigit():
        return False
    elif isbn[9] != "X" and (int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + int(isbn[9]) * 1) % 11 == 0:
        return True
    elif isbn[9] == "X" and (int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + 10 * 1) % 11 == 0:
        return True
    else:
        return False
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    isPangram = True
    if sentence == "":
        return False
    for a in alphabets:
        if sentence.find(a) != -1:
            isPangram = True
        else:
            isPangram = False
            break
    return isPangram
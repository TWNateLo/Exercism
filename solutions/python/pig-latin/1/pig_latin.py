def translate(text):
    words_list = text.split()
    for i in range(len(words_list)):
        words_list[i] = singleWord(words_list[i])
    result = " ".join(words_list)
    return result

def singleWord(text):
    vowels = ("a", "e", "i", "o", "u")
    temp = text
    if text[0] in vowels or text[0:2] == "xr" or text[0:2] == "yt":
        temp = temp + "ay"
    elif all(i not in vowels for i in text[:text.find("qu")]) and "qu" in text:
        temp = temp[(text.find("qu")+2):] + temp[:text.find("qu")+2] + "ay"
    elif all(i not in vowels for i in text[:text.find("y")]) and "y" in text and text.find("y") > 0:
        temp = temp[(text.find("y")):] + temp[:text.find("y")] + "ay"
    elif text[0] not in vowels:
        for i in range(len(text)):
            if text[i] not in vowels:
                i += 1
            else:
                break
        temp = temp[i:] + temp[:i] + "ay"
    return temp
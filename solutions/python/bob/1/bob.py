def response(hey_bob):
    if hey_bob.isspace() == False:
        hey_bob = hey_bob.strip()
    if hey_bob.endswith("?") and hey_bob.isupper() == False:
        return "Sure."
    elif hey_bob.isupper() == True and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    elif hey_bob.isupper() == True and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isspace() == True or hey_bob == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
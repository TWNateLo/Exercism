def is_paired(input_string: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    opens = set(pairs.values())
    stack = []

    for ch in input_string:
        if ch in opens:
            stack.append(ch)
        elif ch in pairs:  # it's a closing bracket
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False

    return not stack
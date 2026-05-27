

# opening bracket must be closed immediately after,
# meaning ([]) will return false because ( isnt closed immediately by )

def consecutiveBrackets(s: str) -> bool:
    rules = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    if len(s) % 2 != 0:
        return False

    first = s[:1]
    if first == ")" or first == "}" or first == "]":
        return False
    
    prev = first
    count = 0

    for char in s:
        count += 1
        
        if count == 1:
            continue

        if (prev != ")" and prev != "}" and prev != "]") and char != rules[prev]:
            return False
        
        if count % 2 == 0:
            if char == "(" or char == "{" or char == "[":
                return False

        prev = char

    return True



s1 = "aaAbcBC" #3
s2 = "abc"     #0
s3 = "AbBCab"  #0
s4 = "UUuU"    #0

def numberOfSpecialChars(word: str) -> int:
    specials = []

    uppercase = []
    for c in word:
        if c == c.upper() and not c in uppercase:
            uppercase.append(c)

    for u in uppercase:
        pos = word.find(u)

        slice1 = word
        slice1 = slice1[pos:]
        #skip if lowercase u appears after uppercase u
        if slice1.find(u.lower()) != -1:
            continue

        slice2 = word
        slice2 = word[:pos]
        if slice2.find(u.lower()) != -1:
            specials.append(u)

    return len(specials)


print(numberOfSpecialChars(s4))
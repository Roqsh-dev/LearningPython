
def lengthOfLargestSubstring(s):
    if s == "":
        return "", 0
    
    longestSubstring = ""
    potentialSubstrings = []

    for digit in s:
        if digit not in longestSubstring:
            longestSubstring += digit
            potentialSubstrings.append(longestSubstring)
        else:
            pos = longestSubstring.find(digit)
            longestSubstring = longestSubstring[(pos+1):]
            longestSubstring += digit

    longestSubstring = potentialSubstrings[0]
    for element in potentialSubstrings:
        if len(element) > len(longestSubstring):
            longestSubstring = element
        
    return longestSubstring, len(longestSubstring)

while True:
    string = input("Enter your string: ")

    substring, length = lengthOfLargestSubstring(string)
    print(f"Longest substring: {substring}")
    print(f"Length: {length}\n")
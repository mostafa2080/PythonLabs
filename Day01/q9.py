def longest_substring(s):
    longest = ""
    current = ""

    for i in range(len(s)):
        if i == 0 or s[i] >= s[i-1]:
            current += s[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = s[i]
    
    if len(current) > len(longest):
        longest = current
    
    print("Longest substring in alphabetical order is:", longest)


longest_substring("mostafa")

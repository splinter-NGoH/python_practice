def lengthOfLongestSubstring(s):
    pointer = 0
    max_length = 0
    length = 0
    for char in range(pointer, len(s) - 1):
        print(char)
        print(pointer)
        print(s[char])
        if s[char] not in s[: pointer + 1]:
            print("in if", s[: pointer + 1])
            pointer += 1
            length += 1
            if max_length < length:
                max_length = length
    print(pointer)
    print(max_length)


lengthOfLongestSubstring("pwwkew")

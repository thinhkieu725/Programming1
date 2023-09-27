"""
COMP.CS.100 Programming 1
6.9.TheLongestSubstringInOrder.py
Creator: Thinh Kieu
Student number: 152167613
"""

def longest_substring_in_order(text):
    """
    searches for the longest substring with its characters in alphabetic order and returns it
    param: text _ strings
    return _ string _ longest substring in alphabetic order
    """

    paramLength = len(text)

    if paramLength == 0:
        return ""

    longestLength = 1
    longestSubString = text[0]

    for i in range(paramLength):
        tempLength = 1
        for j in range(i + 1, paramLength):
            if text[j-1] < text[j]:
                tempLength += 1
                if j == paramLength - 1:
                    if tempLength > longestLength:
                        longestLength = tempLength
                        longestSubString = text[i:]
            else:
                if tempLength > longestLength:
                    longestLength = tempLength
                    longestSubString = text[i:j]
                break

    return longestSubString

def main():
    print(longest_substring_in_order("abcabcdefgabab"))
    print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))
    print(longest_substring_in_order("aaa"))

if __name__ == "__main__":
    main()

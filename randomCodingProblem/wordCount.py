"""
Given a sentence return the # of words in string
- Spaces can be in the front and behind the string
- Examples:
    "this is a dog" >> 4
    " i hate interviews so much " >> 5
    "  must  studyyyy  more  " >> 3
"""

import sys
def countWords(sent):
    # init variables
    i = 0
    count = 0

    # get first starting word
    while(sent[i] == " "):
        i += 1

    # make sure index is still in range of str
    while(i < len(sent)):

        # move till you get a space
        while i < len(sent) and sent[i] != " ":
            i += 1

        # count++ (found word)
        count += 1

        # move till you get letter
        while i < len(sent) and sent[i] == " ":
            i += 1

    return count

s = [
    "this is a dog",
    " i hate interviews so much ",
    "  must  studyyyy  more  "
    ]

for item in s:
    print(countWords(item))

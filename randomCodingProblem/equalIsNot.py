"""
Given a string, return true if the number of appearances of "is" anywhere in the string is equal to the number of appearances of "not" anywhere in the string (case sensitive).

equalIsNot("This is not") → false
equalIsNot("This is notnot") → true
equalIsNot("noisxxnotyynotxisi") → true
"""

def equalIsNot(s):
    s.lower()
    return s.count('is') == s.count('not')

testCases = {
    "This is not": False,
    "This is notnot": True,
    "noisxxnotyynotxisi": True,
    "noisxxnotyynotxsi": False,
    "xxxyyyzzzintint": True,
    "": True,
    "isisnotnot": True,
    "isisnotno7Not": False,
    "isnotis": False,
    "mis3notpotbotis" : False
}

flag = True
for test, result in testCases.items():
    if equalIsNot(test) != result:
        print("Test: " + test + " failed")
        flag = False

if flag:
    print("All test passed!")

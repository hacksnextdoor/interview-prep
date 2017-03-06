"""
Write an efficient function that checks whether any permutation of an input string is a palindrome
You can assume the input string only contains lowercase letters.

Examples:
"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""

def str_to_map(stri):
    dict = {}
    for letter in stri:
        count = dict.get(letter, "dne")
        if count != "dne":
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

def permutation_palindrome(stri):
    mapStr = str_to_map(stri)
    odd_values = 0
    for key, value in mapStr.items():
        if value % 2 != 0:
            odd_values += 1
    if len(stri) % 2 == 0: # even values
        return odd_values == 0
    return odd_values == 1 # odd


test = {
    "civic": True,
    "ivicc": True,
    "civil": False,
    "livci": False,
    "ccccccccc": True,
    "aaabbbcccc": False
}

for test, result in test.items():
    if permutation_palindrome(test) != result:
        print("error w/ " + test)

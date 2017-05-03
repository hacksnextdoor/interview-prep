/*
 
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

 The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 
 */

func checkBrackets(brackets:String) -> Bool {
    
    // change string to array
    var str_array = brackets.characters.map{String($0)}
    
    // create stack
    var stack = [String]()

    // do matching....
    for b in str_array {
        if b == "{" {
            stack.append("}")
        } else if b == "(" {
            stack.append(")")
        } else if b == "[" {
            stack.append("]")
        } else if (stack.isEmpty || stack.removeLast() != b) {
            return false
        }
    }
    return stack.isEmpty
}

var input = "()[]{}"
print(checkBrackets(brackets: input))


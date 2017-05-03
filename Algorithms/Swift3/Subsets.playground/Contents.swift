/*
 
 Given a set of distinct integers, nums, return all possible subsets.
 Note: The solution set must not contain duplicate subsets.
 For example,
 If nums = [1,2,3], a solution is:
 [
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
 ]
 
 */

import Darwin
var str = "some string"

func subsets(_ inArray: [Int]) -> [[Int]] {
    let combos = Int(pow(Double(2),Double(inArray.count))) // 2^3 >> 8
    var output = [[Int]]()
    for n in 0 ... combos {
        var temp = [Int]()
        for j in 0 ... inArray.count {
            if n & (1 << j) > 0 {
                print(j, terminator: "")
                // temp.append(inArray[j])
            }
        }
        output.append(temp)
    }
    return output
}

print("hello")
var nums = [1,2,3]
print(subsets(nums))

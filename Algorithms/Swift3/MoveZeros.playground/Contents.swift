/*
 
 Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
 Note:
 1. You must do this in-place without making a copy of the array.
 2. Minimize the total number of operations.
 */

func moveZeros( _ arr: inout [Int]) -> [Int] {
    var left = 0
    var right = arr.count - 1
    
    while left < right {
        while arr[left] != 0 {
            left += 1
        }
        
        while arr[right] == 0 {
            right -= 1
        }
        
        if right < left {
            break
        }
        
        // swap
        let temp = arr[right]
        arr[right] = arr[left]
        arr[left] = temp
        
        left += 1
        right -= 1 
    }
    
    return arr
}

var nums = [0, 1, 0, 3, 12]
print(moveZeros(&nums))


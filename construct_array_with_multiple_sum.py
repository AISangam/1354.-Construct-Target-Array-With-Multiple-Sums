"""
1354. Construct Target Array With Multiple Sums
Link for the problem: 
https://leetcode.com/problems/construct-target-array-with-multiple-sums/


 Credit for this problem goes to leet code
"""


"""
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true
 

Constraints:

n == target.length
1 <= n <= 5 * 104
1 <= target[i] <= 109

"""

# Solution 
import unittest


def target_array_with_multiple_sum(target_array):
    """
    input to this function: array
    output: transformned array
    """
    sum_target_array = sum(target_array)
    max_value_target_array = max(target_array)
    remaining_sum_except_max = sum_target_array - max_value_target_array
    diff_max_and_rest = max_value_target_array - remaining_sum_except_max
    """
    Condition to check for the false case
    
    condition1: when the difference between sum and max > max
    condition2: when the difference between the max and remaining == 0
    condition3: when there is only one element in the target array
    """
    if remaining_sum_except_max > max_value_target_array or diff_max_and_rest == 0 or len(target_array)==1:
        return False
            
    max_index = target_array.index(max_value_target_array)
    target_array[max_index] = diff_max_and_rest
    print("Target array after transformation....", target_array)
    """
    Base condition for recursion so that we can break recursion
    """
    if max(target_array) > 1:
        target_array_with_multiple_sum(target_array)
    
    # print()
    result = all(element == 1 for element in target_array)
    if result:
        return True
    else:
        return False
    
    


class test_cases(unittest.TestCase):

		def cases(self):
			
            # case 1
			desired_output = True
			input_arr = [9,3,5]
            # error message in case if test case got failed
			message ="Case 1 result failed"
			self.assertEqual(desired_output, target_array_with_multiple_sum(input_arr), 
				message)

            # case 2
			desired_output = False
			input_arr = [1,1,1,2]
            # error message in case if test case got failed
			message ="Case 2 result failed."
			self.assertEqual(desired_output, target_array_with_multiple_sum(input_arr), 
				message)  

            # case 3
			desired_output = True
			input_arr = [8,5]
            # error message in case if test case got failed
			message ="Case 3 result failed."
			self.assertEqual(desired_output, target_array_with_multiple_sum(input_arr), 
				message)         

			return "All cases are passed"

check_case = test_cases()
output = check_case.cases()
print(output)

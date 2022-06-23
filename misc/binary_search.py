import unittest


def binary_search(sorted_array, target):
    """

    Given an array of integers nums which is sorted in ascending order, and an integer target, 
    write a function to search target in nums. If target exists, then return its index.
    Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.



    Example 1:

    ====================================================

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    ====================================================
    """

    left = 0
    right = len(sorted_array)
    mid = (left + right) // 2
    while left < right:
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target:
            right = mid
        else:
            left = mid + 1
        mid  = (left + right) // 2
    return -1



class Test(unittest.TestCase):

    def test_1(self):
        nums = [-1,0,3,5,9,12]
        target = 9

        self.assertEqual(binary_search(nums, target),4)

    def test_2(self):
        nums = [-1,0,3,5,9,12]
        target = 2
        self.assertEqual(binary_search(nums, target),-1)

    def test_3(self):
        nums = []
        target = 2
        self.assertEqual(binary_search(nums, target),-1)


if __name__ == "__main__":
    unittest.main()

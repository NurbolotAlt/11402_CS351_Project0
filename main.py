def twoSumArray(nums, target):
    """
    Brute force approach using nested loops.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def twoSumHashTable(nums, target):
    """
    Optimized approach using a hash table.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def run_tests():
    """Run comprehensive test cases for twoSumArray and twoSumHashTable."""
    test_cases = [
        # Normal cases
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        # Edge cases: duplicates
        {"nums": [1, 5, 3, 3], "target": 6, "expected": [1, 2]},
        {"nums": [0, 4, 3, 0], "target": 0, "expected": [0, 3]},
        # Edge cases: negative numbers
        {"nums": [-3, 4, 3, 90], "target": 0, "expected": [0, 2]},
        {"nums": [-1, -2, -3, -4, -5], "target": -8, "expected": [2, 4]},
        # Boundary conditions
        {"nums": [], "target": 5, "expected": []},
        {"nums": [5], "target": 5, "expected": []},
        {"nums": [1, 2], "target": 3, "expected": [0, 1]},
        {"nums": [2, 7, 11, 15, 6], "target": 22, "expected": [2, 4]},
    ]

    for case in test_cases:
        nums = case["nums"]
        target = case["target"]
        expected = case["expected"]
        arr_result = twoSumArray(nums, target)
        hash_result = twoSumHashTable(nums, target)
        print(f"nums={nums}, target={target}")
        print(f"  Array result: {arr_result}, expected: {expected}")
        print(f"  Hash result:  {hash_result}, expected: {expected}")
        print("  PASS" if arr_result == expected and hash_result == expected else "  FAIL")



if __name__ == "__main__":
    run_tests()

    
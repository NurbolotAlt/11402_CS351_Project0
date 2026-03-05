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


if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Array approach: {twoSumArray(nums, target)}")
    print(f"Hash table approach: {twoSumHashTable(nums, target)}")
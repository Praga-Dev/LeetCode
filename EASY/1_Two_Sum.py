def twoSum(nums: list[int], target: int) -> list[int]:
    dict_num = {}

    
    for i in range(len(nums)):
        result = target - nums[i] # no abs()
        if result in dict_num:
            return [dict_num[result], i]
        else:
            dict_num[nums[i]] = i
    
    return []


# Sample testcases
print(twoSum([2,7,11,15], 9))  #[0, 1]
print(twoSum([-3,7,3,15], 0))  #[0, 2]
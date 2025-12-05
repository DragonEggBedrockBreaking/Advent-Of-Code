with open("input.txt", "r", encoding="utf8") as f:
    lines = [tuple(map(int, line)) for line in f.read().splitlines()]

def joltage(nums, count=12):
    if count == 1:
        return max(nums)
    index = nums.index(first := max(nums[:-count+1]))
    rest = joltage(nums[index+1:], count-1)
    return first * 10**(count-1) + rest 

print(sum(map(joltage, lines)))
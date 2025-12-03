with open("input.txt", "r", encoding="utf8") as f:
    lines = [tuple(map(int, line)) for line in f.read().splitlines()]

def joltage(nums):
    index = nums.index(first := max(nums[:-1]))
    second = max(nums[index+1:])
    return first * 10 + second

print(sum(map(joltage, lines)))
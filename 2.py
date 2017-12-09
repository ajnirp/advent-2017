def line_checksum(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] % nums[j] == 0:
                return nums[i] // nums[j]
            elif nums[j] % nums[i] == 0:
                return nums[j] // nums[i]
    return 0

with open('2.txt', 'r') as f:
    checksum1 = 0
    for line in f.readlines():
        nums = list(map(int, line.strip().split('\t')))
        checksum1 += max(nums) - min(nums)
    print(checksum1)

with open('2.txt', 'r') as f:
    checksum2 = 0
    for line in f.readlines():
        nums = list(map(int, line.strip().split('\t')))
        checksum2 += line_checksum(nums)
    print(checksum2)
with open('5.txt', 'r') as f:
    nums = [int(x.strip()) for x in f.readlines()]
    i, steps = 0, 0
    while True:
        offset = nums[i]
        prev = i
        i += offset
        steps += 1
        nums[prev] += 1
        if i >= len(nums):
            print(steps)
            break

with open('5.txt', 'r') as f:
    nums = [int(x.strip()) for x in f.readlines()]
    i, steps = 0, 0
    while True:
        offset = nums[i]
        prev = i
        i += offset
        steps += 1
        if offset >= 3:
            nums[prev] -= 1
        else:
            nums[prev] += 1
        if i >= len(nums):
            print(steps)
            break
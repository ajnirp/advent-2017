def make_config(banks):
    return ','.join(map(str, banks))

with open('6.txt', 'r') as f:
    banks = list(map(int, f.read().strip().split('\t')))

    n = len(banks)

    seen_configs = set()
    redist_cycles = 0

    init_config = make_config(banks)
    seen_configs.add(init_config)

    added_at = {}
    added_at[init_config] = 0

    while True:
        max_val, max_idx = banks[0], 0
        for i in range(1, n):
            if banks[i] > max_val:
                max_val = banks[i]
                max_idx = i
        banks[max_idx] = 0
        for j in range(max_val):
            offset = (max_idx + 1 + j) % n
            banks[offset] += 1
        redist_cycles += 1
        config = make_config(banks)
        if config in seen_configs:
            print(redist_cycles)
            print(redist_cycles - added_at[config])
            break
        else:
            seen_configs.add(config)
            added_at[config] = redist_cycles
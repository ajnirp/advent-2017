from math import sqrt

n = 347991#
# n = 14

# observation: the bottom right corner of every ring is (2k+1)^2
# where k is the ring number, starting with 0 for the innermost ring

lower = int(sqrt(n))
higher = lower + 2
higher_sq = higher * higher
diff = higher_sq - n
rem = diff % (lower + 1)
halflen = (lower+1)/2
if rem <= halflen:
    print(2*halflen - rem)
else:
    print(rem)
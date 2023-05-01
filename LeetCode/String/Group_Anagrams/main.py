from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

mp = defaultdict(list)

for val in strs:
    mp[tuple(sorted(val))].append(val)

print(mp.values())
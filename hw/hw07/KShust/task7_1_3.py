def count(s):
    counts = {}
    for i in s:
        counts[i] = counts.get(i, 0) + 1
    return counts

print(count("hello"))
import itertools


# Find the number of pairs in array.
def find_pairs(array):
    # count the number of unique items, divide by 2 to count pairs.
    return sum([len(list(group)) // 2 for key, group in itertools.groupby(sorted(array))])


n = 9
array = [10, 20, 20, 10, 10, 30, 50, 10, 20]

pairs = find_pairs(array)
print(pairs)

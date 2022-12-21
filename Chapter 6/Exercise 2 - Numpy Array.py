a = [20, 23, 82, 40, 32, 15, 67, 52]
even_indices = []

for i, number in enumerate(a):
    if number % 2 == 0:
        even_indices.append(i)

print(even_indices)  # Output: [0, 3, 4, 7]
sorted_a = sorted(a)
print(sorted_a)
sliced_a = a[3:]
print(sliced_a)
sliced_a = a[:4]
print(sliced_a)
sliced_a = a[-5:-2: -1]
print(sliced_a)
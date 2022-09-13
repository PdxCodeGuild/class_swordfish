xs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(xs)

for idx in range(2, len(xs), 3):
    if xs[idx] % 2 == 1:
        xs[idx] -= 1

print(xs)
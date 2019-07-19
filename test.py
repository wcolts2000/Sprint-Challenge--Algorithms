n = 6
sum = 0
for i in range(n):
    i += 1
    for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
            k += 1
            for l in range(k + 1, 10 + k):  # O(1)
                l += 1
                sum += 1
                print(sum)

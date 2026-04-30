def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def chinese_remainder(a, m):
    M = 1
    for mi in m:
        M *= mi

    result = 0

    for i in range(len(a)):
        Mi = M // m[i]
        yi = mod_inverse(Mi, m[i])
        result += a[i] * Mi * yi

    return result % M


a = [2, 3, 2]
m = [3, 5, 7]

x = chinese_remainder(a, m)

print("The smallest non-negative solution is:", x)
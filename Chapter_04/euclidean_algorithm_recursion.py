# Euclidean Algorithm
# With Recursion

print("Euclidean Algorithm\n")
print("Please input positive integers only.\n")
a = int(input("First Number: "))
b = int(input("Second Number: "))


def euclid(a, b):
    if a < 0:
        print("Negative Integers are not recognized by program.")
        return
    elif b < 0:
        print("Negative Integers are not recognized by program.")
        return
    elif a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        c = int(a % b)
        d = b
    elif a < b:
        c = int(b % a)
        d = a

    return euclid(d, c)


print("GCD = ", euclid(a, b))

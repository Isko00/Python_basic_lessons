def tri_recursion(k):
    print(k)
    k -= 1

    if k > 0:
        tri_recursion(k)


print("\n\nRecursion Example Results")
tri_recursion(6)


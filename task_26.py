def number(A, B):
    if B == 0:
        return 1
    return A ** B


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print(number(A, B))

      
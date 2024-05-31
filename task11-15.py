# task11
print("task11")
def SelectionSort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

A = [2, 8, 5, 3, 9, 4, 1]
print(SelectionSort(A))
# task 12
print("task12")
def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
    return A

A = [2, 8, 5, 3, 9, 4, 1]
print(InsertionSort(A))

# task13
print("task13")
def BubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = [2, 8, 5, 3, 9, 4, 1]
print(BubbleSort(A))
# task14

print("task14")

class NameTooLongError(Exception):
    pass

def check_name(name):
    if len(name) > 4:
        raise NameTooLongError("Name is too long!")

try:
    check_name("Jonathan")
except NameTooLongError:
    print("Name is too long!")

# task15
print("task15")

def plus_two(number):
    if not isinstance(number, (int, float)):
        print("Ожидаемый тип данных — число!")
        return
    return number + 2

print(plus_two(3))
print(plus_two("3"))

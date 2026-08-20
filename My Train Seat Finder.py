# Sorted list of train seats
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter seat number to find: "))

# -------------------------------
# Iterative Binary Search (O(log n))
# -------------------------------
low, high = 0, len(seats) - 1
found_iterative = False

while low <= high:
    mid = (low + high) // 2
    if seats[mid] == target:
        found_iterative = True
        break
    elif seats[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("Iterative Binary Search:", "Found" if found_iterative else "Not Found")

# -------------------------------
# Recursive Binary Search (O(log n))
# -------------------------------
def recursive_binary_search(seats, low, high, target):
    if low > high:
        return False
    mid = (low + high) // 2
    if seats[mid] == target:
        return True
    elif seats[mid] < target:
        return recursive_binary_search(seats, mid + 1, high, target)
    else:
        return recursive_binary_search(seats, low, mid - 1, target)

found_recursive = recursive_binary_search(seats, 0, len(seats) - 1, target)
print("Recursive Binary Search:", "Found" if found_recursive else "Not Found")

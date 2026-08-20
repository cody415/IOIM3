# Input quiz scores
scores = [45, 67, 89, 23, 67, 90]
target = 67
index = 2

# -------------------------------
# Direct Access (O(1))
# -------------------------------
print("Direct Access:", scores[index])

# -------------------------------
# Linear Search (O(n))
# -------------------------------
found = False
for score in scores:
    if score == target:
        found = True
        break
print("Linear Search:", "Found" if found else "Not Found")

# -------------------------------
# Pair Comparison (O(n^2))
# -------------------------------
duplicate = False
for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] == scores[j]:
            duplicate = True
            break
print("Pair Comparison:", "Duplicate Found" if duplicate else "No Duplicates")

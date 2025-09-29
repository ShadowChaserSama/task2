def halves_sums_equal(n):
    s = str(abs(int(n))) 
    L = len(s)

    if L % 2 == 0:  
        return "Sehv: cut reqem sayli eded daxil edilib!"

    mid = L // 2
    left = s[:mid]
    right = s[mid+1:]

    sum_left = sum(int(ch) for ch in left)
    sum_right = sum(int(ch) for ch in right)

    if sum_left == sum_right:
        return "Equal ✅"
    else:
        return "Not Equal ❌"

# Nümunələr:
print(halves_sums_equal(19091))   # Beredir (1+9=10, 9+1=10)
print(halves_sums_equal(14321))   # Beraber deyil (1+4=5, 2+1=3 → yox)
print(halves_sums_equal(123321))  # Sehv (çünki 6 rəqəmli)

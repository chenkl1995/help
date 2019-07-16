# === 2-dim list ===
l_2_err = [[]] * 3
l_2_err[0].append(-1)
print(l_2_err)

l_2 = [[] for _ in range(3)]
l_2[0].append(-1)
print(l_2)
print()


# === list to str ===
# int list
i = [1, 2, 3]
print(' '.join(str(i)))
print(' '.join([str(ii) for ii in i]))

# str list
s = ['1', '2', '3']
print(' '.join(s))
print()
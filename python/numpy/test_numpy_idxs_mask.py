import numpy as np

lbl = [1, 1, 2, 3, 3, 3, 6, 7, 8, 8, 9]
# a = np.asarray(a)
a = np.array(lbl)
print(a)
print()
np.random.shuffle(a)
print('a =', a)

sort_idx = np.argsort(a)
print(sort_idx.dtype, sort_idx.shape, sort_idx)
b = a[sort_idx]
print('b =', b)

_, unique_idx = np.unique(b, return_index=True)
print(unique_idx.dtype, unique_idx.shape, unique_idx)
c = b[unique_idx]
print('c =', c)

five_mask = c > 5
print(five_mask.dtype, five_mask.shape, five_mask)
d = c[five_mask]
print('d =', d)

eight_mask = d > 8
print(eight_mask.dtype, eight_mask.shape, eight_mask)
e = d[eight_mask]
print('e =', e)

for i in range(eight_mask.shape[0]):
    print(i)

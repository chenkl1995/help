import numpy as np

lbl = [1, 1, 2, 3, 3, 3, 6, 7, 8, 8, 9, 10]
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

five_mask = c > 6
print(five_mask.dtype, five_mask.shape, five_mask)
d = c[five_mask]
print('d =', d)

eight_mask = d > 8
print(eight_mask.dtype, eight_mask.shape, eight_mask)
e = d[eight_mask]
print('e =', e)

eight_mask_ = np.nonzero(eight_mask)[0]
print(eight_mask_)
five_mask_ = np.nonzero(five_mask)[0]
print(five_mask_)

for i, num in enumerate(e):
    print(num)
    print('e idx = ', i)

    d_idx = eight_mask_[i]
    print('d idx = ', d_idx)
    assert d[d_idx] == num

    c_idx = five_mask_[d_idx]
    print('c idx = ', c_idx)
    assert c[c_idx] == num

    b_idx = unique_idx[c_idx]
    print('b idx = ', b_idx)
    assert b[b_idx] == num

    a_idx = sort_idx[b_idx]
    print('a idx = ', a_idx)
    assert a[a_idx] == num

    print()

print(sort_idx[unique_idx[five_mask_[eight_mask_[range(len(e))]]]])

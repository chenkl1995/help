
i = int(123)
f = float(123.456)

'''
    :d
    :f
    :^ -- center align
    :< -- left align
    :> -- right align
'''
print( '{}'.format(i) )
print( '{:d}'.format(i) )
print( '{:6d}'.format(i) )
print()

print( '=' * 8 )
print( '{:^8d}'.format(i) )
print( '{:<8d}'.format(i) )
print( '{:>8d}'.format(i) )
print( '{:0=8d}'.format(i) )
print( '=' * 8 )
print()

print( '{}'.format(i) )
print( '{:f}'.format(i) )
print( '{:3f}'.format(i) )
print( '{:.3f}'.format(i) )
print()

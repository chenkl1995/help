import os.path as osp
import sys

# current file absolute path && filename
print(sys.argv[0])
print(osp.basename(sys.argv[0]))

print(__file__)
print(osp.basename(__file__))
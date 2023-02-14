from ctypes.wintypes import WORD
from distutils.archive_util import make_archive


def getFiboNbr(n, memorize={1:0,2:1}):
    if n in memorize:
        return memorize[n]
    else:
        memorize[n] = getFiboNbr(n - 1, memorize) + getFiboNbr(n - 2, memorize)
        return memorize[n]


output = getFiboNbr(3)
print(output)

"""
from pkg.mod_01 import func_01, func_02
from pkg.mod_02 import func_03, func_04

print(func_01())
print(func_02())
print(func_03())
print(func_04())
"""

import pkg

print(pkg.URL)
print(pkg.mod_01.func_01()) # Solo funciona porque se hicieron las importaciones al principio
                            # Para eso, se importa pkg desde __init__
                            # Se hace de esta forma para hacer la "importación" explicita
                            # y no generar choques de nombres
                            
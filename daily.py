import os
import random
from subprocess import call

ar = [(259, 'NO CHANCE'), (258, 'EN CLASE'), (253, 'FINALIZADO'),
      (257, 'EN CLASE'), (255, 'NO CHANCE'), (256, 'FINALIZADO'),
      (254, 'FINALIZADO'), (252, 'EN CLASE'), (251, 'NO CHANCE')]

ar = list(filter(lambda x: x[1] == 'FINALIZADO', ar))
print("Otra modificacion")
print(ar)
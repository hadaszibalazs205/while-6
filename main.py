'''
6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
'''
import random

oszthato_nullaval = []

meddig = 0

while meddig < 20:
  a = random.randint(1, 12)
  if a % 3 == 0:
    oszthato_nullaval.append(a)
    print(a)
  meddig += 1

print(f"Ennyi db 3-mal osztható szám keletkezett: {len(oszthato_nullaval)}")




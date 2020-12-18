import string
a = "BATTALION CHIEF, (FIRE DEPARTMENT)"
print(''.join([tu for tu in list(a) if tu not in string.punctuation]).split())

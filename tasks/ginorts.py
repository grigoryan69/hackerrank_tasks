import re
S = input()
series="[a-z]","[A-Z]","[13579]","[02468]"
print("".join(map(lambda x: "".join(sorted(re.findall(x, S))),series)))

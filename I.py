s = input()

s = s[:s.find('h') + 1] + s[s.find('h') + 1:s.rfind('h')]*2 + s[s.rfind('h'):]

print(s)
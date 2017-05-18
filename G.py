s = input()

i = s.index('h')
s1 = s[i+1:][::-1]
k = s1.index('h')
k = len(s) - k - 1

print(s[:i] + s[k+1:])

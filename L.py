s = input()

toUpper = ['h']

if 'h' in s:
    i = s.index('h')
    if 'h' in s[i+1:]:
        rs = s[i+1:][::-1]
        j = rs.index('h')
        j = len(s) - j
        
    

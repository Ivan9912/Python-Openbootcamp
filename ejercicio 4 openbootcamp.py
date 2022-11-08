list = []
for match in range (101):
    if match > 0:
        list.append (int(match))
    
reverseCount = sorted(list, reverse=True)
print(reverseCount)
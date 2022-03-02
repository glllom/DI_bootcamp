with open('nameslist.txt', 'r') as f:
    names = list(map(str.strip, f.readlines()))
    print(names)

with open('nameslist.txt', 'r') as f:
    print(f.readline(5))

with open('nameslist.txt', 'r') as f:
    print(f.read()[4])

with open('nameslist.txt', 'r') as f:
    print(f.read().split('\n'))

with open('nameslist.txt', 'r') as f:
    l = f.read().split('\n')
    print(f"Darth : {l.count('Darth')}")
    print(f"Lea : {l.count('Lea')}")
    print(f"Luke : {l.count('Luke')}")


with open('nameslist.txt', 'a') as f:
    f.write('\nGleb')


with open('nameslist.txt', 'r+') as f:
    l = f.read().split('\n')
    for i in range(len(l)):
        if l[i] == 'Luke':
            l[i] = 'Luke Skywalker'
    f.seek(0)
    f.write('\n'.join(l))


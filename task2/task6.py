from tabulate import tabulate
c = []
f = []
for i in range(0, 100, 10):
    c.append(i)
    f.append((i * 1.8) + 32)
    # print(f'{(i * 1.8) + 32}')
print(c)
print(f)
zipped = [list(t) for t in zip(c, f)]
print(zipped)

head = ['C', 'F']

print(tabulate(zipped, headers=head, tablefmt="grid"))
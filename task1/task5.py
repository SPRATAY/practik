img=[[' ']*13 for i in range(4)]
y=0
for x in range(13):
    img[y][x]='*'
    y+=(-1)**(x//3)
print(*[''.join(i) for i in img], sep='\n')
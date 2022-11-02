blue = "\u001b[44m"
white = "\u001b[47m"
red = "\u001b[41m"
print(blue +"\x20" * 3 + white + "\x20" * 3 + red +"\x20" * 3 )
print(blue +"\x20" * 3 + white + "\x20" * 3 + red +"\x20" * 3 )
print(blue +"\x20" * 3 + white + "\x20" * 3 + red +"\x20" * 3 )


black = "\u001b[40m"
white = "\u001b[47m"
n=int(input())
m=int(input())
a = [[white for i in range(n)] for j in range(m)]
for i in range(m):
  for j in range(n):
    if (i+j)%2==0:
      a[i][j] = black
for i in range(n):
  print('  '.join(e for e in a[i]))


n = 50
coord = [["\x20" for j in range(n)] for i in range(n)]

for i in range(n):
    coord[n-1][i] = "-"
    coord[i][n // 2] = "|"

for x in range(n):
    y = x**2
    if y < n:
        coord[-y][(n//2+x)] = "*"
        coord[-y][(n//2-x)] = "*"

coord[n-1][n-1] = ">"
coord[0][n//2] = "^"

for i in range(n):
    print("".join(e for e in coord[i]))


with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    big = 0
    small = 0
    z = -1
    for row in list(books)[1:]:
        year = row[6][:4]

        if int(year) <= 2014:
            small += 1
        else:
            big += 1

all = big + small

a = small * 100 // all
b = big * 100 // all + 1

print("До 2014    " + BLUE + '  ' * a + END + ' ' + str(a) + '%')
print()
print("После 2014 " + BLUE + '  ' * b + END + ' ' + str(b) + '%')
print()

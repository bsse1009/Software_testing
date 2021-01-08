test = [[2,3,7,8],[2,3,7,8],[2,3,7,8]]
out = []
tem = []
def f(j):
    if j == 4:
        j = 0
        return
    for i in range(3):
        f(j+1)
        tem.append(test[i][j])
    print(tem)
    tem.clear()

if __name__ == '__main__':
    f(0)
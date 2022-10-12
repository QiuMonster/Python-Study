
# end=" "意思是输出不换行 以空格代替换行

def jiujiu1(row):
    while row <= 9:
        col = 1
        while col <= row:
            print("%d*%d=%d" % (row, col, row * col), end=" ")
            col += 1
            pass
        print()
        row += 1
        pass

def jiujiu(row):
    while row >= 1:
        col = 1
        while col <= row:
            print("%d*%d=%d" % (row, col, row * col),end=" ")
            col += 1
            pass
        print()
        row -= 1
        pass

jiujiu1(1)
print()
jiujiu(9)

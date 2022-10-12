# 输出相邻像素中肤色像素所在的区域号
def print_region(self):
    for item in self.skin_map:
        if (item.id % self.width == 1):
            print()
        if (item.skin):
            print(item.region, " ", end='')  # 皮肤像素用 1 显示
        elif (not item.skin):
            print(0, " ", end='')  # 非皮肤像素用 0 表示
    print()


# 输出是皮肤的像素矩阵
def print_skin(self):
    for item in self.skin_map:
        if (item.id % self.width == 1):
            print()
        if (item.skin):
            print(1, " ", end='')  # 皮肤像素用 1 显示
        elif (not item.skin):
            print(0, " ", end='')  # 非皮肤像素用 0 表示
    print()


# 输出像素id矩阵
def print_id(self):
    for item in self.skin_map:
        if (item.id % self.width == 1):
            print()
        print(item.id, " ", end='')  # 实现不换行输出
    print()

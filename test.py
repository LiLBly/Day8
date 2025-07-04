import copy

a = [1, [2, 3]]
b = copy.copy(a)      # 浅拷贝
c = copy.deepcopy(a)  # 深拷贝
print(a)  # [1, [2, 3]]
print(b)  # [1, [2, 3]]  -> b 和 a
print(c)  # [1, [2, 3]]  -> c 和 a 完全独立

a[0] = 66
a[1][0] = 99
print(a)  # [66, [99, 3]] -> a 的第一层和第二层都被修改了
print(b)  # [1, [99, 3]]  -> 跟 a 共用了 [2,3] 那个内层列表
print(c)  # [1, [2, 3]]   -> 深拷贝出来的是独立的

import numpy as np

# 测试数组元素属性
ary = np.arange(1, 19)
print(ary, ary.shape)

# 修改ary的维度
ary.shape = (2, 9)
print(ary, ary.shape)
ary.shape = (2, 3, 3)
print(ary, ary.shape)

# 元素的数据类型
ary.shape = (2, 9)
print(ary, ary.dtype)
# ary.dtype = "float64"
# print(ary, ary.dtype)
ary = ary.astype('float32')
print(ary, ary.dtype)

# ValueError: When changing to a larger dtype, its size must be a divisor of the total size in bytes of the last axis of the array.
# ary.dtype = "int64"
# print(ary, ary.dtype)
# ....
# ary.dtype = "int32"
# print(ary, ary.dtype)

# ndarray 数组元素的个数
print(ary, ary.size, len(ary))

# 元素的索引
ary.shape = (2, 3, 3)
print(ary[0])
print(ary[0][0])
print(ary[0][0][0])
print(ary[0][1][1], ary[0, 1, 1])
# 迭代数组元素
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i, j, k])

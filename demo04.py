import numpy as np

data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 第一种设置dtype的方式
ary = np.array(data, dtype='U2,3int32,int32')
print(ary, ary[0][0])

# 第二种设置dtype的方式
ary = np.array(data, dtype=[('name', 'str', 2),
                            ('scores', 'int32', 3),
                            ('age', 'int32', 1)])
print(ary, ary[1]['scores'], ary.itemsize)
# itemsize : Length of one array element in bytes.
print('/////////////')
# 第三种设置dtype的方式
ary = np.array(data, dtype={'names': ['name', 'scores', 'age'],
                            'formats': ['U3', '3int32', 'int32']})
print(ary[0]['name'], ":", ary[0]['scores'], ":", ary.itemsize)
print('**********')
# 第四种设置dtype的方式
ary = np.array(data, dtype={'name': ('U3', 0),
                            'scores': ('3int32', 16),
                            'age': ('int32', 28)})
print(ary[0]['scores'], ary[0]['age'], ary.itemsize)
print('============')
f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01', '2011-02-01'])
dates = f.astype('M8[D]')
print(dates, dates.dtype)
print(dates[-1] - dates[0])
dates = dates.astype('int32')
print(dates,dates.dtype)

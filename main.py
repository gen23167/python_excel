from datetime import datetime
import time
import json

import pandas as pd

from myPack import *

class Person:
    def hello(self):
        print("hello")

person = Person()
person.hello()

num = 200

def testA():
    print(num)

testA()

def testB():
    global num
    num = 500
    print(num)

testB()

print(num)

list = [['ab',1],2.3]
print(list)
for i in list:
    print(i)

print(list[1]) #
print(list[-2]) # 反向元素
print(list.index(2.3)) # 获取元素索引值

list[list.index(2.3)] = 3 # 按索引值改元素值

list.insert(1, "bb") # 指定位置后面加新元素
for i in list:
    print(i)

list.append(22) # 加新元素
for i in list:
    print(i)



list2 = ["a", "b"]
list.extend(list2)# 将list2元素合并到list
for i in list:
    print(i)

# del list[list.index("a")] # 删除元素 方法1
popEl = list.pop(list.index("a")) # 删除元素 方法2
for i in list:
    print(i)
print("list.pop的元素: " + popEl)

print(len(list)) # 列表有几个元素
print([1,1,2,3].count(1)) # 统计指定元素的个数

list.remove("b") # 删除元素 方法3 删除指定元素
for i in list:
    print(i)

list.clear() # 清空列表
print(len(list))

# 元组定义
tp1 = (1,)
tp2 = tuple()
tp3 = (1,2,3.2) # 元组
print(len(tp3))
print(f"tp3最大元素: {max(tp3)}")

for i in tp1:
    print(i)

print(tp3[2])

print(" 123 ".strip()) # 移除首尾空格
print("1231".strip("1")) # 移除首尾指定字符

str = "123456"
index = 0
while index < len(str):
    print(str[index])
    index += 1

for i in "a,b,c,".split(","):
    print(i)

print("a,b,c,".replace(",", "|"))

print("abc".count("a"))
print(len("abc"))

print("a,b,c,".split(",")[::-1]) # 列表倒序
print("a,b,c,d,e,f".split(",")[3:6]) # 列表分割

for i in "a,b,c,d,e,f".split(",")[3:6]:
    print(i)

print("set----------")
# set 定义
set1 = {"a","b","a"}
set2 = set()
for i in set1:
    print(i)

print(set1)
print(f"{set1}")

set1.add("b")
set1.add("d")
print(set1)

set3 = {1,2}
set4 = {1,3,4}
set5 = set3.difference(set4) # 取set3有但set5无的元素
print(set5)

set3.difference_update(set4) # 取set3有但set5无的元素, 结果更新到set3
print(set3)

set6 = {1,2,3}
set7 = {1,4,5}
print(set6.union(set7)) # 合集

list = [1,2,3]
list.append(4)
print(f"list: {list}")

dict1 = {"a":1,"b":2}
print(dict1)
print(dict1["a"])
dict1["a"] = 3 # 修改值
print(dict1["a"])

dict1["c"] = "33"

print(dict1.keys())
print(dict1.values())

print("a">"A")

# 多返回值
def retTest():
    return 1,2,3

a,b,c = retTest()
print(a)
print(b)
print(c)

# 不定长参数
def multiParam(*args):
    print(args)

multiParam("a", "b")

# **    字典格式不定长参数
def multiParam(**kwargs):
    print(kwargs)

multiParam(name="a", id="b")

# 使用默认值的参数位置一定要在没默认值参数的后面
def defaultParam(age, name="ben"):
    print(f"name:{name}, age:{age}")

defaultParam(age=13)

# 函数作为参数传递
def test_func(compute):
    print(compute(1, 2))

def compute(x, y):
    return x + y

test_func(compute)

# lambda 关键字, 只能用一次
test_func(lambda x, y: x + y)


# io read
f = open("1.txt", "r", encoding="UTF-8")
print(f"type 读取 1.txt结果类型: {type(f)}")
print(f"readlines 读取 1.txt全部内容: {f.readlines()}")

f = open("1.txt", "r", encoding="UTF-8")
print(f"read 读取 1.txt全部内容: {f.read()}")

f = open("1.txt", "r", encoding="UTF-8")
for line in open("1.txt", "r"):
    print(line)
f.close()

with open("1.txt", "r", encoding="UTF-8") as f:
    print(f"with open readlines 读取 1.txt全部内容: {f.readlines()}")


with open("1.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"with open read 读取 for 1.txt: {line}")


# 写文件
# f = open("write.txt", "w", encoding="UTF-8")
# f.write("hello world %s" % datetime.datetime.now())
#f.flush() # 后面有调close(), 就不用写这个
# f.close()

# 追加写入文件
f = open("write.txt", "a", encoding="UTF-8")
f.write("\nhello world %s" % datetime.now())
f.close()


fr = open("1.txt", "r", encoding="UTF-8")
fw = open("1.txt.bak", "w", encoding="UTF-8")

# print(len("a,b".split(",")) and True)
for line in fr:
    line = line.strip()
    arr = line.split(",")
    if len(arr) >= 5 and arr[4] == "测试":
        continue
    fw.write(line)
    fw.write("\n")
fr.close()
fw.close()

# 捕获异常
try:
    # 1/0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("error msg: ")
    print(e)

try:
    # 1/0
    print(name)
except Exception as e:
    print("error msg: ")
    print(e)
else:
    print("无异常")
finally:
    print("结束")

my_pack_a.print_pack()
my_pack_b.print_pack()


data = [{"name":"ben张", "age": 16},{"name":"alpha", "age": 15}]
json_str = json.dumps(data) # 中文自动转码
json_str_chs = json.dumps(data, ensure_ascii=False) # 中文不转码, 才显示正常
print(type(json_str))
print(type(json_str_chs))
print(json_str)
print(json_str_chs)

json1 = json.loads(json_str_chs)
print(type(json1))
print(json1)

# 创建示例DataFrame
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar'],
    'B': [1, 2, 1, 2],
    'C': [1, 2, 3, 4]
})

# 去重
df_unique = df.drop_duplicates()
print(df_unique)


# 打印日期时间
dt = datetime.now()
print(dt)
print(f"datetime转字串 {dt.strftime('%Y-%m-%d %H:%M:%S')}")

timestamp = dt.timestamp()
print(f"timestamp: %s" % (timestamp))
# 睡眠2秒
# time.sleep(2)
# print(datetime.datetime.now())

timestamp_str = 1740292626
local_time = time.localtime(1740292626)
print(f"timestamp转local_time {local_time}")

datetime_var = datetime.fromtimestamp(timestamp_str)
print(f"timestamp转datetime {datetime_var}")
# YEAR = local_time

year = datetime_var.strftime("%Y")
print(f"datetime获取 year: {year}")

month = datetime_var.strftime("%m")
print(f"datetime获取 month: {month}")


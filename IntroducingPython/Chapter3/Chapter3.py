
# coding: utf-8

# In[17]:

#List
empty_list = [ ]
weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五']
type(empty_list)


# In[16]:

type(weekdays)


# In[18]:

#Tuple
roles = ('甘道夫', '亞拉岡', '索倫', '勒苟拉斯', '亞玟')
type(roles)


# In[21]:

weekdays[0] = '星期一猴子穿新衣'
weekdays


# In[1]:

roles[0] = '甘道夫是魔法師'
roles


# In[2]:

list('中文')


# In[8]:

a_tuple = ("一", "二", "三")
list(a_tuple)


# In[14]:

birthday = "1/6/2015"
birthday.split('/')


# In[16]:

birthday = "a/b//c/d//e"
birthday.split('//')


# In[17]:

a = ['中國','美國','英國']
a[0] 


# In[20]:

a[-1]


# In[23]:

a = [1, "jerry", 2, "吳老師"]
a[0]


# In[49]:

a = [[[1, "jerry", 2, "吳老師"], "台灣科大"], "台灣"]
a[0][0][1]


# In[33]:

a = [1, "jerry", 2, "吳老師"]
a[0]


# In[36]:

a[0] = 's'
a


# In[57]:

a.append("3")
a


# In[61]:

areas = ["大安區", "士林區", "文山區"]
names = [1, "jerry", 2, "吳老師"]
areas.extend(names)
areas


# In[63]:

areas = ["大安區", "士林區", "文山區"]
names = [1, "jerry", 2, "吳老師"]
areas += names
areas


# In[65]:

areas = ["大安區", "士林區", "文山區"]
names = [1, "jerry", 2, "吳老師"]
areas.append(names)
areas


# In[77]:

areas = ["大安區", "士林區", "文山區"]
areas.insert(2, "內湖區")
areas


# In[78]:

del areas[-2]
areas


# In[85]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區"]
areas.remove("大安區")
areas


# In[94]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區"]
areas.pop(1)
areas


# In[96]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區"]
areas.index("信義區")


# In[99]:

"新店區" in areas


# In[100]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區", "信義區"]
areas.count('信義區')


# In[110]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區"]
new_areas = ','.join(areas)
type(new_areas)


# In[115]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區"]
new_areas = ','.join(areas)
type(areas)


# In[129]:

areas = ["大安區", "士林區", "文山區", "大同區", "信義區"]
separator = "*"
joined = separator.join(areas)
joined


# In[130]:

separatored = joined.split(separator)
separatored


# In[131]:

areas


# In[132]:

separatored == areas


# In[134]:

number = [5,3,42,35,99]
sorted_number = sorted(number)
sorted_number


# In[135]:

number


# In[139]:

number = [5,3,42,35,99]
sorted(number)


# In[140]:

number = [5,3,42,35,99]
number.sort()
number


# In[145]:

number = [5,3,42,35,99]
number.sort(reverse=True)
number


# In[146]:

number = [5,3,42,35,99]
len(number)


# In[148]:

a = [1,2,3]
a


# In[149]:

b = a
b


# In[151]:

a[0] = 'new'
a


# In[152]:

b


# In[155]:

a = ["神奇", "的", "list", "功能"]
b = a
c = b


# In[156]:

b


# In[157]:

c


# In[158]:

a[0] = "有夠神奇"


# In[159]:

a


# In[160]:

b


# In[162]:

c


# In[164]:

a = ["試試", "神奇", "list的copy", "功能"]
a


# In[165]:

b = a.copy()


# In[166]:

b


# In[167]:

c = list(a)


# In[168]:

c


# In[171]:

d = a[:]
d


# In[175]:

a[0] = "Try"
a


# In[176]:

b


# In[177]:

b = a.copy()
b


# In[1]:

#Tuple
empty_tuple = ()
empty_tuple


# In[2]:

roles = ('甘道夫', '亞拉岡', '索倫', '勒苟拉斯', '亞玟')
type(roles)
roles[0] = '甘道夫是魔法師'
roles


# In[7]:

roles = ('甘道夫', '亞拉岡', '索倫', '勒苟拉斯', '亞玟')
a,b,c,d,e = roles
a


# In[8]:

password = "sdlkpekcp"
test_password = "aaabbb"
password, test_password = test_password, password
password


# In[9]:

test_password


# In[11]:

roles = ['甘道夫', '亞拉岡', '索倫', '勒苟拉斯', '亞玟']
roles = tuple(roles)
type(roles)


# In[14]:

#dictionary
empty_dict = {}
empty_dict


# In[17]:

class_ntust = {
    "number" : "1059999",
    "name" : "jerry"
    }
class_ntust


# In[19]:

school = [["班級","甲班"],["姓名","甘道夫"],["學號","110999"]]
dict(school)


# In[20]:

school = [("班級","甲班"),("姓名","甘道夫"),("學號","110999")]
dict(school)


# In[23]:

school = ["中文","cd","ef"]
dict(school)


# In[36]:

class_ntust = {
    "member1" : "甘道夫",
    "member2" : "亞拉岡",
    "member3" : "索倫",
    }
class_ntust


# In[29]:

class_ntust["member1"] = "亞玟"
class_ntust


# In[30]:

class_ntust["member1"] = "甘道夫"
class_ntust


# In[53]:

class_ntust = {
    "member1" : "甘道夫",
    "member2" : "亞拉岡",
    "member3" : "索倫",
    }


class_ntust2 = {
    "member4" : "金鋼狼",
    "member5" : "暴風女",
    "member6" : "X教授",
    }
class_ntust




# In[38]:

class_ntust2


# In[54]:

class_ntust.update(class_ntust2)
class_ntust


# In[44]:

first = {"a":1, "b":2}
second = {"b":"cat"}
first.update(second)
first


# In[55]:

del class_ntust["member1"]
class_ntust


# In[57]:

class_ntust.clear()
class_ntust


# In[61]:

class_ntust = {
    "member1" : "甘道夫",
    "member2" : "亞拉岡",
    "member3" : "索倫",
    }
"member1" in class_ntust


# In[63]:

class_ntust["member1"]


# In[64]:

class_ntust["member11"]


# In[65]:

"member1" in class_ntust


# In[66]:

"member11" in class_ntust


# In[67]:

class_ntust.get("member1")


# In[72]:

class_ntust.get("member11", "號碼錯誤哦!")


# In[76]:

class_ntust.keys()


# In[77]:

class_ntust.values()


# In[78]:

class_ntust.items()


# In[79]:

class_ntust


# In[81]:

class_ntust_new = class_ntust
class_ntust_new


# In[85]:

class_ntust["member1"] = "金庸"
class_ntust


# In[86]:

class_ntust_new


# In[88]:

class_ntust = {
    "member1" : "甘道夫",
    "member2" : "亞拉岡",
    "member3" : "索倫",
    }
class_ntust


# In[90]:

class_ntust_new = class_ntust.copy()
class_ntust_new


# In[91]:

class_ntust["member1"] = "笑傲江湖"
class_ntust


# In[92]:

class_ntust_new


# In[93]:

#set
empty_set = set()
empty_set


# In[94]:

even_numbers = {0,2,3,4,5}
even_numbers


# In[95]:

#tuple ,
#list []
#dictionary {:}
#set set() or {}


# In[97]:

set("中文試試")


# In[98]:

set(["甘道夫","亞拉岡","亞玟","咕嚕","索倫"])


# In[99]:

set(("甘道夫","亞拉岡","亞玟","咕嚕","索倫"))


# In[101]:

set({"member":"甘道夫","member2":"亞拉岡"})


# In[103]:

drinks = {
    "item1" : {"珍珠奶茶","紅茶"},
    "item2" : {"烏龍奶茶","烏龍茶"},
    "item3" : {"蜂蜜紅茶","紅茶"},
   }


# In[111]:

for name, contents in drinks.items():
    if "紅茶" in contents:
        print(name)


# In[114]:

for name, contents in drinks.items():
    if "紅茶" in contents and not ("珍珠奶茶" in contents):
        print(name)


# In[117]:

for name, contents in drinks.items():
    if contents & {"紅茶"} :
        print(name)


# In[119]:

for name, contents in drinks.items():
    if "紅茶" in contents and not contents & {"蜂蜜紅茶"} :
        print(name)


# In[123]:

a = {1,2}
b = {2,3}
type(a)


# In[124]:

a&b


# In[125]:

a.intersection(b)


# In[126]:

a|b


# In[127]:

a.union(b)


# In[133]:

a - b


# In[129]:

a^b


# In[131]:

b^a


# In[138]:

rings_list = ["甘道夫","亞拉岡","亞玟","咕嚕","索倫"]
type(rings_list)


# In[145]:

rings_tuple = "甘道夫","亞拉岡","亞玟","咕嚕","索倫"
type(rings_tuple)


# In[141]:

rings_dict = {"member1":"甘道夫","member2":"咕嚕"}
type(rings_dict)


# In[152]:

rings_set = {"甘道夫","亞拉岡","亞玟","咕嚕","索倫"}
type(rings_set)


# In[143]:

rings_list[2]


# In[146]:

rings_tuple[2]


# In[150]:

rings_dict["member1"]


# In[155]:

"甘道夫" in rings_set


# In[157]:

rings = ["甘道夫","亞拉岡","亞玟","咕嚕","索倫"]
potter = ["哈利波特","妙麗","榮恩","鄧不利多"]
tuple_of_lists = rings, potter
tuple_of_lists


# In[158]:

list_of_lists = [rings, potter]
list_of_lists


# In[161]:

dict_of_lists = {"book1":potter,"book2":rings}
dict_of_lists


# In[ ]:




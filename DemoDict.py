# DemoDict.py
phone = {"kim":"1111","lee":"2222","park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
print("park" in phone)
print("kang" not in phone)

p = phone
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone) == id(p))


device = {"iph":5, "ipd":10}
device["mbk"] = 15
device["iph"] = 6
print(device)

del device["iph"]
print(device)

print("----------items----------")
for item in device.items():
    print(item)
print("----------keys----------")
for item in device.keys():
    print(item)
print("----------values----------")
for item in device.values():
    print(item)

print("----------자료형 bool 판단----------")
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1,2,3]))
print("----------논리식----------")
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and True)
print(True and True and False)
print(True or False or False)
print(5 / 2)
print(5 // 2)
print(5 % 2)




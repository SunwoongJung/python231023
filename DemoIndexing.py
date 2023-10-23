#DemoIndexing.py


x = 100
y = 3.14

print(type(x))
print(type(y))

strA = "Python is Very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))

lst = [1,2,3]
for item in lst:
    print(item)


print("0 : " + strA[0])
print("1 : " + strA[1])
print("0:6 : " + strA[0:6])
print(":6 : " + strA[:6])
print("-3: : " + strA[-3:])
print("-8: : " + strA[-8:])
print(": : " + strA[:])

strC = """이 문자열은
다중 라인으로
저장합니다."""

print(strC)
print(("이 문자열은 \t를 출력합니다."))

colors = ["red", "blue", "greem"]
print (type(colors))
print(colors)
colors.append("yellow")
print(colors)
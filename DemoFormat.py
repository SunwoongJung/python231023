# Formatting 예제

for x in range(1,6):
    print (x, "*", x, "=", x*x)

print ("---오른쪽 정렬---")
for x in range(1,6):
    print (x, "*", x, "=", str(x*x).rjust(3))

print ("---0을 출력---")
for x in range(1,6):
    print (x, "*", x, "=", str(x*x).zfill(5))

for i in range(1,11):
    url = "http://www.multicampus.com/?page=" + 1
    print(url)

print("{0:,}".format(15000))
print("{0:e}".format(15000))
print("{0:f}".format(15000))
print("{0:.2f}".format(15000))

f = open("demo.txt", "wt", encoding="utf-8")
f.write("1st\n2nd\n3rd")
f.close()

f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()


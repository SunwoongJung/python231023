# func2.py
# 스코핑룰 (LGB 규칙)

x = 1
def func1(a):
    return a+x

# 호출
print(func1(1))

def func2(a):
    x = 5
    return a+x

# 호출
print (func2(1))

# 기본값이 있는 경우
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ':' + port
    return strURL

print(connectURI("multi.com", "80")) 
print(connectURI(port="8080", server="multi.com")) 


def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))

g = lambda x,y : x*y
print (g(3,4))
print((lambda x:x*x(3)))
print (globals())


# DemoSetTuple.py

a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


print("---Tuple형식---")
tp = (1,2,3)
print(tp)
print(len(tp))
print(tp[0]) 

tp1 = (1, "김유신", "d", "vava")

try :
    print("id:%s, name %s" % tp1) # %s --> string
except:
    print("오류발생")

tp1 = ("ㅁㅁ", "김유신", "d", "vava")


def calc(a,b):
    """
    이 함수는 2개의 숫자를 입력받아서 
    덧셈과 곱셈을 하는 함수 입니다ㅣ 
    """
    return a+b, a*b # 반환형이 무조건 tuple?

print(calc(3,4))

a = calc(3,4)
print(a)
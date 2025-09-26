#제어문 선택문 if 반복문 forwhile

#for문실습
#1. 문자열을 이용한 반목문
'''
hi = "안녕하세요 반갑습니다"
for ch in  hi:
    print(ch,end='')

korea = "사랑하는 우리나라 대한민국"
count = 0
for i in korea:
    print(i)

korea = "사랑하는 우리나라 대한민국"
count = 0
for i in korea:
    print(i,end='')
    count = count+1
    print(count)

korea = "나는 인평자동차고등학교 AI과 김진성입니다"
for i in korea:
    if i==' ':
        print()
    else:
            print(i,end='')


#2. range() 반목문
for i in range (10):
    print("안녕",end='')
print("끝")

#100까지의 수 중 2의 배수 출력
for i in range (0,101,3):
    print(i)

for i in range (1,101):
    print(i,end=' ')
    if i % 10 == 0:
        print( )

#for문을 이용하여 23부터 40 까지 출력하시오
for i in range(23,41):
    print(i)

#for문을 이용하여 97부터 77 까지 출력하시오
for i in range(97,76,-1):
    print(i)
'''
import  turtle
'''
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
'''
#원하는 다각형 그리는프로그램
n = int(input("몇각형을그릴까요?: "))
for i in range(n):
        turtle.forward(100)
        turtle.left(360/n)



















































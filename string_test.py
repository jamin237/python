#print("배규찬")
#print("안녕하세요")
#print(5)
#name = input("당신의 이름을 입력하세요:")
#print("당신의 이름은", name, "입니다")

#height = int(input("당신의 키를 입력하세요: "))
#weight = int(input("당신의 몸무게를 입력하세요: "))
#mbi =weight/(height*height)*10000

#print("당신의 비만도는", mbi, "입니다")
#print(type(height))
#print(type(weight))
#print(type(mbi))

import turtle
turtle.shape("turtle")


#오각형 그리기
turtle.color('green')
turtle.forward(150)
turtle.left(72)
turtle.forward(150)
turtle.left(72)
turtle.forward(150)
turtle.left(72)
turtle.forward(150)
turtle.left(72)
turtle.forward(150)
turtle.left(72)
#사각형 그리기
turtle.color('blue')
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
#삼각형 그리기
turtle.color('red')
turtle.begin_fill()
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.end_fill()
'''
turtle.color('green', 'pink')
turtle.pensize(5)
turtle.begin_fill()
for i in range(5):
 turtle.forward(150)
 turtle.right(144)
turtle.end_fill()
turtle.done'''


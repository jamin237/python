import keyword
import calendar
import datetime

#print(keyword.kwlist)
#print(calendar.month(2009, 8))
today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second) 

#입출력 복습
"""
#비만도(bmI) 구하기 몸무게/(키의제곱)*10000

height = int(input("키를 입력하세요:"))
weight = int(input("몸무게를 입력하세요:"))
bmi = weight/(pow(height**2))+*10000
print("당신의 비만도는",{round(bmi)},"입니다")
print("당신의 비만도는",{round(bmi)},"입니다")

#반올림 round()
pi = 3.6451
print(round(pi,  1))
print(round(pi, 2))


#사칙연산 계산기 만들기
num1 = int(input("첫번째 값 입력 받기"))
num2 =  int(input("두번째 값 입력 받기"))

add_result =  num1 + num2
sub_result  = num1 -num2
mul_result = num1 *num2
div_result = num1 /num2

print(f"덧셈결과:{add_result}입니다.")
print(f"뺄셈결과:{sub_result}입니다.")
print(f"곱셈결과:{mul_result}입니다.")
print(f"나눗셈결과:{round(div_result)}입니다.")
"""
#변수


























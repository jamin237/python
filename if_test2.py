#반올림 round() 포매팅
'''
print(round(5.5795,2)) #5.58
print(round(5.5295,1)) #5.5
print(round(5.5795,0))  #6.0
print(round(5.5795,-1)) #10
print(round(5.5795)) #6
a = round(5.5295)
b = round(5.5795,0) 
print(type(a)) #int
print(type(b)) #float

#포메팅
print("{:.1f}".format(3.5289))
print("{:.0f}".format(3.5289))
print("{:.3f}".format(3.5289))

print("{0}과 {0}".format(3.5555,3.7777))
print("{0}과 {1}".format(3.5555,3.7777))

print("{:.2f}과 {:.1f}".format(3.5555,3.7777))
print("{1:.1f}과 {0:.2f}".format(3.5555,3.7777))

a=3
b=8
if a>=b:
    print(a+b)
else:
    print(a*b)

#if실습
#중국집 메뉴 선택 조건

money = int(input("가지고 있는 돈은  얼마인가요?"))

if money >= 20000:
    print("탕수육 먹어요")
elif money >= 10000:
    print("쟁반짜장 먹어요")
elif money >= 8000:
    print("해물짬뽕 어때")
elif money >= 6000:
    print("짜장면 먹지뭐" )
else:
    print("단무지나 먹어야겠다")
'''

scores = [85, 92, 78, 95, 88]

print("입력된 점수: ",scores) #리스트변수에 입력돤 점수 출력
print(f"전체학생수: {len(scores)}명") #전체 학생수 출력
if len(scores) > 0:
    max_scores= max(scores) #최고 점수 구하기
    min_scores= min(scores) #최저 점수 구하기
    tot_scores= sum(scores) #점수의 총합 구하기
    avg_scores= sum(scores)/len(scores) #점수의 평균 구하기
    print(f"최고 점수: {max_scores}점")
    print(f"최저 점수: {min_scores}점")
    print(f"총합 점수: {tot_scores}점")
    print("평균 점수:"  "{:.2f}".format (avg_scores))
else:
    print("입력된 점수가 없습니다.")




















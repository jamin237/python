# 출력 포매팅 표준함수

profile="""
안녕하세요
 저는 인평자동차고등학교
 ai 소프트웨어과
 1학년2반 김진성입니다.
"""
"""
print(profile)
print("김진성")
print("나의소개:"+profile)
print("나의나이:",age)
print("내이름은" + name+"이고 내소개는\""+ profile+"\"이야")
print("내이름은" , name,"이고 내소개는\"", profile,"\"이야")

#문자열 포매팅
name = "김진성"
age = 17
print("이름:"+ name+ " 나이: ", age)
print("이름:", name, "나이: ", age)
print("이름: %s 나이: %d"%(name,age))
print("이름: {} 나이: {}".format(name,age))
print(f"이름: {name} 나이: {age}")

a = 11
print(a)
print("%d는 16진수로%x"%(a,a))
"""
name = "김 진 성!!"
print(len(name))
print(len(profile))
number = [1,5,-2,0,6]
print("최대값은",max(number)) #max()최대값 구하기
print("최소값은",min(number)) #min()최소값 구하기
print("합계는", sum(number))  #sum()합계 구하기
print("평균은",  sum(number)/len(number)) #평균 구하기
#pow()
print(pow(5,9)) #5**9
print(5**9)

a = "I Love Python"
print(a.lower())  # 소문자로 변환
print(a.upper())  # 대문자로 변환




















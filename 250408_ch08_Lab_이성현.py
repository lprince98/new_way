############## Chapter 08 ##################
######### Lab ########
## 1 BMI 계산기
def bmi(mass, height):
    bmi_cal = (mass / (height ** 2)) *10000
    return bmi_cal
answer = bmi(int(input('몸무게를 kg 단위로 입력하세요: ')), int(input('키를 cm단위로 입력하세요: ')))
print('당신의 BMI는 %f입니다.' % answer)
if answer < 18.5:
    print('당신은 저체중입니다.')
elif answer >= 18.5 and answer < 23:
    print('당신은 정상입니다.')
elif answer >= 23 and answer < 25:
    print('당신은 과체중입니다.')
elif answer >= 25 and answer < 30:
    print('당신은 경도비만입니다.')
else:
    print('당신은 고도비만입니다.')

## 2 환전 계산기
def exchange_money(kor_money, rate):
    exchange = kor_money / rate
    return exchange
rate_nation = {'미국':1481.40,'일본':1006.42,'유로':1616.80,'중국':201.23,'영국':1887.22}

korea_mon = int(input('환전 금액(원)을 입력하세요:'))
nation = input('국가를 입력하세요:')
result = exchange_money(korea_mon, rate_nation[nation])

print('%d원은 %f 단위입니다.'% (korea_mon, result))


    
    

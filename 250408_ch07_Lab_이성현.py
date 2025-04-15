############### Ch07 List ##########
#### Lab exam #####
## 1 주기율표를 외워보자
periodic_table = []

for i in range(4):
    periodic_table = input('주기율표 구절을 입력하시오:')
    periodic_table.append(periodic_table)
    
print(periodic_table)

## 오늘의 명언
import random

proverb_1 = ['멈추지 않는 한, 얼마나 천천히 가는지는 중요하지 않다.']
proverb_2 = ['끈기는 긴 경주가 아니라, 짧은 경주를 계속해서 이어가는 것이다.']
proverb_3 = ['일곱 번 넘어져도 여덟 번째엔 일어서라.']
proverb_4 = ['산을 옮기는 사람도 작은 돌부터 옮긴다.']
proverb_5 = ['인생의 많은 실패는 성공에 얼마나 가까웠는지를 모른 채 포기한 사람들에게서 온다.']
proverb_6 = ['에너지와 끈기는 모든 것을 이긴다.']
proverb_7 = ['끈기를 통해 많은 이들이 실패할 것 같던 상황에서 성공을 얻는다.']
proverb_8 = ['성공은 대부분, 다른 사람들이 포기한 후에도 붙잡고 있는 데서 나온다.']
proverb_9 = ['인내와 끈기는 어려움을 사라지게 하고 장애물을 없애는 마법 같은 힘이 있다.']
proverb_10 = ['성공한 사람과 그렇지 못한 사람을 나누는 결정적인 요인 중 절반은 순수한 끈기다.']

day_prov = [proverb_1,proverb_2,proverb_3,proverb_4,proverb_5,proverb_6,proverb_7,proverb_8,proverb_9,proverb_10]
day_rand = random.randint(0,9)
print('##########################','\n','#### 오늘의 명언 ####','\n',day_prov[day_rand] )

# ## 습도 구하기
temperature = [0,10,20,30]
vapor = [4.8,9.4,17.3,30.4]
cur_hum = float(input('현재 수증기량:'))
cur_tem = float(input('현재 온도는:'))

if cur_tem in temperature:
    cal_hum = (cur_hum/vapor[temperature.index(cur_tem)])*100
print('현재 습도는 %s' %cal_hum)

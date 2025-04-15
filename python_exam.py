############ Chapter 12 #########
######### Additional exam #######
## 1 구구단
# num = int(input('구구단:'))

# for i in range(num,num+1):
#     for j in range(1,20):
#         cal = i * j
#         print('%d 곱하기 %d 는 %d'% (i,j,cal))
        
## 2 3과 5의 배수를 모두 더하기
num = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
       num +=i 
print(num)        
   
## 3      
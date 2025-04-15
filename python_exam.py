############ Chapter 12 #########
######### Additional exam #######
## 1 구구단
# num = int(input('구구단:'))

# for i in range(num,num+1):
#     for j in range(1,20):
#         cal = i * j
#         print('%d 곱하기 %d 는 %d'% (i,j,cal))
        
## 2 3과 5의 배수를 모두 더하기
# num = 0
# for i in range(1, 1000):
#     if i%3 == 0 or i%5 == 0:
#        num +=i 
# print(num)        
   
## 3 게시판 페이징하기
# def get_total_page(num, page):
#     if num < page:
#         result = num//page + 1
#         return result
#     else:
#         result = num//page + 1
#         return result

# num = int(input('게시물의 총 개수:'))
# page = int(input('한 페이지당 게시물 수:'))
# print('총 페이지 수:', get_total_page(num, page))

## 4 간단한 메모장 만들기
import sys

option = sys.argv[0]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)   
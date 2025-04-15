########### Chapter 09 ######## 
####### Additional exam ######
## 1 중복요소 제거
a = [80,20,20,30,60,30]
set_a = set(a)
sort_a = sorted(set_a)
print(sort_a)

## 2
dict = {}
result = {x: x**2 for x in range(1,11)}
print(result)

## 3 
d = {"Apple": 1, "Banana": 2, "Grape": 3} 

for k,v in d.items():
    print('{} -> {}'.format(k,v))

## 4 
sent_1 = input('첫 번째 문자열:')
sent_2 = input('두 번째 문자열:')

incl_sent = set(sent_1) & set(sent_2)
print('모두 포함된 글자:',incl_sent)

## 5 
set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {30, 40, 50, 60, 70, 80}

incl_set = set(set_1) & set(set_2)
only_set_1 = set_1 - incl_set
only_set_2 = set_2 - incl_set
print('어느 한 쪽에만 있는 요소들:',only_set_1, only_set_2)


    
##################### Chapter 10 #############
############ Lab exam ###########
## 1
infile = open('D:\\phones.txt','r',encoding = 'utf-8')
text = infile.read()
outfile = open('D:\\temp2.txt','w',encoding = 'utf-8')
out_text = outfile.write(text)

infile.close()
outfile.close()

## 2
infile = open(r'C:\Users\blues\Python\exam\text\input.txt','r')
outfile = open(r'C:\Users\blues\Python\exam\text\output.txt','w')
text = infile.read().split()

text_dic = {}
count = 0 
for i in text:
    text_strip = i.rstrip().lower().strip(',').strip('.')
    if text_strip in text_dic:
        text_dic[text_strip] += 1
        count += 1
    else: 
        text_dic[text_strip] = 1
        count += 1

for key in sorted(text_dic.keys()):
    result = key + '' + str(text_dic[key]) + '\n'
    outfile.write(result)

outfile.close()
infile.close()

## 3 
import csv
file_csv = open(r'C:\Users\blues\Python\exam\text\rn_20250414001422.csv','r')
data = csv.reader(file_csv)
sum = 0
count = 0

for line in data:
    count += 1
    sum += float(line[2])

print(line[1],'1980년 2월 28일부터 2025년 04월 12일까지의 총강수량은:', sum)
print(line[1],'1980년 2월 28일부터 2025년 04월 12일까지의 평균 강수량은:', sum/count)

file_csv.close()

## 4 
import random

infile = open(r'C:\Users\blues\Python\exam\text\hangman.txt','r')
text = infile.readlines()
choice_text = random.choice(text).rstrip()
text_list = list(choice_text)
final = list('_' * len(text_list))
trial = 10

for c in range(trial+1):
    a = 0
    answer = input('단어를 추측하세요:')
    for i in choice_text:
          
        if i == answer:
            final[a] = i
        a += 1
        
    print(final)
    if final == text_list:
        print('성공입니다.')  
        break
    elif c == trial and final != text_list:
        print('실패하였습니다')
        break

infile.close()


    

    

    

            

    
    
    



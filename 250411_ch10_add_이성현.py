############# Chapter 10 ##########
########## Additional exam #######
## 1
infile = open(r'C:\Users\blues\Python\exam\text\input.txt','r')
text = infile.read()
print(text)

infile.close()

## 2
infile = open(r'C:\Users\blues\Python\exam\text\input.txt','r')
text = infile.readlines()
print(text)

infile.close()

## 3 
file_name = input("파일 이름을 입력하세요. : ")
infile = open(file_name, "r")
text = infile.read()

count = 0
for line in text:
    text_edit = line.rstrip().strip("'").strip('.').strip(',')
    for i in text_edit:
        count += 1
        
print('파일 안에는 총 %d개의 글자가 있습니다.' %count)
infile.close()

## 4
file_name = input("파일 이름을 입력하세요. : ")
infile = open(file_name, "r")
text = infile.read().split()
text_dic = {}

count = 0
for line in text:
    text_edit = line.rstrip().strip("'").strip('.').strip(',').lower()
    
    for i in text_edit:
        if i in text_dic:
            text_dic[i] += 1
            count += 1
        else: 
            text_dic[i] = 1
            count += 1

sorted_dict = dict(sorted(text_dic.items()))
print(sorted_dict)
infile.close()


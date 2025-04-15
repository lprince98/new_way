######### Chapter 04 추가 문제
## 1
ing = input('문자열을 입력하시오:')
print(ing+'하는 중')

##2
string = input('기호를 입력하시오:')
between = input('중간에 삽입할 문자열을 입력하시오:')
print(string[0]+between+string[1])

##3
drive = input('드라이브 이름:')
dir = input('디렉토리 이름:')
file = input('파일 이름:')
extension = input('확장자:')
print('완전한 이름은 '+drive+dir+file+'.'+extension)

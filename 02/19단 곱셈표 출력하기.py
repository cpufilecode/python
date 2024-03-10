# 2단 곱셈표

number = [1,2,3,4,5,6,7,8,9]
for item in number:
    print(2 * item)

# range문 실습

for exam in range(2, 20):
    print(exam)

# 19단 곱셈표 (업그레이드 ver)
    
for item in range(2, 20):
    for exam in range(2, 20):
        print(item,' X ', exam, ' = ', item * exam)
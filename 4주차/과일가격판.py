fruits = {'apple':1000,'orange':2000,'banana':3000,'mango':4000}

print("과일 이름을 입력해주세요.")
f_str = input()
if f_str in fruits:
    print(f"{f_str}의 가격은 {fruits[f_str]} 입니다.")
else:
    print(f"{f_str}은/는 존재하지 않습니다.")
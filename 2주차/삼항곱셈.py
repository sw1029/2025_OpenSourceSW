n = 3
num_list = []

for i in range(n):
    print(f"{i+1}번째 피연산자를 입력하세요: ",end="")
    num_list.append(int(input()))

result = 1
for i in range(len(num_list)):
    print(f"{num_list[i] }",end="")
    result *= num_list[i]
    if i != len(num_list)-1: print(" x ", end="")
    else: print(" = ",end="")
print(result, end="")
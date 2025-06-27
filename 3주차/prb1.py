import random
x = random.randint(1,100)
y = random.randint(1,100)

print(f'{x} x ? = {x*y}')
print("정답: ",end="")
result = int(input())
print()
if result == x: print("정답입니다")
else: print("오답입니다.")
# 백준 1111번
# 주어진 수열을 통해 (a, b)를 추측하고 이를 바탕으로 생성한 수열이 주어진 수열과 일치하는지

n = int(input())
arr = list(map(int, input().split()))

def find_rule(num_list):
  a = int((num_list[2] - num_list[1]) / (num_list[1] - num_list[0]))
  b = num_list[1] - (a * num_list[0])
  return a, b

def same_num(num_list):
  for i in range(len(num_list)):
    if i == 0:
      continue
    if num_list[i-1] == num_list[i]:
      pass
    else:
      return False
  return True

def solve():
  if n == 1:
    print('A')
  elif n == 2:
    if arr[0] == arr[1]:
      print(arr[-1])
    else:
      print('A')
  else:
    if arr[0] == arr[1]:
      if same_num(arr):
        print(arr[-1])
      else:
        print('B')
      return
    sample = [arr[0]]
    a, b = find_rule(arr)
    for i in range(n):
      if i == 0:
        continue
      sample.append(a*arr[i-1]+b)
    if sample == arr:
      print(a*arr[-1]+b)
    else:
      print('B')

solve()
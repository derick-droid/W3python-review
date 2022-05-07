lst = []
n = int(input("Enter number of elements : "))
sum_list = 0

for i in range(0, n):
    ele = int(input("enter number : "))
    lst.append(ele)

print(lst)

for ele in range(0, len(lst)):
    sum_list = sum_list + lst[ele]

average = sum_list / len(lst)
print(f" the average is:  {average}")

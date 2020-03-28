my_list=[]
for i in range(5):
    my_list.append(int(input('Enter the number ')))
def reverse(array):
    for i in range(2):
        placeholder=array[i]
        array[i]=array[4-i]
        array[4-i]=placeholder
reverse(my_list)
print(my_list)

        

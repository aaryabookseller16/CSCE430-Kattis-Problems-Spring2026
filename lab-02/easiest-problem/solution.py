# helper function to calculate sum of digits
def sum_digits(n):
    size_of_n = len(n)
    sum = 0
    power = 0
    for i in range(size_of_n - 1, -1 , -1):
        digit = int(n[i])

        sum += digit
        power += 1
        
    return sum

while True:
    num = input()
    int_num = int(num)
    if int_num == 0:
        break
    sum_of_num = sum_digits(num)
    for i in range(11, 100000):
        current_product = int_num*i
        current_product_string = str(current_product)
        #print(f"current_product", current_product)
        running_sum = sum_digits(current_product_string)
        #print(f"running_sum", running_sum)
        
        if running_sum == sum_of_num:
            print(i)
            break
        
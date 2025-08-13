base_num = int(input("Enter your base number: "))
power_num = int(input("Enter your rasieto (^) number: "))

def raise_to_function(base_num, power_num):
    result = 1
    for num in range(power_num):
        result = result * base_num
    return result
print(raise_to_function(int(base_num), int(power_num)))

def rec_power(num, power_value):
    powa = pow(num, power_value)
    return powa

num = int(input("Enter number: " ))
power_value = int(input("Enter power value: " ))
print(f'The value of {num} to the power of {power_value} is {rec_power(num, power_value)}')





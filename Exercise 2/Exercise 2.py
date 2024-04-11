def prime_factor(number):
    counter2 = 0
    counter3 = 0
    counter5 = 0
    counter7 = 0
    counter11 = 0
    first_number = number
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            counter2 += 1
        elif number % 3 == 0:
            number = number / 3
            counter3 += 1
        elif number % 5 == 0:
            number = number / 5
            counter5 += 1   
        elif number % 7 == 0:
            number = number / 7
            counter7 += 1
        elif number % 11 == 0:
            number = number / 11
            counter11 += 1        
    return f"The prime factors of the number {first_number} is 2^{counter2}, 3^{counter3}, 5^{counter5}, 7^{counter7}, 11^{counter11}"

number = int(input("Write a number: "))
print(prime_factor(number))
    
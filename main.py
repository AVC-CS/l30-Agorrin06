def main():
    while True:
        try:
            number = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    
    if number %2!=0:
        result = 1
    else:
        result = 0

    if result:
        print(f'The value {number} is an odd number')
    else:
        print(f'The value {number} is an even number')
    return result


if __name__ == '__main__':
    main()

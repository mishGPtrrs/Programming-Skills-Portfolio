# even or odd

def check_even_odd(number):
    #determine if the number is even or odd
    if number % 2 == 0:
        return f"the number {number} is even."
    else:
        return f"the number {number} is odd."

def main():
    #ask the user to enter a number
    user_input = int(input("enter a number: "))
    
    #get the result from check_even_odd function
    result = check_even_odd(user_input)
    
    #print the result
    print(result)

#run the main function
if __name__ == "__main__":
    main()

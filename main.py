#Caesar cipher:
'''
The Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
Moreover, we will let the code preserve the letters' case (lower-case letters will remain lower-case)
and all non-alphabetical characters will remain untouched.
'''

from validation import number_in_range_validation, true_false_validation #import my module

def message_type_validation (message_type:str) -> str:
    '''
    Check whether the input is valid.

    Args:
        message_type (str): The message_type to check.

    Returns:
        str: The validated message_type.

    Raises:
        ValueError: if the input is not valid. 
    '''
    message_type = message_type.lower()

    if message_type in ('e', 'd'):
        return message_type
    
    raise ValueError("You must type 'e' or 'd'")

def ascii_code_check (letter_ord:int, letter_type:str) -> str:
    '''
    Adjust shifted ASCII values to remain within alphabet boundaries.
    Handles wraparound for both uppercase and lowercase letters.

    Args:
        letter_ord (int): The ord(letter).
        letter_type (str): The type of the letter (uppercase or lowercase).

    Returns:
        str: The chr(letter).
    '''

    if letter_type == "upper":
        if 65 <= letter_ord <= 90:
            return chr(letter_ord)
        
        elif letter_ord > 90: 
            return chr(letter_ord-26) 
        
        else:
            return chr(letter_ord+26)
               
    if 97 <= letter_ord <= 122:
        return chr(letter_ord)
    
    elif letter_ord > 122:
        return chr(letter_ord-26)
    
    else:
        return chr(letter_ord+26)

def main():
    again = True
    while again:
    #Taking the input from the user
        text = input("Enter the message: ")

        print("What do you want to do with this message?")
        
        while True:
            try:
                message_type = message_type_validation(input("Enter 'e' for (encryption) or 'd' for (decryption) "))

            except ValueError as error:
                print(f"Invalid input, {error}")

            else:
                if message_type == 'e':
                    operation = 1

                else:
                    operation = -1
                
                break

        while True:
            try:
                shift = number_in_range_validation(int(input("Enter the cipher shift value (1..25): ")), 1, 25)
                break

            except ValueError as error:
                print(f"Input invalid, {error}")

        message = ""
        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    letter_type = "upper"

                else:
                    letter_type = "lower"

                letter = ascii_code_check(ord(letter) + (shift*operation), letter_type)
                
            message += letter

        print(message)

        while True:
            try:
                again = true_false_validation(input("Do you want to enter another message? 'yes' or 'no' "))
                break

            except ValueError as error:
                print(f"Invalid input, {error}")

    print("See you!")

if __name__=="__main__":
    main()
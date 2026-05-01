#Caesar cipher :
'''
The Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.
Moreover, we will let the code preserve the letters' case (lower-case letters will remain lower-case)
and all non-alphabetical characters will remain untouched.
'''

from validation import number_in_range_validation #import my module

def ascii_code_check (letter_ord, letter_type) :
    if letter_type == "upper" :
        if 65 <= letter_ord <= 90 :
            return chr(letter_ord)
        
        else :
            return chr(letter_ord-26) 
               
    if 97 <= letter_ord <= 122 :
        return chr(letter_ord)
    
    else :
        return chr(letter_ord-26)

def main() :
#Taking the input from the user
    text = input("Enter the message you want to encrypt: ")
    try :
        shift = number_in_range_validation(input("Enter the cipher shift value (1..25): "), 0, 25)
    except ValueError as error :
        print(f"Input invalid, {error}")

    message = ""
    letter_type = None
    for letter in text :
        if letter.isalpha() :
            if letter.isupper() :
                letter_type = "upper"

            else :
                letter_type = "lower"

            letter = ascii_code_check(ord(letter) + shift, letter_type)
            
        message += letter

    print(message)

if __name__=="__main__":
    main()
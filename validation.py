"""
validation.py

Reusable validation and helper functions
for handling user input, strings, and numbers.

Author: Amr Deyab
Date: 2026-05-01
"""

# imports here

from typing import Any

__all__ = [
    "positive_digit_validation",
    "digit_validation",
    "number_in_range_validation",
    "non_empty_validation",
    "name_validation",
    "yes_no_validation",
    "remove_duplicates",
    "again_validation",
]

def positive_digit_validation(number: str) -> int:
    """
    Check whether the input is a positive number.

    Args:
        number (str): The number to check.

    Returns:
        int: The validated positive integer.

    Raises:
        ValueError: If the input is not a positive integer.
    """

    if number.isdigit():
        return int(number)
    
    raise ValueError("You must enter a positive number")

def digit_validation(number: str) -> int:
    """
    Check whether the input is a number.

    Args:
        number (str): The number to check.

    Returns:
        int: The validated integer.

    Raises:
        ValueError: If the input is not a number.
    """

    try :
        return int(number)
    
    except ValueError as error:
        raise ValueError("You must enter a number.") from error

def number_in_range_validation(number: int, start:int, end:int) -> int :
    """
    Check whether the input is in the range.

    Args:
        number (int): The number to check if it is in range.
        start (int): The start of the range
        end (int): The end of the range

    Returns:
        int: The validated number.

    Raises:
        ValueError: If the input is not in the range.
    """

    if start <= number <= end :
        return int(number)
    
    if number < start :
        raise ValueError("You cannot enter a number lower than the starting number.")

    raise ValueError("You cannot enter a number larger than the last number.")

def non_empty_validation(text:str) -> str :
    """
    Check whether the input is not empty.

    Args:
        text (str): The text to check if it is empty.

    Returns:
        str: The text if not empty.

    Raises:
        ValueError: If the input is empty.
    """

    if text.strip() :
        return text.lower()
    
    raise ValueError("You must type something.")

def name_validation(name:str) -> str :
    """
    Check if the name consists only of letters.

    Args:
        name (str): The name to check if it is valid.

    Returns:
        str: The validated name.

    Raises:
        ValueError: If the name not only letters.
    """

    if name.isalpha() :
        return name.lower()
    
    raise ValueError("The name must consist of letters only.")

def yes_no_validation(word:str) -> str :
    """
    Check if the input is 'yes' or 'no'.

    Args:
        word (str): The word to check if it is 'yes' or 'no'.

    Returns:
        str: The validated word.
        
    Raises:
        ValueError: If the input is not 'yes' or 'no'.
    """

    if word.lower() in ('no','yes'):
        return word.lower()

    raise ValueError("You must type 'yes' or 'no'.")  

def remove_duplicates(items:list[Any]) -> list[Any]:
    """
    Remove the duplicates from the list.

    Args:
        items (list): List from which duplicate items should be removed.

    Returns:
        list: The list after removing the duplicates.
    """
    unique_items = []
    for item in items :
        if item in unique_items :
            continue

        unique_items.append(item)

    return unique_items

def again_validation(again:str) -> bool :
    """
    Check if the input is 'yes' or 'no'.

    Args:
        again (str): The word to check if it is 'yes' or 'no'.

    Returns:
        bool: True if 'yes', False if 'no'.
    
    Raises:
        ValueError: If the input is not 'yes' or 'no'.
    """
    again = again.lower()
    if again in ('yes', 'no'):
        return again == 'yes'

    raise ValueError("You must type 'yes' or 'no'")

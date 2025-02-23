# List Comprehensions

def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Convert a PascalCase or camelCase string to snake_case.

    Args:
        pascal_or_camel_cased_string (str): The input string in PascalCase or camelCase.

    Returns:
        str: The converted string in snake_case.
    """
    # Convert each uppercase letter to lowercase and prepend with an underscore
    # conversion to snake case using a for loop
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')
    # return clean_snake_cased_string

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()

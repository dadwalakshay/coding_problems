alpha_numeric_mapper = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}


contact_list = {
    'mom': 9999999999,
    'dad': 9090909090,
    'sis': 9988776655,
    'friend': 9876543210,
    'faf': 9191919191,
}


contact_name_to_keypad_combinations = {}


def smart_contact_finder(user_input=''):
    """Helper function to fetch possible contact."""
    if not user_input:
        return []

    matched_contact_numbers = []

    matched_keypad_numbers = list(
        filter(
            lambda keypad_number: user_input in keypad_number,
            contact_name_to_keypad_combinations.keys()
        )
    )

    for keypad_number in matched_keypad_numbers:
        matched_contact_numbers.extend(
            contact_name_to_keypad_combinations[keypad_number]
        )

    return matched_contact_numbers


def contact_name_to_keypad_number_converter(contact_list={}):
    """Converts Alphabatical Contact names to Keypad digits and store in-place.
    """
    for key, value in contact_list.items():
        raw_contact_name = key
        raw_contact_number = value

        keypad_numbered_contact_name = ''

        for character in key:
            for digit, letters in alpha_numeric_mapper.items():
                if character in letters:
                    keypad_numbered_contact_name += str(digit)

        if not keypad_numbered_contact_name:
            return

        try:
            assert type(contact_name_to_keypad_combinations[keypad_numbered_contact_name]) is list
        except (AssertionError, KeyError):
            contact_name_to_keypad_combinations[keypad_numbered_contact_name] = [raw_contact_number, ]
        else:
            contact_name_to_keypad_combinations[keypad_numbered_contact_name].append(raw_contact_number)

    return


if __name__ == '__main__':
    dummy_test_cases = {
        '323': [contact_list['dad'], contact_list['faf'], ],
        '3743': contact_list['friend'],
        '99999': [],
    }

    # Create a rainbow table of contact_name-keypad_number combinations
    contact_name_to_keypad_number_converter(contact_list)

    score = 0

    for key, value in dummy_test_cases.items():
        try:
            predicted_response = smart_contact_finder(key)

            assert value in predicted_response or value == predicted_response
        except AssertionError:
            print(f'Test case failed | Excepected result: {value} | Actual result: {predicted_response}')
        else:
            score += 1

    print(f'\nThis algorithm is {(score/len(dummy_test_cases.keys())*100):.2f}% accurate.')

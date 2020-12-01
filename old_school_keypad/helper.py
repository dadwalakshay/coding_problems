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
}


def smart_contact_finder(usr_inp=''):
    """Helper function to fetch possible contact."""
    return


if __name__ == '__main__':
    dummy_test_cases = {
        '323': contact_list['dad'],
        '3743': contact_list['friend'],
        '99999': None
    }

    score = 0

    for key, value in dummy_test_cases.items():
        try:
            predicted_response = smart_contact_finder(key)

            assert predicted_response == value
        except AssertionError:
            print(f'Test case failed | Excepected result: {value} | Actual result: {predicted_response}')
        else:
            score += 1

    print(f'\nThis algorithm is {(score/len(dummy_test_cases.keys())*100):.2f}% accurate.')

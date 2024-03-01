POSITIVE_ANSWER = 'yes'


def create_list_of_int():
    """
    Function to create a list of integers, and also see item by index
    :return: list of integers
    """
    custom_items = input("Please enter numbers separated by coma: ").split(',')

    try:
        custom_items = list(map(lambda x: int(x.strip()), custom_items))
    except ValueError:
        print('Invalid list of numbers')
        return

    custom_answer = input("Do you want to see specific item? (enter yes or no) ").lower()
    show_specific_item = False

    if custom_answer == POSITIVE_ANSWER:
        show_specific_item = True


    if show_specific_item:
        index = input('Please enter the index of the item you want to see: ')

        try:
            index = int(index)
        except ValueError:
            print('Entered invalid index of item, will be taken default index (0)')
            print(custom_items[0])
        else:
            print(custom_items[index])

    return custom_items


print(create_list_of_int())

import sys

class Item():
    def __init__(self, id, value):
        self.id = id
        self.value = int(value)

def print_solution(min_items):
    if isinstance(min_items, str):
        print(min_items)
    else:
        print('%s %d, %s %d' % (min_items[0].id, min_items[0].value, min_items[1].id, min_items[1].value))

def read_arguments():
    filename = sys.argv[1]
    balance_str = sys.argv[2]
    try:
        balance = int(balance_str)
    except ValueError:
        print('Invalid balance: %. Balance must be a positive integer' % balance_str)
        exit(2)

    try:
        file = open(filename, 'r')
    except IOError:
        print('Invalid filename: %. Could not open file' % filename)
        exit(2)

    return file, balance

def read_items_from_file(file):
    items = []
    for line in file:
        id, value_str = line.split(',')
        try:
            value = int(value_str)
            items.append(Item(id, value))  # only initialize items with valid inputs
        except ValueError:
            print('Invalid value % for item %. Value must be a positive integer' % (value_str, id))

    return items

def solve(items, balance):
    items.sort(key=lambda x: x.value)
    min_distance = sys.maxsize
    min_items = 'Not possible'

    for i, item in reversed(list(enumerate(items))):
        remaining = balance - item.value
        low = 0
        high = i - 1
        mid = 0
        while (low <= high):
            mid = (low + high) // 2
            if items[mid].value > remaining:
                high = mid - 1
            else:
                low = mid + 1

        if items[mid].value > remaining:
            mid -= 1

        remaining = balance - item.value - items[mid].value
        if remaining < min_distance and remaining >= 0 and mid != i:
            min_distance = remaining
            min_items = (item, items[mid])

    return min_items

def main():
    file, balance = read_arguments()
    items = read_items_from_file(file)
    min_items = solve(items, balance)
    print_solution(min_items)

if __name__ == '__main__':
    main()
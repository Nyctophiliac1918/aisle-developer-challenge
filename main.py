from helpers import *
from BillItem import *


def take_input(input_items, input_items_in_single_line):
    # input taken from txt file
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        split_input_string = line.split()
        count_of_floats = 0
        start = 0

        # logic to show the products that are mentioned in one line in a single line only
        # 1 imported box of chocolates (food) at 10.00 1 imported bottle of perfume at 47.50 will return
        # 1 imported box of chocolates (food): 10.50 1 imported bottle of perfume: 54.62
        for index in range(0, len(split_input_string)):
            if isfloat(split_input_string[index]) and start != index:
                input_items.append(split_input_string[start:index+1])
                count_of_floats += 1
                start = index + 1
        input_items_in_single_line.append(count_of_floats)


def generate_bill(input_items, output_items):
    final_sales_tax = 0
    total_price = 0

    # will give the total sales tax and the final price
    for input_item in input_items:
        item = BillItem(input_item)
        final_sales_tax += item.calculate_total_tax()
        total_price += item.final_selling_price()
        output_items.append(item.bill_print_info())

    return [final_sales_tax, total_price]


def print_items(input_items_in_single_line, output_items):
    start = 0
    count = input_items_in_single_line[start]

    # logic to show the products that are mentioned in one line in a single line only
    for output_item in output_items:
        # output[0] = details about the product
        item_info = " ".join(output_item[0])

        # price rounded off to two decimal places
        final_price = round(output_item[1], 2)

        if count > 1:
            print('{}: {:.2f}'.format(item_info, final_price), end=' ')
            count -= 1
        else:
            print('{}: {:.2f}'.format(item_info, final_price))
            start += 1
            if start != len(input_items_in_single_line):
                count = input_items_in_single_line[start]


def print_tax_and_price(final_sales_tax, total_price):
    # prices rounded off to two decimal places
    print('Sales Taxes: {:.2f} Total: {:.2f}'.format(round(final_sales_tax, 2), round(total_price, 2)))


def main():
    input_items = list()
    input_items_in_single_line = list()
    take_input(input_items, input_items_in_single_line)

    output_items = list()
    result = generate_bill(input_items, output_items)
    final_sales_tax = result[0]
    total_price = result[1]

    print_items(input_items_in_single_line, output_items)
    print_tax_and_price(final_sales_tax, total_price)

    return


if __name__ == '__main__':
    main()

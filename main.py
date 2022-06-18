from check import *

IMPORT_DUTY_PERCENTAGE = 5
BASIC_TAX_PERCENTAGE = 10


class BillItem:
    exempted_commodities = ['book', 'medicine', 'food']

    def __init__(self, item):
        self.item = item
        self.quantity = int(item[0])
        self.price = float(item[-1])
        self.price_per_unit = self.price / self.quantity
        self.is_exempted_from_basic_tax = False
        self.is_import_duty_applied = False

    def is_item_imported(self):
        # checking if the item is imported or not
        if 'imported' in self.item:
            self.is_import_duty_applied = True

    def is_item_basic_tax_exempted_commodity(self):
        # checking if the item is from the tax exempted commodities ot not
        for commodity in self.exempted_commodities:
            if any(commodity in list_item for list_item in self.item):
                self.is_exempted_from_basic_tax = True

    def calculate_total_tax(self):
        final_tax_percentage = 0

        self.is_item_basic_tax_exempted_commodity()
        self.is_item_imported()

        if not self.is_exempted_from_basic_tax:
            final_tax_percentage += BASIC_TAX_PERCENTAGE

        if self.is_import_duty_applied:
            final_tax_percentage += IMPORT_DUTY_PERCENTAGE

        # rounded off to two decimal places
        return round(self.price * final_tax_percentage / 100, 2)

    def final_selling_price(self):
        return self.price + self.calculate_total_tax()

    def bill_print_info(self):
        length_of_split_list = len(self.item)

        # ['1', 'book', 'at', '12.49'] returns ['1', 'book'] which will help in printing the final output
        item_detail = self.item[0:length_of_split_list - 2]

        # returns text for printing item info and final selling price of the item
        return [item_detail, self.final_selling_price()]


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

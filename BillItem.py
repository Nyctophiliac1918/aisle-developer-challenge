from constants import *


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
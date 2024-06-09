
class Printer:
    def __init__(self, printer_name, manufacturer_country, printer_color, price, text_color, manufacture_date, paper_type):
        self.printer_name = printer_name
        self.manufacturer_country = manufacturer_country
        self.printer_color = printer_color
        self.price = price
        self.text_color = text_color
        self.manufacture_date = manufacture_date
        self.paper_type = paper_type
        self.paper_used = 0  # Кількість використаного паперу, початкове значення - 0

    def display_data(self):
        print("Printer Data:")
        print(f"{'Printer name':<20} {self.printer_name}")
        print(f"{'Manufacturer country':<20} {self.manufacturer_country}")
        print(f"{'Printer color':<20} {self.printer_color}")
        print(f"{'Price':<20} {self.price}")
        print(f"{'Text color':<20} {self.text_color}")
        print(f"{'Manufacture date':<20} {self.manufacture_date}")
        print(f"{'Paper type':<20} {self.paper_type}")
        print(f"{'Paper used':<20} {self.paper_used} pages")

    def print_pages(self, pages):
        if pages < 0:
            print("Error: Number of pages to print cannot be negative.")
        else:
            self.paper_used += pages
            print(f"Printed {pages} pages.")

def create_printer():
    # Запитати у користувача дані про принтер
    printer_name = input("Enter printer name: ")
    manufacturer_country = input("Enter manufacturer country: ")
    printer_color = input("Enter printer color: ")
    price = float(input("Enter printer price: "))
    text_color = input("Enter text color: ")
    manufacture_date = input("Enter manufacture date: ")
    paper_type = input("Enter paper type: ")

    # Створити екземпляр класу Printer
    printer = Printer(printer_name, manufacturer_country, printer_color, price, text_color, manufacture_date, paper_type)
    return printer

# Створити два екземпляри класу Printer
print("Enter details for Printer 1:")
printer1 = create_printer()
print("Enter details for Printer 2:")
printer2 = create_printer()

# Вивести дані про обидва принтери
print("\nDetails of Printer 1:")
printer1.display_data()
print("\nDetails of Printer 2:")
printer2.display_data()

# Приклад використання методу print_pages для обох принтерів
pages_to_print1 = int(input("\nEnter number of pages to print for Printer 1: "))
printer1.print_pages(pages_to_print1)
pages_to_print2 = int(input("Enter number of pages to print for Printer 2: "))
printer2.print_pages(pages_to_print2)

# Вивести оновлені дані про обидва принтери
print("\nUpdated details of Printer 1:")
printer1.display_data()
print("\nUpdated details of Printer 2:")
printer2.display_data()
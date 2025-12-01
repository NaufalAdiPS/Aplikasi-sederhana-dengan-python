from datetime import datetime


class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"Order ID : {self.order_id}")
        print(f"Customer : {self.customer_name}")
        print(f"Order Date : {self.order_date}")
        print(f"Total Amount : Rp{self.total_amount:,.2f}")


class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        return sum(order.total_amount for order in self.orders)

    def calculate_total_tax(self, tax_rate):
        return sum(order.calculate_tax(tax_rate) for order in self.orders)

    def display_orders(self):
        print("\n Daftar Semua Pesanan:")
        for order in self.orders:
            order.display_order()
            print("-" * 30)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():
    processor = OrderProcessor()

    print("Sistem pengelolaan pesanan")
    jumlah = int(input("Masukkan jumlah pesanan: "))

    for i in range(jumlah):
        print(f"\nPesanan ke-{i+1}")
        order_id = input("Masukkan Order ID : ")
        customer_name = input("Masukkan Nama Pelanggan : ")
        order_date = input("Masukkan Tanggal Pesanan (YYYY-MM-DD): ")
        while not validate_date(order_date):
            print("Tanggal tidak valid! Contoh: 2025-10-11")
            order_date = input("Masukkan Tanggal Pesanan (YYYY-MM-DD): ")
        total_amount = float(input("Masukkan Total Harga (Rp): "))

        
        order = Order(order_id, customer_name, order_date, total_amount)
        processor.add_order(order)

    
    tax_rate = 0.1
    total_revenue = processor.calculate_total_revenue()
    total_tax = processor.calculate_total_tax(tax_rate)

    
    processor.display_orders()
    print(f"\n Total Pendapatan: Rp{total_revenue:,.2f}")
    print(f"Total Pajak (10%): Rp{total_tax:,.2f}")


if __name__ == "__main__":
    main()

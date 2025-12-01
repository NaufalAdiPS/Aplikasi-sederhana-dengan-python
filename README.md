# Aplikasi-sederhana-dengan-python
Repository untuk hardskill Membuat aplikasi sederhana dengan python.Dibimbing

---

## Fitur Program
Dalam progam ini memiliki beberapa fungsi yaitu :
- Mewakili data pesanan pelanggan menggunakan kelas Order
- Mengelola daftar pesanan menggunakan kelas OrderProcessor
- Menghitung total pendapatan dari semua pesanan
- Menghitung total pajak berdasarkan tarif pajak tertentu
- Menampilkan detail semua pesanan dalam format yang mudah dibaca
- Validasi format tanggal menggunakan`datetime.strptime

---

## Struktur code python

### 1. Class Order
Merepresentasikan satu pesanan pelanggan dengan atribut:
- order_id
- customer_name
- order_date
- total_amount

Metode:
- calculate_tax(tax_rate) → Menghitung pajak sesuai tarif
- display_order() → Menampilkan detail pesanan

---

### 2. Class OrderProcessor
Mengelola kumpulan objek Order.

Metode:
- add_order(order) → Menambah pesanan ke list
- calculate_total_revenue() → Total pendapatan
- calculate_total_tax(tax_rate) → Total pajak
- display_orders() → Menampilkan semua pesanan

---

### 3. Program Utama
Program utama melakukan:
- Input data pesanan
- Validasi tanggal dengan datetime.strptime
- Menambahkan pesanan ke dalam OrderProcessor
- Menampilkan laporan pendapatan dan pajak
- Menampilkan semua pesanan

---

## Cara menjalankan progam pythonn nya

1. Pastikan bahwa python sudah terinstall.
2. Simpan code nya dan bebas menamakan nya misal main.py
3. Dan kemudian buka terminal dan ketil python main.py.
4. Setelah itu input sesuai dengan yang ingin di input.

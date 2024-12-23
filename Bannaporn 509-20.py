products = {
"หมูสับกิโล": 150,
"เนื้ออกไก่": 105,
"ไก่บ้าน(ตัว)": 120,
"มาม่าต้มยำ": 6.50,
"ข้าวสาร": 150,
"น้ำตาล": 20,
"ปลากะป๋องสามแม่ครัว": 10,
"ซอสน้ำปลาหอย": 18,
"ผงชูรส": 10.25,
"ไข่แผงคละเบอร์": 120.25,
"ชาเขียว": 21.50,
"Pepsi": 29.50,
"กาแฟ": 15.75,
"ขนมปังอบเนย": 19,
"ชาไทย": 11.50,
"น้ำเปล่า": 15.15,
"น้ำแข็ง": 10
}

budget = 1000
selected_products = []

while len(selected_products) < 15:
print("รายการสินค้า:")
for product, price in products.items():
print(f"- {product}: {price} บาท")

choice = input("กรุณาเลือกสินค้า (พิมพ์ชื่อสินค้า): ")
if choice in products:
    price = products[choice]
    if price <= budget:
        selected_products.append(choice)
        budget -= price
        print(f"คุณเลือก {choice} ราคา {price} บาท")
    else:
        print("เกินงบประมาณ!")
else:
    print("ไม่มีสินค้าชนิดนี้")
total_price = sum(products[item] for item in selected_products)
change = budget

print("\nสินค้าที่คุณเลือก:")
for item in selected_products:
print(f"- {item}")
print(f"\nราคาทั้งหมด: {total_price:.2f} บาท")
print(f"เงินทอน: {change:.2f} บาท")


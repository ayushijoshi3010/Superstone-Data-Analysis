# Importing all the required libraries

import pandas as pd
import numpy as np
import random
from faker import Faker

# Initializing Faker for collecting fake data
fake=Faker('en_IN')

# Defining base lists

categories={
    "Furniture":["Office Chairs","Study Table","Sofa","Bookshelf","Dining Table"],
    "Office Supplies":["Pen","Notebook","Stapler","File Folder","Calculator"],
    "Electronics":["Laptop","Keyboard","Mouse","Headphones","Monitor"],
    "Grocery":["Rice Bag","Cooking Oil"]
}

regions=["North","South","East","West"]
payment_modes=["Cash","Credit Card","UPI","Net Banking"]
delivery_status=["Delivered","Pending","Returned","Cancelled"]
customer_segments=["COnsumer","Corporate","Home Office"]

# Step-3 Generate Fake Data

records=[]

for i in range(1000): #1000 fake orders

    order_id=f"ORD{1000 +i}"
    order_date=fake.date_between(start_date='-3y',end_date='today')
    ship_date=order_date+pd.Timedelta(days=random.randint(1,7))

    customer_name=fake.name()
    customer_id=f"CUST{random.randint(100,999)}"
    customer_segment=random.choice(customer_segments)

    category=random.choice(list(categories.keys()))
    product_name=random.choice(categories[category])
    product_id=f"PROD{random.randint(100,999)}"

    region=random.choice(regions)
    state=fake.state()
    city=fake.city()

    quantity=random.randint(1,10)
    unit_price=random.randint(100,15000)
    discount=random.choice([0,5,10,15,20])

    sales_amount=unit_price*quantity*(1-(discount/100))
    costprice=sales_amount*random.uniform(0.3,0.8)
    profit=sales_amount-costprice

    stock_left=random.randint(0,50)

    if(stock_left<10):
        auto_reorder="Yes"
        reorder_quantity=random.randint(20,50)
    
    else:
        auto_reorder="No"
        reorder_quantity=0
    
    supplier_name=fake.company()
    supplier_email=fake.company_email()
    payment_mode=random.choice(payment_modes)
    delivery=random.choice(delivery_status)

    # Append row as a dictionary
    records.append({
        "Order Id":order_id,
        "Order Date":order_date.strftime('%d-%m-%Y'),
        "Ship Date":ship_date.strftime('%d-%m-%Y'),
        "Customer Id":customer_id,
        "Customer Name":customer_name,
        "Customer Segment":customer_segment,
        "Product Id":product_id,
        "Product Name":product_name,
        "Category":category,
        "Region":region,
        "State":state,
        "City":city,
        "Quantity":quantity,
        "Unit Price":unit_price,
        "Discount %":discount,
        "Sales Amount":round(sales_amount,2),
        "Cost Price":round(costprice,2),
        "Profit":round(profit,2),
        "Payment Mode":payment_mode,
        "Delivery Status": delivery,
        "Supplier Name":supplier_name,
        "Supplier Email":supplier_email,
        "Stock Left":stock_left,
        "Auto Reorder":auto_reorder,
        "Reorder Quantity":reorder_quantity
    })


# Create DataFrame and save it to csv

df=pd.DataFrame(records)

print(df.head())
try:
    df.to_csv("Superstone_Management_System.csv",index=False)
    print("Dataset generated Successfully! File saved as 'Superstone_Management_System.csv' ")
except PermissionError:
    print("Please close this file 'Superstone_Management_System.csv' if it's open in Excel or Power BI")
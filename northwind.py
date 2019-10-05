import sqlite3

conn = sqlite3.connect(r'C:\Users\anika\Desktop\AnikaDS\Unit_3_Lambda\DS-Unit-3-Sprint-2-SQL-and-Databases\Sprint Challenge\northwind_small.sqlite3')
cursor = conn.cursor()

expensive = cursor.execute('SELECT productname, unitprice FROM product ORDER BY unitprice DESC LIMIT 10').fetchall()
age = cursor.execute('SELECT AVG((julianday(employee.hiredate) - julianday(employee.birthdate))/365) FROM employee').fetchall()
expensive_suppliers = cursor.execute('SELECT product.productname, product.unitprice, supplier.companyname FROM product, supplier WHERE product.supplierid = supplier.id ORDER BY unitprice DESC LIMIT 10').fetchall()
lg_unique_category = cursor.execute('SELECT category.categoryname, COUNT(product.id) FROM category, product WHERE product.categoryid = category.id LIMIT 1').fetchall()

'''Output:
[('Côte de Blaye', 263.5), ('Thüringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("
Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('M
anjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('Rössle Sauerkr
aut', 45.6)]

[(37.308980213089804,)]

[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'
), ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe N
iku', 97, 'Tokyo Traders'), ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), ('C
arnarvon Tigers', 62.5, 'Pavlova, Ltd.'), ('Raclette Courdavault', 55, 'Gai pâturage'), ('M
anjimup Dried Apples', 53, "G'day, Mate"), ('Tarte au sucre', 49.3, "Forêts d'érables"), ('
Ipoh Coffee', 46, 'Leka Trading'), ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmär
kte AG')]

[('Beverages', 77)]
'''

if __name__ == '__main__':
    print(expensive, age, expensive_suppliers, lg_unique_category)

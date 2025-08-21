import xml.etree.ElementTree as ET

root = ET.Element('bookstore')

book1 = ET.SubElement(root, 'book')
title1 = ET.SubElement(root, 'title')
title1.text = 'Intorduction to Python'
author1 = ET.SubElement(root, 'author')
author1.text = 'John Doe'
price1 = ET.SubElement(root, 'price')
price1.text = '29.99'

book2 = ET.SubElement(root, 'book')
title2 = ET.SubElement(root, 'title')
title2.text = 'Data Science with Python'
author2 = ET.SubElement(root, 'author')
author2.text = 'Jane Smith'
price2 = ET.SubElement(root, 'price')
price2.text = '39.95'

tree = ET.ElementTree(root)
tree.write('books.xml')

parsed_tree = ET.parse('books.xml')
parsed_root = parsed_tree.getroot()

for book in parsed_root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    price = book.find('price').text
    print(f'Title: {title}, Author: {author}, Price: {price}')
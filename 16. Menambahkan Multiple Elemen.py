import xml.etree.ElementTree as ET

root = ET.Element('root')

for i in range(5):
    child = ET.SubElement(root, 'child')
    child.text = f'Content {i+1}'

print(ET.tostring(root, encoding='unicode'))
# Fungsi: Menambahkan beberapa elemen ke dalam XML dengan loop.
# Kondisi: Ketika Anda ingin dengan cepat membuat beberapa elemen XML.
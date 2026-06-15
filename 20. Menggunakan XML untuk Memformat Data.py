import xml.etree.ElementTree as ET

root = ET.Element('data')
item = ET.SubElement(root, 'item')
item.text = 'Sample Item'

# Menyimpan ke file
tree = ET.ElementTree(root)
tree.write("data.xml")

# Membaca file yang sama
new_tree = ET.parse("data.xml")
new_root = new_tree.getroot()
print(ET.tostring(new_root, encoding='unicode'))
# Fungsi: Memformat data dalam XML dan menulis kemudian membacanya dari file.
# Kondisi: Ketika Anda perlu menyimpan format data dalam XML.
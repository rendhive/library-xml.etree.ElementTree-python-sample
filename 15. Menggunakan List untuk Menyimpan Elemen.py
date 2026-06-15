import xml.etree.ElementTree as ET

root = ET.Element('root')
children_data = ['Content 1', 'Content 2']

for content in children_data:
    child = ET.SubElement(root, 'child')
    child.text = content

print(ET.tostring(root, encoding='unicode'))
# Fungsi: Menyimpan elemen dari list ke dalam XML.
# Kondisi: Ketika Anda mengelola nilai yang tersimpan dalam struktur list untuk dijadikan elemen XML.
import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child id="1">Content 1</child>
</root>'''

root = ET.fromstring(xml_data)
child = root.find('child')
child.set('name', 'Child 1')  # Menambahkan atribut baru
print(child.attrib)  # Menampilkan atribut dari elemen
# Fungsi: Mengelola atribut dari elemen XML.
# Kondisi: Ketika Anda ingin mengelola informasi tambahan di elemen XML.
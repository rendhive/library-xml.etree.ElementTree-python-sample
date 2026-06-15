import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
</root>'''

# Menyimpan ke file
tree = ET.ElementTree(ET.fromstring(xml_data))
tree.write('output.xml')

# Membaca dari file
new_tree = ET.parse('output.xml')
new_root = new_tree.getroot()
print(new_root.tag)  # Menampilkan tag root
# Fungsi: Menyimpan dan membaca file XML.
# Kondisi: Ketika Anda untuk perlu menyimpan konfigurasi atau data untuk penggunaan mendatang.
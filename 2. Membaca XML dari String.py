import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
print(root.tag)  # Menampilkan nama tag root
# Fungsi: Membaca dan mem-parsing file XML sederhana dari string.
# Kondisi: Ketika Anda ingin memproses data XML yang sudah ada dalam format string.
import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
for child in root:
    print(child.tag, child.text)  # Menggunakan iterasi untuk mendapatkan tag dan teks
# Fungsi: Mengakses setiap elemen dalam XML.
# Kondisi: Ketika Anda ingin mendapatkan informasi dari setiap elemen.
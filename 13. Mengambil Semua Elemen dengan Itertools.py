import xml.etree.ElementTree as ET
import itertools

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
children = root.findall('child')  # Mengambil semua elemen child

# Menggunakan itertools untuk membuat kombinasi
for combo in itertools.combinations(children, 2):
    print([child.text for child in combo])
# Fungsi: Mengambil semua child dan menggunakan itertools.
# Kondisi: Ketika Anda memerlukan kombinasi dari elemen yang ada.
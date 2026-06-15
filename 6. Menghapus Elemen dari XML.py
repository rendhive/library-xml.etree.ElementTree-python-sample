import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
root.remove(root.find('child'))  # Menghapus elemen pertama
print(ET.tostring(root, encoding='unicode'))  # Mengonversi kembali ke string
# Fungsi: Menghapus elemen dari XML.
# Kondisi: Ketika Anda perlu menghapus data yang tidak diperlukan.
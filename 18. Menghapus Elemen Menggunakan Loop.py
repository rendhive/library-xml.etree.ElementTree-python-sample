import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
    <child>Content 3</child>
</root>'''

root = ET.fromstring(xml_data)
to_remove = root.findall('child')[1]  # Elemen kedua
root.remove(to_remove)  # Menghapus elemen

print(ET.tostring(root, encoding='unicode'))  # Tampilkan isi XML setelah penghapusan
# Fungsi: Menghapus elemen berdasarkan hasil pencarian.
# Kondisi: Ketika Anda ingin memodifikasi struktur XML dengan menghapus elemen tertentu.
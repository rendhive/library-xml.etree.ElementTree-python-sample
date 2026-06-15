import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
</root>'''

root = ET.fromstring(xml_data)
child_exists = root.find('child') is not None
print(f"Child exists: {child_exists}")
# Fungsi: Memeriksa apakah elemen tertentu ada di dalam XML.
# Kondisi: Ketika Anda ingin memastikan bahwa elemen tersebut ada sebelum melakukan tindakan lebih lanjut.
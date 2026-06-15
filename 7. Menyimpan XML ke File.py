import xml.etree.ElementTree as ET

root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "Content 1"

tree = ET.ElementTree(root)
tree.write("output.xml")  # Menyimpan data XML ke file
# Fungsi: Menyimpan objek XML ke file.
# Kondisi: Ketika Anda ingin menyimpan hasil pemrosesan XML ke dalam file.
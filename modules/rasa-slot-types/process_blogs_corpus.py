import xml.etree.ElementTree as ET

root = ET.parse('./corpus/blogs/999503.male.25.Internet.Cancer.xml').getroot()

for post in root.findall('post'):
    print(post.text)

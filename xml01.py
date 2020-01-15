from xml.etree.ElementTree import parse

doc = parse('./resources/exam1.xml')

a = doc.findall("student")

for tmp in a:
    print(tmp.findtext("name"))
    print(tmp.findtext("age"))
    print(tmp.find("addr").attrib)
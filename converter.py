#!/usr/bin/env python

from lxml import etree

root = etree.Element("cockatrice_carddatabase", version="3")
cards = etree.SubElement(root, "cards")

card = etree.SubElement(cards, "card")
card.text = "HI"
child3 = etree.SubElement(cards, "child3", atag="2").text = "Something else"
card2 = etree.SubElement(cards, "card")
card2.text = "HIHI"

# <card>
#     <name></name>
#     <set picURL=""></set>
#     <related></related>
#     <color></color>
#     <manacost></manacost>
#     <cmc></cmc>
#     <type></type>
#     <pt></pt>
#     <loyalty></loyalty>
#     <tablerow></tablerow>
#     <text></text>
#     <token></token>
#     <cipt></cipt>
# </card>

res = etree.tostring(root, pretty_print=True)
print(res)
xml_file = open("out.xml", "w")
xml_file.write(res)
xml_file.close()

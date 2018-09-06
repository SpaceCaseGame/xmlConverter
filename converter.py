#!/usr/bin/env python

# john@netpurgatory.com
# 09/03/2018

from lxml import etree
import csv
import sys


def readCsv(inFile):
    cardData = []
    with open(inFile) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                cardData.append(row)
                line_count += 1
        print('Read '+str(line_count-1)+' cards.')
    return(cardData)


def genXml(outFile, inData):
    root = etree.Element("cockatrice_carddatabase", version="3")
    cards = etree.SubElement(root, "cards")

    line_count = 0
    for cData in inData:
        line_count += 1
        # print(cData["Name"])
        card = etree.SubElement(cards, "card")
        etree.SubElement(card, "name").text = cData["Name"]
        # <set picURL=""></set> Ignore
        etree.SubElement(card, "related").text = cData["Hosted Skills"]
        etree.SubElement(card, "color").text = cData["Class"]
        etree.SubElement(card, "manacost").text = cData["Cost"]
        # <cmc></cmc> Ignore
        etree.SubElement(card, "type").text = cData["Card Type"]
        etree.SubElement(card,
                         "pt").text = cData["Strength"]+cData["Durability"]
        # <loyalty></loyalty> Ignore
        tableRow = ""
        if cData["Card Type"] == "Gear":
            if cData["Subtypes(s)"] == "Armor":
                tableRow = 0
            if cData["Subtypes(s)"] == "Weapons":
                tableRow = 2
        if cData["Card Type"] == "AEon":
            tableRow = 1
        if cData["Card Type"] == "Talent":
            tableRow = 3
        etree.SubElement(card, "tablerow").text = tableRow
        etree.SubElement(card, "text").text = cData["Intrinsic"]
        # etree.SubElement(card,
        #                 "token").text = cData["Exotic"]+cData["ELE Support"]
        # <cipt></cipt> Ignore

    res = etree.tostring(root, pretty_print=True)
    xml_file = open(outFile, "w")
    xml_file.write(res)
    xml_file.close()
    print('Wrote '+str(line_count)+' lines.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect number of arguments!")
        sys.exit(1)
    inFile = sys.argv[1]
    cardData = readCsv(inFile)
    genXml("output.xml", cardData)

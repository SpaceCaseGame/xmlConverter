#!/usr/bin/env python

# john@netpurgatory.com
# 09/03/2018

from lxml import etree
import csv
import sys


def readCsv(inFile):
    """Reads exported card data
    This takes in a csv file where the first line containers
    the headers that will be used to determine the field names
    and returns a list of dictionaries.
    """
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


def genXml(outFile, verbose, cardData, skillData):
    """Generate xml file based for Cockatrice
    This expects both cardData and skillData as lists of dictionaries.
    """
    root = etree.Element("cockatrice_carddatabase", version="3")
    cards = etree.SubElement(root, "cards")

    line_count = 0
    for cData in cardData:
        line_count += 1
        if verbose:
            print(cData["Name"])
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
            if cData["Subtype(s)"] == "Armor":
                tableRow = "0"
            if cData["Subtype(s)"] == "Weapons":
                tableRow = "2"
        if cData["Card Type"] == "AEon":
            tableRow = "1"
        if cData["Card Type"] == "Talent":
            tableRow = "3"
        etree.SubElement(card, "tablerow").text = tableRow
        etree.SubElement(card, "text").text = cData["Intrinsic"]
        # etree.SubElement(card,
        #                 "token").text = cData["Exotic"]+cData["ELE Support"]
        # <cipt></cipt> Ignore
    for cData in skillData:
        line_count += 1
        if verbose:
            print(cData["Name"])
        card = etree.SubElement(cards, "card")
        etree.SubElement(card, "name").text = cData["Name"]
        etree.SubElement(card, "cmc").text = cData["Cost"]
        etree.SubElement(card, "type").text = cData["AET Type"]
        etree.SubElement(card, "text").text = cData["Text"]
        etree.SubElement(card, "token").text = "1"
    res = etree.tostring(root, pretty_print=True)
    xml_file = open(outFile, "w")
    xml_file.write(res)
    xml_file.close()
    print('Wrote '+str(line_count)+' lines.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect number of arguments!")
        sys.exit(1)
    cardFile = sys.argv[1]
    cardData = readCsv(cardFile)
    skillFile = sys.argv[2]
    skillData = readCsv(skillFile)
    genXml("output.xml", False, cardData, skillData)

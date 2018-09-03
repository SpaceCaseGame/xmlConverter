#!/usr/bin/env python

from lxml import etree
import csv

def readCsv(inFile):
    cardData = []
    with open(inFile) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(row)
                line_count += 1
            else:
                cardData.append(row)
                line_count += 1
        print('Processed ',line_count,' lines.')
    return(cardData)

def genXml(outFile, inData):
    root = etree.Element("cockatrice_carddatabase", version="3")
    cards = etree.SubElement(root, "cards")

    for cData in inData:
        print cData["Name"]
        card = etree.SubElement(cards, "card")
        #card.text = "HI"
        etree.SubElement(card, "name").text = cData["Name"]
        #child3 = etree.SubElement(cards, "child3", atag="2").text = "Something else"
    #card2 = etree.SubElement(cards, "card")
    #card2.text = "HIHI"

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
    xml_file = open(outFile, "w")
    xml_file.write(res)
    xml_file.close()

cardData=readCsv("cards.csv")
genXml("output.xml", cardData)

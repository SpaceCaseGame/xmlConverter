#!/usr/bin/env python

# john@netpurgatory.com
# 09/03/2018

from lxml import etree
import csv


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
        card = etree.SubElement(cards, "card")
        etree.SubElement(card, "name").text = cData["Name"]
        etree.SubElement(card, "type").text = cData["Card Type"]

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
    xml_file = open(outFile, "w")
    xml_file.write(res)
    xml_file.close()
    print('Wrote '+str(line_count)+' lines.')

cardData = readCsv("cards.csv")
genXml("output.xml", cardData)

#!/usr/bin/python3.4
import sys


def reduce():

    myList = list()
    listMacchina1 = list()
    listMacchina2 = list()
    listMacchina3 = list()

    for line in sys.stdin:
        myList.append(line)
        id = line[13]
        time = line[15]+line[16]
        # print str(time)
        if id=="1":
            # listMacchine.append("id: "+id+ " time: "+ str(time).strip())
            listMacchina1.append(time.strip())
            listMacchina1 = map(int, listMacchina1)
        if id=="2":
            # listMacchine.append("id: "+id+ " time: "+ str(time).strip())
            listMacchina2.append(time.strip())
            listMacchina2 = map(int, listMacchina2)
        if id=="3":
            # listMacchine.append("id: "+id+ " time: "+ str(time).strip())
            listMacchina3.append(time.strip())
            listMacchina3 = map(int, listMacchina3)

    print "macchina 1, tempo speso: " + str(sum(listMacchina1))
    print "macchina 2, tempo speso: " + str(sum(listMacchina2))
    print "macchina 3, tempo speso: " + str(sum(listMacchina3))
if __name__ == "__main__":
    reduce()

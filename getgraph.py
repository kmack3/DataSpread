import os
import math
import numpy as np
import matplotlib.pyplot as plt

path = '/Users/kmack/graphdata/'

fpr = [];
csize = [];
time = [];
osize = [];

def parsedata():
    for filename in os.listdir(path):
        count = 0
        if (filename[0] == '.'):
            continue
        if (filename == "acad_sheet43.txt" or filename ==  "acad_sheet61.txt" or filename == "acad_sheet679.txt" or filename == "acad_sheet697.txt"): # the error files
            continue
        orig = True 
        for line in open(path + filename):
            if 'Greedy' in line:
                orig = False
            if 'Total:' in line:
                if orig:
                    osize.append(int((line.split())[-1]))
                else:
                    csize.append(int((line.split())[-1]))
            if 'FP Rate' in line:
                fpr.append(float((line.split())[-1]))
            if 'Time taken' in line:
                time.append(int((line.split())[-1]))
        if orig:
            print(filename)
    f = open("cleandata.txt", 'w')
    for i in range(len(time)):
        if (math.isnan(fpr[i])):
            fpr[i] = 0.0
        f.write(str(time[i]) + ' ' + str(fpr[i]) + ' ' + str(osize[i]) + ' ' + str(csize[i]))
        f.write('\n')


def getdata():
    # data file is time, fpr, orig size, compressed size
    f = open("cleandata.txt", 'r')
    for line in f:
        words = line.split()
        time.append(int(words[0]))
        fpr.append(float(words[1]))
        osize.append(int(words[2]))
        csize.append(int(words[3]))

def printdata():
    print("fpr: " + str(len(fpr)))
    print("time: " + str(len(time)))
    print("osiez: " + str(len(osize)))
    print("csize: " + str(len(csize)))
    print(fpr)
    print(time)
    print(osize)
    print(csize)


def graphdata(ind, dep, xl, yl):
    data = (list(zip(ind, dep)))
    data.sort()
    x = []
    y = []
    for i in data:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y)
    plt.title(yl + " vs " + xl)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.show()

def hist(data, title, n_bins):
    colors = ['red', 'tan', 'lime']
    plt.hist(data, bins=n_bins, histtype='bar')
    #plt.hist([3, 4, 5, 6], bins=n_bins, histtype='bar')
    plt.title(title)
    plt.show()




#parsedata()
getdata()


difference = []
for i in range(len(osize)):
    difference.append(int(osize[i]) - int(csize[i]))


# graphdata(time, osize, "time", "original size") # time gets larger if original graph is larger
# graphdata(time, fpr, "time", "fpr") # fpr gets larger the larger the original graph
graphdata(difference, fpr, "amount compressed", "fpr")
# hist(difference, "amount compressed", 50)

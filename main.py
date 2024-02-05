import random
import os
csvs = ["2to23.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt", "7.txt", "8.txt", "9.txt", "A.txt", "B.txt", "C.txt", "D.txt", "E.txt", "F.txt", "G.txt", "H.txt", "I.txt", "J.txt", "K.txt", "L.txt", "add.txt", "ad1.txt", "ad2.txt", "ad3.txt", "ad4.txt", "ad5.txt", "ad6.txt", "ad7.txt", "ad8.txt", "ad9.txt", "adA.txt", "adB.txt", "adC.txt", "adDD.txt", "adE.txt", "adF.txt", "adG.txt", "adH.txt", "adI.txt", "adJ.txt", "adK.txt", "adL.txt"]
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'relative/path/to/file/you/want')
for a in enumerate(csvs):
    print(a)
filename = os.path.join(dirname, csvs[int(input())])
while True:
    with open(filename, "r") as spamreaders:
        spamreader = spamreaders.readlines()
        while True:
            c = random.randint(0, len(spamreader)-1)
            b = spamreader[c].count("+") > 0
            d = "+"*b+"*"*((b-1)**2)
            if random.randint(0, 1) == 1:
                if input(d+spamreader[c].split(d)[-1].split(",")[0]+"="+spamreader[c].split(d)[-1].split(",")[-1].strip()[-1]) == "q":
                    print("==========="+spamreader[c][0])
                    break
                print("==========="+spamreader[c][0])
            else:
                if input(spamreader[c].split(",")[0]) == "q":
                    print("==========="+spamreader[c].split(",")[1])
                    break
                print("==========="+spamreader[c].split(",")[1])
    if input("q") != "q":
        break

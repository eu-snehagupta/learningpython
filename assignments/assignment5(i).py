import csv

A = [{"coke": 1 }, {"milk": 2 }, {"curd": 3 }, { "MILK": 1}, {"juice": 3 } ]
B = [{"orange": 1 }, {"papaya": 2 }, {"pineapple": 3 }, { "apple": 1}, {"papaya": 3 } ]
C = [{"jeans": 1 }, {"shirt": 2 }, {"jeans": 3 }, { "milk": 1}, {"SHIRT": 3 } ]
D = [{"HISTORY": 1 }, {"history": 2 }, {"maths": 3 }, { "civics": 1}, {"maths": 3 } ]
data = [A, B, C, D]

newdata_ = dict()
for elements in data:
    for subelements in elements:
        for key, value in subelements.items():
            key_ = key.lower()
            newdata_[key_] =  (newdata_[key_] if key_ in newdata_.keys() else 0) + value
filetowrite = open("datafile.csv", "w")
writer = csv.DictWriter(filetowrite, newdata_.keys())
writer.writeheader()
writer.writerow(newdata_)
filetowrite.close()

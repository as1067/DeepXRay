import csv

class LabelReader:

    def read(self,file="labels.txt"):
        annotations = {}
        with open(file) as file:
            reader = csv.reader(file,delimiter="\t")
            for row in reader:
                name = row[0]
                ls = []
                for i in range(1,len(row)):
                    ls.append(int(i))
                annotations[name] = ls
        print(annotations)
        return annotations

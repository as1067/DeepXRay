import pandas

d = pandas.read_csv("Annotations.csv")
labels = d["Finding Labels"].values
names = d["Image Index"].values
cat2num = {}
label_names = []
cats = []
count = 0
annotations = {}
for i in range(len(names)):
    full = labels[i]
    sep = full.split("|")
    name = names[i]
    ans = []
    for label in sep:
        if label not in label_names:
            label_names.append(label)
            cat2num[label] = count
            count+=1
            cats.append([])
        ans.append(cat2num[label])
    annotations[name] = ans
print(annotations)

file = open("labels.txt","w")
for name in names:
    line = name
    for l in annotations[name]:
        line+="\t"+str(l)
    file.write(line+'\n')

print(len(names))
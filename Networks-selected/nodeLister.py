import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",type = str ,required=True,help="input name")
args = vars(ap.parse_args())

myFile = open(args["input"],"r")
myFile.readline()
nodes = []

for line in myFile.readlines():
    line = (line.strip()).split()
    source = line[0]
    target = line[1]
    if '"'+source+'"' not in nodes:
        nodes.append('"'+source+'"')
    if '"'+source+'"' not in nodes:
        nodes.append('"'+target+'"')

filename = "json/"+args["input"][:-4]+"_nodes.txt"

f = open(filename,"w")

f.write(("var "+args["input"][:-9]+"_nodes = ["+", ".join(nodes)+"]"))

f.close()
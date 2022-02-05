import argparse
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input",type = str ,required=True,help="input name")
ap.add_argument("-c", "--cluster",type = str ,required=True,help="cluster file")
#ap.add_argument("-d", "--description",type = str ,required=True,help="description file")
ap.add_argument("-f", "--flag", default=False, action="store_true", help="Flag to indicate clustering")

args = vars(ap.parse_args())

# descriptionFile = open(args["description"],"r")
# descriptionFile.readline()
# des = {}
description  = "temp"
# for line in descriptionFile.readlines():
#     line = (line.strip()).split("\t")
#     description = line[1]
#     node = line[3]
#     if node not in des:
#         des[node] = description

networkFile = open(args["input"],"r")
networkFile.readline()
nodes = []
links = [] 

for line in networkFile.readlines():
    line = (line.strip()).split()
    source = line[0]
    target = line[1]
    if source not in nodes:
        nodes.append(source)
    if target not in nodes:
        nodes.append(target)
    links.append((source,target))

cluster = []
clusterFile = open(args["cluster"],"r")
for line in clusterFile.readlines():
    tempNode = line.strip()
    if tempNode not in cluster:
        cluster.append(tempNode)

f = open("networks.js","a")

f.write(("\n\nvar "+args["input"][:-9]+"_network = "+'{\n"nodes": [\n'))

for node in nodes:
    if args["flag"]:
        if node in cluster:
            if nodes.index(node) != len(nodes)-1:
                f.write(('{"id": "'+node+'", "colorCode":1, "description":"'+description+'"},\n'))
            else:
                f.write(('{"id": "'+node+'", "colorCode":1, "description":"'+description+'"}\n'))
        else:
            if nodes.index(node) != len(nodes)-1:
                f.write(('{"id": "'+node+'", "colorCode":0, "description":"'+description+'"},\n'))
            else:
                f.write(('{"id": "'+node+'", "colorCode":0, "description":"'+description+'"}\n'))
    else:
        if nodes.index(node) != len(nodes)-1:
            f.write(('{"id": "'+node+'", "colorCode":0, "description":"'+description+'"},\n'))
        else:
            f.write(('{"id": "'+node+'", "colorCode":0, "description":"'+description+'"}\n'))

f.write('],\n "links": [\n')

for tuple in links:
    if links.index(tuple) != len(links)-1:
        f.write(('{"source": "'+tuple[0]+'", "target": "'+tuple[1]+'"},\n'))
    else:
         f.write(('{"source": "'+tuple[0]+'", "target": "'+tuple[1]+'"}\n'))

f.write('  ]\n}\n')

networkFile.seek(0)
networkFile.readline()

nodes = []
for line in networkFile.readlines():
    line = (line.strip()).split()
    source = line[0]
    target = line[1]
    if '"'+source+'"' not in nodes:
        nodes.append('"'+source+'"')
    if '"'+source+'"' not in nodes:
        nodes.append('"'+target+'"')
f.write(("var "+args["input"][:-9]+"_nodes = ["+", ".join(nodes)+"]"))

f.close()
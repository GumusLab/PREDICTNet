import argparse
ap = argparse.ArgumentParser()

ap.add_argument("-m", "--markers",type = str ,required=True,help="markers dataset")
ap.add_argument("-t", "--table",type = str ,required=True,help="table for conversion")

args = vars(ap.parse_args())

markerfile = open(args["markers"],"r")
tablefile = open(args["table"])
outfile = open("markers_geneid.txt","w")

conv = {}

tablefile.readline()
for line in tablefile.readlines():
    line = line.strip().split("\t")
    conv[line[0]] = line[3]


for line in markerfile.readlines():
    if "marker" not in line:
        outfile.write(line)
    else:
        line2 = (line.strip()).split(":")
        somalogic = line2[1][1:-2]
        if somalogic in conv:
            new_id = conv[somalogic]
            outfile.write(("\t"+line2[0]+':"'+new_id+'",\n'))
        else:
            outfile.write(line)

markerfile.close()
tablefile.close()
outfile.close()




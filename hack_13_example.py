import sys

# check to make sure that there are the right number of arguments
if len(sys.argv) != 3:
    print("usage {} <input file> <output file>".format(sys.argv[0]))
    sys.exit()

lineno = 1
with open(sys.argv[1], 'rb') as infile:
    with open(sys.argv[2], 'wb') as outfile:
        for line in infile:
            outfile.write("{}: ".format(lineno) + line)
            lineno += 1

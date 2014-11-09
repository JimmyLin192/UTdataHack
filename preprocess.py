############################################################
##    FILENAME:   preprocess.py    
##    VERSION:    1.0
##    SINCE:      2014-11-14
##    AUTHOR: 
##        Jimmy Lin <jimmylin@cs.utexas.edu>*
##        Hsiang-Fu Yu <rofuyu@cs.utexas.edu>
##        Zhong Kai <zhongkai@ices.utexas.edu>
##        Ian Yen <ianyen@cs.utexas.edu>   
##
############################################################
##    Edited by MacVim
##    Documentation auto-generated by Snippet 
############################################################

FEAT_SEP = " "
INS_SEP = "\n"

## TODO: convert data to libsvm format
f = open ("data", "rb+")

strings = []
for row in f:
    ins = row.strip(INS_SEP)
    ins = ins.split(FEAT_SEP)

    ins_str = ""
    ## TODO: add label to string
    # ins_str += str(label)
    ## TODO: add features to string
    for i in range(0, len(ins)):
        if i != 0: ins_str += " "
        ins_str += str(i+1) + ":" + str(ins[i])
        print(ins_str)
    strings.append(ins_str)

f.close()

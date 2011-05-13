import sys
if len(sys.argv) < 3:
    print 'Input format: python parse.py [file_in1] [file_in2] ... [file_out]'
    quit()
fout = open(sys.argv[len(sys.argv) - 1],'w')
fout.write('experiment,data\n');
i = 1
for file_input in sys.argv[1:-1]:
    fin = open(file_input,'r')
    fout.write(str(i) + ',')
    fout.write(fin.read().replace(",",";").replace("\n","|"))
    fout.write('\n')
    i+=1
    fin.close()
fout.close()
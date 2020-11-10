import re
import pandas as pd

files = {'k80gpu.out','p100gpu.out','v100gpu.out'}

f = open('stat.csv','a')
nprocs = []
gflops = []
dataset = []
gputypes = []
bw =[]

for filepath in files:
    if re.search("^(k80gpu.out)", filepath):
        gputype = ('K80')
    elif re.search("^(p100gpu.out)", filepath):
        gputype = ('P100')
    elif re.search("^(v100gpu.out)", filepath):
        gputype = ('V100')

    with open(filepath,"r") as file_object:
        for lines in file_object:
            line = lines.strip()
            if re.search("totGFLOPS:",line):
                x = re.search("totGFLOPS:",line)
                x = re.search("[0-9]+[.][0-9]+",line[x.start():])
                print(x.group(0))
                gflops.append(float(x.group(0)))
                gputypes.append(gputype)
            if re.search("recon_CDS1.bin",line):
                print('CDS1')
                dataset.append('CDS1')
            if re.search("recon_CDS2.bin",line):
                print('CDS2')
                dataset.append('CDS2')
            if re.search("GB/s tot:",line):
                x = re.search("GB/s tot:",line)
                x = re.search("[0-9]+[.][0-9]+",line[x.start():])
                print(x.group(0))
                bw.append(float(x.group(0)))


f.write('dataset,totGFLOPS,gpu,bw\n')
for i,h,k,m in zip(dataset,gflops,gputypes,bw):
    f.write(i+','+str(h)+','+k+','+str(m)+'\n')
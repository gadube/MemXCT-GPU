import re
import pandas as pd

files = {'scaling2.out'}

f = open('stat_2.csv','a')
nprocs = []
gflops = []
dataset = []
gputypes = []
bw = []
nnodes = []
ap_p = []
c_p = []
r_p = []
tot_p = []
ap_bp = []
c_bp = []
r_bp = []
tot_bp = []

for filepath in files:
    gputype = ('K80')
    # if re.search("^(k80gpu.out)", filepath):
    #     gputype = ('K80')
    # elif re.search("^(p100gpu.out)", filepath):
    #     gputype = ('P100')
    # elif re.search("^(v100gpu.out)", filepath):
    #     gputype = ('V100')

    with open(filepath,"r") as file_object:
        for lines in file_object:
            line = lines.strip()
            if re.search("NUMBER OF PROCESSES    :",line):
                x = re.search("[0-9]+",line)
                nnodes.append(int(x.group(0)))
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
            if re.search("recon:",line):
                if re.search("proj:",line):
                    x = re.search("proj:",line)
                    total_proj = re.search("[0-9]+[.][0-9]+[e][+|-][0-9]+",line[x.start():])
                    ap_proj = re.search("[(][0-9]+[.][0-9]+[e][+|-][0-9]+",line[x.start():])
                    C_proj = re.search("[ ][0-9]+[.][0-9]+[e][+|-][0-9]+",line[x.start() + ap_proj.start():])
                    R_proj = re.search("[0-9]+[.][0-9]+[e][+|-][0-9]+[)]",line[C_proj.start() + x.start() + ap_proj.start():])
                    ap_proj = ap_proj.group(0)[1:]
                    C_proj = C_proj.group(0)[1:]
                    R_proj = R_proj.group(0)[:-1]
                    total_proj = total_proj.group(0)
                    ap_p.append(float(ap_proj))
                    c_p.append(float(C_proj))
                    r_p.append(float(R_proj))
                    tot_p.append(float(total_proj))
                if re.search("backproj:",line):
                    x = re.search("backproj:",line)
                    total_bproj = re.search("[0-9]+[.][0-9]+[e][+|-][0-9]+",line[x.start():])
                    R_bproj = re.search("[(][0-9]+[.][0-9]+[e][+|-][0-9]+",line[x.start():])
                    C_bproj = re.search("[ ][0-9]+[.][0-9]+[e][+|-][0-9]+",line[x.start() + R_bproj.start():])
                    ap_bproj = re.search("[0-9]+[.][0-9]+[e][+|-][0-9]+[)]",line[C_bproj.start() + x.start() + R_bproj.start():])
                    ap_bproj = ap_bproj.group(0)[:-1]
                    C_bproj = C_bproj.group(0)[1:]
                    R_bproj = R_bproj.group(0)[1:]
                    total_bproj = total_bproj.group(0)
                    ap_bp.append(float(ap_bproj))
                    c_bp.append(float(C_bproj))
                    r_bp.append(float(R_bproj))
                    tot_bp.append(float(total_bproj))


f.write('Dataset,GFLOPS,gpu,BW,Ap_proj,C_proj,R_proj,Tot_proj,Ap_bproj,C_bproj,R_bproj,Tot_bproj,Nodes\n')
for a,b,c,d,e,F,g,h,i,j,k,l,m in zip(dataset,gflops,gputypes,bw,ap_p,c_p,r_p,tot_p,ap_bp,c_bp,r_bp,tot_bp,nnodes):
    f.write(a+','+str(b)+','+c+','+str(d)+','+str(e)+','+str(F)+','+str(g)+','+str(h)+','+str(i)+','+str(j)+','+str(k)+','+str(l)+','+str(m)+'\n')
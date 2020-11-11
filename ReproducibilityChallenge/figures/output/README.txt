This directory contains all figures used.

CDS1.png                - Fiji generated reconstruction from MemXCT of CDS1
CDS2.png                - Fiji generated reconstruction from MemXCT of CDS2
CDS1_strong_scaling.png - Reproduced strong scaling figure for CDS1
CDS2_strong_scaling.png - Reproduced strong scaling figure for CDS2
CPU-GPU_bw.png          - Reproduced memory bandwidth utilization
CPU-GPU_perf.png        - Reproduced single CPU-GPU performance 

Although our results were not accurate to those produced in the paper, 
many similar trends exist between the two sets of results. Single CPU-GPU 
performance tests show similar results to the paper in terms of performance,
but differ in memory bandwidth utilization due to a lack of similar hardware
on Azure. Our strong scaling results present very similar trends to those seen 
in the MemXCT paper on a small number of nodes. Increasing this scale would 
provide similar results to those discussed in the paper. Reproducing these results
confirm validity of the results presented by the MemXCT paper and show that 
this application is capable of running on a variety of different hardware with 
consistent performance.

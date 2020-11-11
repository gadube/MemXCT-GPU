This folder contains the run scripts used in the reproducibility experiments.

Single CPU-GPU Performance Run Scripts:
  source ./k80run.sh   #Runs the test for K80 nodes 
  source ./p100run.sh  #Runs the test for P100 nodes 
  source ./v100run.sh  #Runs the test for V100 nodes 

Strong Scaling Run Scripts:
  qsub azure_scaling.pbs    #PBS script used for job submission
  source ./run.sh.azure.CDS1         #Used to run one test for CDS1
  source ./run.sh.azure.CDS2         #Used to run one test for CDS2

NOTE: The only updates to the environment from what was performed in the 
      original MemXCT run scripts are:
         PROJBLOCK=128   <--    PROJBLOCK=512 
         BACKBLOCK=128   <--    BACKBLOCK=512 
         PROJBUFF=8      <--    PROJBUFF=48
         BACKBUFF=8      <--    BACKBUFF=48
NOTE: The azure_scaling.pbs script can be modified to run on other
      schedulers. This experiment used 4 nodes, with 1 MPI process per
      node and 12 OpenMP threads per node.

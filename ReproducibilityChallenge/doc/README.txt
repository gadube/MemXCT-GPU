This digital artifact is organized as follows:

ReproducibilityChallenge/
  compile/
    gpuinit.sh           - MemXCT compilation script
    cpuinit.sh           - MemXCT compilation script
    p100init.sh          - MemXCT compilation script
    v100init.sh          - MemXCT compilation script
    vectorization.txt    - vectorization report 
    mpi_build_install.sh - MPI install and build/ create modulefile script
    environment.txt      - Environment of master node at run
    README.txt           - Explanation of how scripts work
  doc/
    README.txt - Readme describing contents of artifact
    report.pdf - Final Reproducibility Report
  figures/
    output/
      CDS1_strong_scaling.png - Strong scaling figure for CDS1 (Figure 11)
      CDS2_strong_scaling.png - Strong scaling figure for CDS2 (Figure 11)
      CPU-GPU_perf.png        - CPU-GPU Performance figure (Figure 9)
      CPU-GPU_bw.png          - CPU-GPU Bandwidth figure (Figure 9)
      CDS1.png                - Fiji visualization for CDS1 reconstruction
      CDS2.png                - Fiji visualization for CDS2 reconstruction
      README.txt              - Explanation of each image and figure
    scripts/
      graph_scaling.py - Script used to generate strong scaling figure
      graph_perf.py    - Script used to generate CPU-GPU performance figure
      run_parse.py     - Script for parsing output file
      README.txt       - Explanation of how scripts work
  run/
    output/
      scaling.out          - output from strong scaling tests
      k80gpu.out           - output from single CPU-GPU tests on k80
      p100gpu.out          - output from single CPU-GPU tests on p100
      v100gpu.out          - output from single CPU-GPU tests on v100
      recon_CDS1.bin       - output reconstruction image binary file for CDS1
      recon_CDS2.bin       - output reconstruction image binary file for CDS2
    scripts/
      azure_scaling.pbs   - PBSPro script to start batch job for scaling
      k80run.sh           - Run script for CPU-GPU Performance (K80)
      p100run.sh          - Run script for CPU-GPU Performance (P100)
      v100run.sh          - Run script for CPU-GPU Performance (V100)
      run.sh.azure.CDS1   - Single run script and env setup for CDS1
      run.sh.azure.CDS2   - Single run script and env setup for CDS1
      README.txt          - Explanation of run scripts


NOTE: README.txt files in individual directories contain specific information on
      the scripts and outputs in that specific file.


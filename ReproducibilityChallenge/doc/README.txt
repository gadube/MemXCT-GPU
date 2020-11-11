This digital artifact is organized as follows:

ReproducibilityChallenge/
  compile/
    gpuinit.sh        - MemXCT compilation script
    vectorization.txt - vectorization report from compiler
    README.txt        - Explanation of how scripts work
  doc/
    README.txt - Readme describing contents of artifact
    report.pdf - Final Reproducibility Report
  figures/
    output/
      CDS1_strong_scaling.png - Strong scaling figure for CDS1 (Figure 11)
      CDS2_strong_scaling.png - Strong scaling figure for CDS2 (Figure 11)
      CPU-GPU_Performance.png - CPU-GPU Performance figure (Figure 9)
      CPU-GPU_Bandwidth.png   - CPU-GPU Bandwidth figure (Figure 9)
      recon_CDS1.png          - Fiji visualization for CDS1 reconstruction
      recon_CDS2.png          - Fiji visualization for CDS2 reconstruction
    scripts/
      graph_scaling.py - Script used to generate strong scaling figure
      graph_perf.py    - Script used to generate CPU-GPU performance figure
  run/
    output/
      scaling_output.txt     - output from strong scaling tests
      k80_performance_output.txt - output from single CPU-GPU tests on k80
      p100_performance_output.txt - output from single CPU-GPU tests on p100
      v100_performance_output.txt - output from single CPU-GPU tests on v100
    scripts/
      azure_scaling.pbs - PBSPro script to start batch job for scaling
      azure_perf.pbs    - PBSPro script to start batch job for single CPU-GPU performance 



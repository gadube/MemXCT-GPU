Compiler Versions:
  gcc/9.2.0
  cuda/11.1
  openmpi/4.0.3

Compilation is performed by running the following:
  source ./gpuinit.sh       #for GPU (K80) runs
  source ./p100init.sh       #for GPU (P100) runs
  source ./v100init.sh       #for GPU (V100) runs
  source ./cpuinit.sh       #for CPU runs

This should provide the executable 'memxct' in the $HOME/MemXCT/ directory after
loading an openmpi module and installing CUDA 11.1

NOTE: If the openmpi/4.0.3 software and modulefile are not already installed,
      the file ./mpi_build_install.sh should be run before running any of the
      other initialization files. This file can be updated to install any version
      of openmpi and install modulefiles to whichever directory is preferred.

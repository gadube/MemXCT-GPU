This directory contains scripts used for creating figures.

run_parse.py      -Python file used to convert raw data into a *.csv dataset
graph_scaling.py  -Python script used to generate scaling plots from run_parse.py *.csv file
graph_single.py   -Python script used to generate CPU-GPU performance plots from run_parse.py *.csv file

run_parse.py and graphing scripts should be run in the same directory (where the results/output/log file is located).

Visualization of reconstructed output is done with Fiji using the following method:
  1. select File > Import > RAW
  2. Choose recon_CDS*.bin file
  3. set Width/Height equal to [CDS1: 512, CDS2: 1024]
  4. select Little-endian byte order
  5. select OK

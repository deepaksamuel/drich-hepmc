
# DRICH n-sigma analysis for EIC
## 20 Sep 2023:  
This folder contains the code to generate hepmc files for the analysis and the hepmc files as well.  

The original .C  code was provided by Dr. Chandradoy Chatterjee. Thanks Chandra!
It was modified by me to generate a unique file name with the first part indicating the pid, followed by the momentum (GeV) and then the eta bin id. 0 indicates 1.5-2.5  and 1 indicates 2.5 to 3.5.

Running  `python generate_hep_mc.py`  will generate all the hepmc files for the momentum range, pid range and etabin range in the code, in a parallel code.
It took about less than 30 seconds to generate all the files in this directory.

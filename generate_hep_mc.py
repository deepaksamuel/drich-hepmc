
# import numpy as np

# def generate_and_execute_statements():
#     # Get ranges from user input
#     nevents=10000


#     for bin in bin_id_range:
#         for mom in mom_range:
#             for pid in  pid_range:
#                 statement = f"root -l 'drich_hepmc_writer_sp.C({nevents},{bin},{mom},{pid})'"
#                 print(statement)
#                 subprocess.run(statement, shell=True)  # Execute the statement

# if __name__ == "__main__":
#     generate_and_execute_statements()


import multiprocessing
import numpy as np
import subprocess

nevents=10000
bin_id_range =[0,1]
mom_range=np.arange(0.5,60.5,0.5)
pid_range=[211,2212,321]

def execute_statement(statement):
  subprocess.run(statement, shell=True)

def generate_and_execute_statements():
    # ... your existing code ... 
    with multiprocessing.Pool() as pool:
        statements = [
            f"root -l 'drich_hepmc_writer_sp.C({nevents},{bin},{mom},{pid})'"
            for bin in bin_id_range
            for mom in mom_range
            for pid in pid_range
        ]
        pool.map(execute_statement, statements)

if __name__ == "__main__":
    generate_and_execute_statements()
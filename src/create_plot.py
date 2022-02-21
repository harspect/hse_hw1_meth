import pandas as pd
from matplotlib import pyplot as plt

def create_plot(id):
  path = f'/content/s_{id}_1_bismark_bt2_pe.deduplicated.bedGraph'
  bg = pd.read_csv(path,  delimiter='\t', skiprows=1, header=None)
  with plt.style.context('seaborn'):  
    fig = plt.figure(figsize=(15, 5))
    plt.title(id) 
    plt.hist(bg[3], bins=100, density=True)
    plt.xlabel('Percentage')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

l = ['SRR3824222', 'SRR5836473', 'SRR5836475'];
for one in l:
  create_plot(one)
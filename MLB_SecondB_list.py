### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
SecondB_PCA = pd.read_csv("export/SecondB_pca.csv")

# Extracting Player Names for Positions
SecondB_Info = pd.read_csv("export/SecondB_Names.csv", names = ['Players','Team'])
#print(FirstB_Names)
#FirstB_PCA.drop(['pc1', 'pc2'], axis=1)

#FirstB_max = pd.DataFrame.max(FirstB_PCA['pc1'])
#print(FirstB_max)

# God Player
God = [200,60] # God[0] = -150 and God[1] = 35
# Combining Datasets
SecondB = SecondB_PCA.join(SecondB_Info)
#print(FirstB['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(SecondB),1])
count = 0
while count < len(SecondB):
    Closiest_to_God[count][0] = sqrt(((SecondB['pc1'][count] - God[0])**2) + ((SecondB['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = FirstB_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(SecondB):
        break
print(len(Closiest_to_God))
print(len(SecondB_Info))
Closiest_to_God = np.hstack((Closiest_to_God, SecondB_Info[1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/SecondB_List.csv', index = None, header=True)
print(dataset)

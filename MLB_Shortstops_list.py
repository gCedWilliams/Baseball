### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
Shortstops_PCA = pd.read_csv("export/Shortstops_pca.csv")

# Extracting Player Names for Positions
Shortstops_Names = pd.read_csv("export/Shortstops_Names.csv", names = ['Players','Team'])
#print(Shortstops_Names)
#Shortstops_PCA.drop(['pc1', 'pc2'], axis=1)

#Shortstops_max = pd.DataFrame.max(Shortstops_PCA['pc1'])
#print(Shortstops_max)

# God Player
God = [200,0] # God[0] = -150 and God[1] = 35
# Combining Datasets
Shortstops = Shortstops_PCA.join(Shortstops_Names)
#print(Shortstops['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(Shortstops),1])
count = 0
while count < len(Shortstops):
    Closiest_to_God[count][0] = sqrt(((Shortstops['pc1'][count] - God[0])**2) + ((Shortstops['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = Shortstops_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(Shortstops):
        break
Closiest_to_God = np.hstack((Closiest_to_God, Shortstops_Names[1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/Shortstops_List.csv', index = None, header=True)
print(dataset)

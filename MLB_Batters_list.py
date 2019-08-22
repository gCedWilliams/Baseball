### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
Batters_PCA = pd.read_csv("export/Batters_pca.csv")

# Extracting Player Names for Positions
Batters_Names = pd.read_csv("export/Batters_Names.csv", names = ['Players','Team'])
#print(Batters_Names)
#Batters_PCA.drop(['pc1', 'pc2'], axis=1)

#Batters_max = pd.DataFrame.max(Batters_PCA['pc1'])
#print(Batters_max)

# God Player
God = [200,40] # God[0] = -150 and God[1] = 35
# Combining Datasets
Batters = Batters_PCA.join(Batters_Names)
#print(Batters['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(Batters_Names),1])
count = 0
while count < len(Batters):
    Closiest_to_God[count][0] = sqrt(((Batters['pc1'][count] - God[0])**2) + ((Batters['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = Batters_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(Batters):
        break
print(len(Closiest_to_God))
print(len(Batters_Names['Players']))
print(len(Batters_Names['Team']))
Closiest_to_God = np.hstack((Closiest_to_God, Batters_Names['Players'][1:],Batters_Names['Team'][1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/Batters_List.csv', index = None, header=True)
print(dataset)

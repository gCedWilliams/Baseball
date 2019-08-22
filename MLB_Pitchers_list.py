### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
Pitchers_PCA = pd.read_csv("export/Pitchers_pca.csv")

# Extracting Player Names for Positions
Pitchers_Names = pd.read_csv("export/Pitchers_Names.csv", names = ['Players','Team'])
#print(Pitchers_Names)
#Pitchers_PCA.drop(['pc1', 'pc2'], axis=1)

#Pitchers_max = pd.DataFrame.max(Pitchers_PCA['pc1'])
#print(Pitchers_max)

# God Player
God = [150,20] # God[0] = -150 and God[1] = 35
# Combining Datasets
Pitchers = Pitchers_PCA.join(Pitchers_Names)
#print(Pitchers['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(Pitchers),1])
count = 0
while count < len(Pitchers):
    Closiest_to_God[count][0] = sqrt(((Pitchers['pc1'][count] - God[0])**2) + ((Pitchers['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = Pitchers_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(Pitchers):
        break
Closiest_to_God = np.hstack((Closiest_to_God, Pitchers_Names[1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/Pitchers_List.csv', index = None, header=True)
print(dataset)

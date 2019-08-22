### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
Outfielders_PCA = pd.read_csv("export/Outfielders_pca.csv")

# Extracting Player Names for Positions
Outfielders_Names = pd.read_csv("export/Outfielders_Names.csv", names = ['Players','Team'])
#print(Outfielders_Names)
#Outfielders_PCA.drop(['pc1', 'pc2'], axis=1)

#Outfielders_max = pd.DataFrame.max(Outfielders_PCA['pc1'])
#print(Outfielders_max)

# God Player
God = [200,0] # God[0] = -150 and God[1] = 35
# Combining Datasets
Outfielders = Outfielders_PCA.join(Outfielders_Names)
#print(Outfielders['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(Outfielders),1])
count = 0
while count < len(Outfielders):
    Closiest_to_God[count][0] = sqrt(((Outfielders['pc1'][count] - God[0])**2) + ((Outfielders['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = Outfielders_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(Outfielders):
        break
Closiest_to_God = np.hstack((Closiest_to_God, Outfielders_Names[1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/Outfielders_List.csv', index = None, header=True)
print(dataset)

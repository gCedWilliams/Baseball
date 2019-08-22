### MLB ALL Create a list of the 10 best players to pick for a position

## Packages/funcitions
import csv
import numpy as np
from math import sqrt
import pandas as pd
from pandas import DataFrame

# Extracting PCA vectors
Catchers_PCA = pd.read_csv("export/Catchers_pca.csv")

# Extracting Player Names for Positions
Catchers_Names = pd.read_csv("export/Catchers_Names.csv", names = ['Players','Team'])
#print(Catchers_Names)
#Catchers_PCA.drop(['pc1', 'pc2'], axis=1)

#Catchers_max = pd.DataFrame.max(Catchers_PCA['pc1'])
#print(Catchers_max)

# God Player
God = [200,20] # God[0] = -150 and God[1] = 35
# Combining Datasets
Catchers = Catchers_PCA.join(Catchers_Names)
#print(Catchers['pc1'][0])

# create list of the best Players
Closiest_to_God = np.empty([len(Catchers),1])
count = 0
while count < len(Catchers):
    Closiest_to_God[count][0] = sqrt(((Catchers['pc1'][count] - God[0])**2) + ((Catchers['pc2'][count] - God[1])**2))
    #Closiest_to_God[count][1] = Catchers_Names['Players'][count+1]
    #print(Closiest_to_God[count][0])
#    print(count)
    count += 1
    if count >= len(Catchers):
        break
Closiest_to_God = np.hstack((Closiest_to_God, Catchers_Names[1:]))
# Attaches the names of each player to their Euclidean distance to God

Closiest_to_God = Closiest_to_God[Closiest_to_God[:,0].argsort()]
print(Closiest_to_God)

##Export to CSV
dataset = DataFrame(Closiest_to_God)
df= dataset.to_csv (r'export/Catchers_List.csv', index = None, header=True)
print(dataset)

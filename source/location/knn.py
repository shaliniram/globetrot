#!/usr/bin/env python
import numpy as np
import pandas as pd

import sklearn
from sklearn.neighbors import NearestNeighbors

def geeks(r1,  r2,  r3,  r4,  r5, r6,  r7, r8):
    igis=pd.read_csv(r"findlocation\\out.csv")
    igis.columns=['City','Landmark','House of Worship','Pilgrimage','Archaeological Site','Shoreline','Waterside','Woods','Hill Station','Urban Area','State']
    igis.head()

    t=[ r1,  r2,  r3,  r4,  r5, r6,  r7, r8]

    x=igis.ix[:,(2,3,4,5,6,7,8,9)].values
    x[0:10]

    nbrs=NearestNeighbors(n_neighbors=5).fit(x)

    print(nbrs.kneighbors([t])[1])

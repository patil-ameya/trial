import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter

style.use('ggplot')
plt.figure(figsize=(5,5))
dataset={'postive':[[4,4],[6,2]],'negative':[[2,4],[4,2],[6,4],[4,6]]}
point=[6,6]
colors=['blue','orange']
marker=['o','s']
k=0

def knn(data,predict,k=3):
    if len(data)>=k:
        warnings.warn('K is set to less value')

    distances=[]
    for group in data:
        for features in data[group]:
            euc_dist=np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euc_dist,group])

    votes=[i[1] for i in sorted(distances)[:k]]
    vote_result=Counter(votes).most_common(1)[0][0]
    return vote_result

for i in dataset:
    for j in dataset[i]:
        plt.scatter(j[0],j[1],s=80,c=colors[k],marker=marker[k])
    k=k+1

result=knn(dataset,point)
if result == 'positive':
    color='blue'
    marker='o'

else:
    color='orange'
    marker='s'

plt.scatter(point[0],point[1],s=200,c=color,marker=marker)
plt.show()

print(result)

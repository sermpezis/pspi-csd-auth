import numpy as np

R = np.array([[np.nan,np.nan,4,np.nan,np.nan,2],
	      [5, np.nan,4, np.nan,np.nan,1],
		  [4, np.nan,5, np.nan, 2, np.nan],
		  [np.nan,1, np.nan, 5, np.nan, 4],
		  [2, np.nan, np.nan, 4, 5, np.nan],
		  [4, 5, np.nan, 1, np.nan, np.nan]])


print('Ratings matrix')
print(R)
print()



def inner_product(x,y):
	return np.nansum([x[i]*y[i] for i in range(len(x))])

def norm2(x):
	return np.sqrt(np.nansum([x[i]*x[i] for i in range(len(x))]))


simil = np.zeros(R.shape)
for i in range(R.shape[0]):
	for j in range(R.shape[0]):
		x = R[i,:]
		y = R[j,:]
		simil[i,j] = inner_product(x,y)/(norm2(x)*norm2(y))


print('Similarities matrix')
print(simil)
print()



predictions = np.array(R)
for i in range(R.shape[0]):
	for j in range(R.shape[1]):
		if np.isnan(R[i,j]):
			k = 1/np.nansum([simil[i,u] for u in range(R.shape[0]) if ~np.isnan(R[u,j])])
			print(k)
			predictions[i,j] = k * np.nansum([simil[i,u]*R[u,j] for u in range(R.shape[0]) if ~np.isnan(R[u,j])])
	

print('Predictions matrix')
print(predictions)
print()
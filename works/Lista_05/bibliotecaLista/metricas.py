def mse(y, y_pred):
    return np.sum(( y - y_pred ) ** 2) / y.shape[0]

def rmse(y, y_pred):
    return mse(y, y_pred) ** 0.5
	import numpy as np

def Standardization(x):
	x_np = np.asarray(x)
	z_scores_np = (x_np - x_np.mean()) / x_np.std()
	return z_scores_np

def Normal(x):
	x_np = np.asarray(x)
	np_minmax = (x_np - x_np.min()) / (x_np.max() - x_np.min())
	return np_minmax
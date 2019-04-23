from sklearn.neighbors import KNeighborsClassifier
class Metric(object):
	def accuracy(self,y_test,y_pred):
		NUMaccuracy = np.sum(y_pred == y_test) / y_test.shape[0]
		return NUMaccuracy
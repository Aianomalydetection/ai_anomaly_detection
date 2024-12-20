from sklearn.cluster import KMeans

class ClusteringModel:
    def __init__(self, n_clusters=2):
        self.model = KMeans(n_clusters=n_clusters)

    def train(self, data):
        self.model.fit(data)

    def predict(self, data):
        return self.model.predict(data)

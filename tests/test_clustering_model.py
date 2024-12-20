from src.models.clustering_model import ClusteringModel

def test_clustering_model():
    data = [[0.1, 0.2], [0.15, 0.25], [5.0, 5.2]]
    model = ClusteringModel()
    model.train(data)
    result = model.predict([[5.1, 5.3]])
    assert result[0] == 1

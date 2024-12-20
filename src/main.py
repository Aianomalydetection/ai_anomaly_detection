from src.models.clustering_model import ClusteringModel
from src.pipeline.data_pipeline import preprocess, postprocess

data = [[0.1, 0.2], [0.15, 0.25], [5.0, 5.2]]

# Preprocessing
processed_data = preprocess(data)

# Model Training and Prediction
model = ClusteringModel()
model.train(processed_data)
result = model.predict([[5.1, 5.3]])

# Postprocessing
final_result = postprocess(result)
print("Anomaly detected:" if final_result[0] else "No anomaly detected")

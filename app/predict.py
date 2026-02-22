from collections import Counter
from .model_loader import yolo_model, rf_model, label_encoder

def predict_image(image_path):

    results = yolo_model(image_path, conf=0.5)
    result = results[0]
    boxes = result.boxes

    if len(boxes) == 0:
        return {
            "counts": {},
            "severity": "Safe"
        }

    class_ids = boxes.cls.tolist()
    class_names = [yolo_model.names[int(i)] for i in class_ids]
    count_dict = Counter(class_names)

    total = sum(count_dict.values())

    feature_vector = [
        total,
        count_dict.get("brown-planthopper", 0),
        count_dict.get("stem-borer", 0),
        count_dict.get("rice-bug", 0),
        count_dict.get("green-leafhopper", 0)
    ]

    prediction = rf_model.predict([feature_vector])
    severity = label_encoder.inverse_transform(prediction)[0]

    return {
        "counts": dict(count_dict),
        "severity": severity
    }
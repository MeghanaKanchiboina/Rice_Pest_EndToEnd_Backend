import os
from ultralytics import YOLO
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

YOLO_PATH = os.path.join(MODEL_DIR, "best.pt")
RF_PATH = os.path.join(MODEL_DIR, "random_forest.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

print("Loading YOLO model...")
yolo_model = YOLO(YOLO_PATH)

print("Loading Random Forest model...")
rf_model = joblib.load(RF_PATH)

print("Loading Label Encoder...")
label_encoder = joblib.load(ENCODER_PATH)

print("Models loaded successfully!")
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
import os
# ========== STEP 1: Load & Clean Dataset ==========
# Make sure this path is correct on your local system and the file exists there.
# If you are using the file I generated, it's 'synthetic_crop_data_all_crops.csv'
df_crop_recommendation = pd.read_csv("C:/Users/AzrielLucifer/PycharmProjects/FlaskProject/synthetic_crop_data_all_crops.csv")

# CORRECTED COLUMN NAMES based on the generated dataset's headers
required_columns = [
    'N', 'P', 'K',
    'Temperature(C)', 'Humidity(%)', 'Soil_pH', 'Moisture(%)',
    'Crop', 'Region', 'Month', 'Fertilizer'
]

# Ensure all required columns are present - USING df_crop_recommendation
for col in required_columns:
    if col not in df_crop_recommendation.columns:
        raise ValueError(f"Missing column in dataset: {col}. Available columns are: {df_crop_recommendation.columns.tolist()}")

# Clean whitespace & casing - USING df_crop_recommendation
for cat_col in ['Crop', 'Region', 'Month', 'Fertilizer']:
    df_crop_recommendation[cat_col] = df_crop_recommendation[cat_col].astype(str).str.strip().str.lower()

# ========== STEP 2: Encode Categorical Features ==========
label_encoders = {}
dropdowns = {}

for col in ['Crop', 'Region', 'Month']:
    le = LabelEncoder()
    df_crop_recommendation[col] = le.fit_transform(df_crop_recommendation[col]) # USING df_crop_recommendation
    label_encoders[col] = le
    dropdowns[col] = sorted(le.classes_)

fertilizer_encoder = LabelEncoder()
df_crop_recommendation['Fertilizer'] = fertilizer_encoder.fit_transform(df_crop_recommendation['Fertilizer']) # USING df_crop_recommendation

# ========== STEP 3: Feature Scaling ==========
X = df_crop_recommendation.drop('Fertilizer', axis=1) # USING df_crop_recommendation
y = df_crop_recommendation['Fertilizer'] # USING df_crop_recommendation

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

y_encoded = to_categorical(y)

# ========== STEP 4: Split Dataset for Validation ==========
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# ========== STEP 5: Define ANN Model ==========
model = Sequential([
    Dense(128, input_dim=X.shape[1], activation='relu'),
    BatchNormalization(),
    Dropout(0.4),

    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),

    Dense(128, activation='relu'),
    Dropout(0.3),

    Dense(y_encoded.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# ========== STEP 6: Train with Early Stopping ==========
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

# ========== STEP 7: Save Model and Tools ==========
model.save("model.h5")

with open("encoders.pkl", "wb") as f:
    pickle.dump({
        "label_encoders": label_encoders,
        "fertilizer_encoder": fertilizer_encoder,
        "dropdowns": dropdowns
    }, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model training complete and saved as model.h5")
print("✅ LabelEncoders, Scaler, and dropdown values saved as pkl files")

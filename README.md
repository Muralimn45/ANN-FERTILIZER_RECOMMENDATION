"COMPANY": CODETECT IT SOLUTIONS

"NAME": MURALI N

"INTERN ID": CT04DY169

"DOMAIN": PYTHON PROGRAMMING.

"DURATION": 4 WEEKS

"MENTOR":NEELA SANTHOSH KUMAR

# ANN-FERTILIZER_RECOMMENDATION
"DESCRIPTON":
Fertilizer Recommendation System: Web-Based & ANN-Powered
This project outlines a web-based fertilizer recommendation system that relies on user-provided data and an Artificial Neural Network (ANN) model to generate intelligent and personalized fertilizer suggestions. It's a digital tool designed to help farmers and gardeners make informed decisions without the need for physical sensors.

System Architecture
The system consists of three primary components: the User Interface (Webpage), the Database, and the ANN-ML Model.

1. User Interface (Webpage) 💻
This is the front-end of the system, designed to be intuitive and easy for a user to interact with. The webpage acts as a data collection portal. It features a form where users manually input key information about their soil and crop. The required data fields would typically include:

Soil Nutrient Levels: Manual entry for Nitrogen (N), Phosphorus (P), and Potassium (K) levels, usually obtained from a recent soil test report.

Soil Parameters: Input fields for soil pH, moisture content, and possibly soil type (e.g., clay, loam, sandy).

Crop Information: A dropdown menu or input field to select the specific crop they are growing (e.g., wheat, maize, rice, tomatoes).

Location/Environmental Data: The user might be asked to provide their geographical location, which can be used to automatically fetch local weather data (temperature, rainfall) via an API.

Once all the required information is entered, the user clicks a "Generate Recommendation" button to initiate the analysis.

2. Database 💾
The database serves as the backbone for storing all information. It holds:

Training Data: A massive dataset of historical agricultural information used to train the ANN model. This includes thousands of records containing various combinations of soil parameters, crop types, weather data, and the corresponding optimal fertilizer recommendations that resulted in high yields. This is the most crucial part of the system's intelligence.

User Data: The data entered by users through the webpage is temporarily stored to be passed to the ANN model for analysis.

3. ANN-ML Model 🧠
This is the brain of the system. The ANN is a machine learning algorithm trained on the historical data in the database. Its function is to recognize patterns and relationships between the input variables (soil data, crop, weather) and the desired output (fertilizer recommendation).

Model Training: The ANN is trained offline using the historical dataset. During training, the model learns to associate specific soil and environmental conditions with the ideal fertilizer mix and quantity for a particular crop.

Prediction: When a user submits their data through the webpage, the system sends this new data to the trained ANN model. The model processes this input and predicts the most suitable fertilizer recommendation. The recommendation typically includes:

Fertilizer Type: The specific chemical fertilizers to use (e.g., urea, DAP, MOP).

Dosage: The quantity of each fertilizer needed, often in kilograms per hectare.


The final recommendation is then formatted into a clear, concise output that is displayed back to the user on the webpage. This process provides a quick, data-driven, and personalized solution for managing soil fertility. The system is highly adaptable as the ANN can be retrained with new data to improve its accuracy over time
#OUTPUT :
<img width="1377" height="842" alt="Image" src="https://github.com/user-attachments/assets/a3bed4a2-d00a-4ebf-9637-c17091b3a33c" />

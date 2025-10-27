👇

🌍 CO₂ Emission Prediction App

#APP LINK :- https://co2ete-3mykpc6pm7sehhuvjsg8ma.streamlit.app/

This Streamlit web application predicts the CO₂ emissions (in grams per kilometer) of a vehicle based on its engine and fuel consumption characteristics. The model uses machine learning to estimate emissions, helping users analyze the environmental impact of different vehicle configurations.

📂 Project Structure
CO2_Emission_Prediction/
│
├── app.py                   # Streamlit app file
├── best_model.pkl           # Trained ML model (saved using pickle)
├── requirements.txt         # Dependencies list (optional)
└── README.md                # Project documentation

⚙️ Features Used

The model uses the following features for prediction:

Engine Size (L)

Cylinders

Fuel Consumption City (L/100 km)

Fuel Consumption Hwy (L/100 km)

Fuel Consumption Comb (L/100 km)

Fuel Consumption Comb (mpg)

Target variable:

CO₂ Emissions (g/km)

🚀 How to Run the App

Install Dependencies

pip install streamlit pandas numpy scikit-learn


Ensure Model File Exists
Make sure best_model.pkl is in the same directory as app.py.
If you haven’t saved it yet:

import pickle
with open("best_model.pkl", "wb") as f:
    pickle.dump(model, f)


Run the Application

streamlit run app.py


Use the Interface

Enter the vehicle specifications (engine size, cylinders, fuel consumption details).

Click "Predict CO₂ Emissions" to get the estimated output.

🧠 Model Description

The model was trained on a dataset containing vehicle specifications and their CO₂ emission levels.
Typical algorithms used for this type of regression problem include:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

The trained model was saved as best_model.pkl for prediction in the Streamlit app.

📊 Conclusion

This project demonstrates an end-to-end machine learning regression workflow integrated into an interactive Streamlit web app.
It allows users to predict vehicle CO₂ emissions quickly and easily, promoting awareness about fuel efficiency and environmental impact.

💡 Future Enhancements

Add feature scaling or normalization.

Include additional parameters like vehicle type or fuel type.

Visualize emission trends based on user inputs.

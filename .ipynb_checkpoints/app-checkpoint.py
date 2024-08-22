import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('flight_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("Flight Price Prediction App")

# Numeric inputs
stops = st.number_input("Number of Stops", min_value=0, max_value=3, step=1)

# Select box for flight class with options Economy and Business
flight_class_option = st.selectbox("Class", options=["Economy", "Business"])
# Map the selected class to 0 (Economy) or 1 (Business)
flight_class = 0 if flight_class_option == "Economy" else 1

duration = st.number_input("Duration (hours)", min_value=0.0, max_value=50.0, step=0.1)
days_left = st.number_input("Days Left Until Flight", min_value=0, max_value=365, step=1)

# Radio buttons for categorical features (user will only select one option in each category)
selected_airline = st.radio("Select Airline", options=[
    'Air India', 'GO FIRST', 'Indigo', 'SpiceJet', 'Vistara'
])

selected_source_city = st.radio("Select Source City", options=[
    'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'
])

selected_destination_city = st.radio("Select Destination City", options=[
    'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai'
])

selected_departure_time = st.radio("Select Departure Time", options=[
    'Early Morning', 'Evening', 'Late Night', 'Morning', 'Night'
])

selected_arrival_time = st.radio("Select Arrival Time", options=[
    'Early Morning', 'Evening', 'Late Night', 'Morning', 'Night'
])

# Map the selected options to one-hot encoded values
airlines = {
    'Air India': 0, 'GO FIRST': 0, 'Indigo': 0, 'SpiceJet': 0, 'Vistara': 0
}
airlines[selected_airline] = 1

source_cities = {
    'Chennai': 0, 'Delhi': 0, 'Hyderabad': 0, 'Kolkata': 0, 'Mumbai': 0
}
source_cities[selected_source_city] = 1

destination_cities = {
    'Chennai': 0, 'Delhi': 0, 'Hyderabad': 0, 'Kolkata': 0, 'Mumbai': 0
}
destination_cities[selected_destination_city] = 1

departure_times = {
    'Early Morning': 0, 'Evening': 0, 'Late Night': 0, 'Morning': 0, 'Night': 0
}
departure_times[selected_departure_time] = 1

arrival_times = {
    'Early Morning': 0, 'Evening': 0, 'Late Night': 0, 'Morning': 0, 'Night': 0
}
arrival_times[selected_arrival_time] = 1

# Prepare input data for prediction
input_data = [
    stops,
    flight_class,
    duration,
    days_left,
    airlines['Air India'],
    airlines['GO FIRST'],
    airlines['Indigo'],
    airlines['SpiceJet'],
    airlines['Vistara'],
    source_cities['Chennai'],
    source_cities['Delhi'],
    source_cities['Hyderabad'],
    source_cities['Kolkata'],
    source_cities['Mumbai'],
    destination_cities['Chennai'],
    destination_cities['Delhi'],
    destination_cities['Hyderabad'],
    destination_cities['Kolkata'],
    destination_cities['Mumbai'],
    departure_times['Early Morning'],
    departure_times['Evening'],
    departure_times['Late Night'],
    departure_times['Morning'],
    departure_times['Night'],
    arrival_times['Early Morning'],
    arrival_times['Evening'],
    arrival_times['Late Night'],
    arrival_times['Morning'],
    arrival_times['Night']
]

# Button to make the prediction
if st.button("Predict Price"):
    # Convert input_data to numpy array
    input_data = np.array([input_data])

    # Predict the price
    prediction = model.predict(input_data)

    # Display the result
    st.success(f"The predicted price is ${prediction[0]:.2f}")


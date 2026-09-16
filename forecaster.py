import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)
random.seed(42)

# Generate restaurant waiting-time dataset
data = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = range(10, 20)

for day in range(60):
    day_of_week = days[day % 5]

    for hour in hours:
        wait_time = random.randint(5, 15)

        if hour in [13, 14]:
            wait_time += random.randint(15, 30)

        if hour == 17:
            wait_time += random.randint(10, 20)

        if day_of_week == 'Friday':
            wait_time += random.randint(5, 10)

        data.append([day_of_week, hour, wait_time])

df = pd.DataFrame(
    data,
    columns=['Day_of_Week', 'Hour_of_Day', 'Wait_Time_Minutes']
)

df.to_csv('restaurant_data.csv', index=False)
print("Restaurant dataset created successfully!")

# Convert day names into numbers
le = LabelEncoder()
df['Day_Encoded'] = le.fit_transform(df['Day_of_Week'])

X = df[['Day_Encoded', 'Hour_of_Day']]
y = df['Wait_Time_Minutes']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree model
model = DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print(f"Model Mean Absolute Error: {mae:.2f} minutes")

# User prediction
print("\n--- Restaurant Wait-Time Prediction ---")

day_input = input("Enter day (Monday-Friday): ").capitalize()

if day_input not in days:
    print("Invalid day. Please enter a weekday.")

else:
    try:
        hour_input = int(input("Enter hour (10-19): "))

        if hour_input < 10 or hour_input > 19:
            print("Invalid hour. Enter a value between 10 and 19.")

        else:
            day_encoded = le.transform([day_input])[0]

            predicted_wait = model.predict(
                [[day_encoded, hour_input]]
            )

            print(
                f"Predicted waiting time for {day_input} "
                f"at {hour_input}:00: "
                f"{predicted_wait[0]:.0f} minutes"
            )

    except ValueError:
        print("Please enter the hour as a number.")

# Restaurant Peak Hour Forecaster 🕒

## 📌 Overview

**Restaurant Peak Hour Forecaster** is a machine learning project that predicts restaurant waiting time based on the **day of the week and hour of the day**.

The project uses a **Decision Tree Regressor** to identify non-linear patterns in restaurant traffic and estimate expected waiting time.

> **Note:** The dataset used in this project is synthetically generated for academic purposes.

---

## 🎯 Objectives

* Generate a dataset representing restaurant waiting times.
* Preprocess the data for machine learning.
* Train a Decision Tree Regression model.
* Predict waiting time based on day and hour.
* Evaluate the model using **Mean Absolute Error (MAE)**.

---

## 🚀 Features

* Synthetic restaurant dataset generation
* Data preprocessing
* Decision Tree Regression
* Waiting-time prediction
* Model evaluation using MAE
* User input validation

---

## 🔄 Workflow

```text
Data Generation
      ↓
Data Preprocessing
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
User Input
      ↓
Wait-Time Prediction
```

---

## 📊 Dataset

The project uses a synthetic dataset containing **600 observations** representing 60 simulated days.

Features:

* `Day_of_Week` – weekday
* `Hour_of_Day` – hour of the day
* `Wait_Time_Minutes` – target waiting time

Dataset file:

```text
restaurant_data.csv
```

---

## 🧠 Model

**Decision Tree Regressor**

A Decision Tree was selected because restaurant waiting times can change sharply during peak periods such as lunch and evening hours.

**Evaluation:** 80/20 train-test split using **Mean Absolute Error (MAE)**.

---

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Git & GitHub

---

## ⚙️ Installation & Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/main.py
```

The user can enter a weekday and hour to receive the predicted waiting time.

Example:

```text
Enter day: Wednesday
Enter hour: 13

Predicted waiting time: XX minutes
```

---

## 🧪 Testing

Run the validation tests using:

```bash
python -m pytest
```

Tests cover valid/invalid inputs, dataset generation, and prediction functionality.

---

## ⚠️ Limitations

* Uses synthetic rather than real restaurant data.
* Considers only day and hour as prediction features.
* Does not account for weather, events, holidays, or real-time customer volume.

---

## 🔮 Future Enhancements

* Use real restaurant data.
* Add more prediction features.
* Compare multiple ML models.
* Add graphs and visualizations.
* Develop a web-based interface.

---

## 👨‍

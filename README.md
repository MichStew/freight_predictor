
# 🚛 Freight Cost Predictor

This Streamlit-powered web app predicts freight shipping costs based on user inputs such as panel count, mileage, and truck count. It leverages cleaned historical data and advanced machine learning models to deliver fast and accurate pricing.

🔗 **Live App**: [freight-predictor.streamlit.app](https://freight-predictor.streamlit.app)  
📂 **GitHub Repo**: [Michstew/freight_predictor](https://github.com/Michstew/freight_predictor)

---

## 📈 Model Performance

Trained on a cleaned dataset (excluding outliers and missing values), the model performance is:

| Model           | MAE ($) | R² Score |
|------------------|---------|----------|
| Gradient Boosting | 398.11  | 0.9985   |
| Random Forest     | 482.97  | 0.9945   |
| XGBoost           | 429.83  | 1.0000   |
| LightGBM          | 605.49  | 0.9761   |
| CatBoost          | 468.85  | 0.9997   |

CatBoost and Gradient Boosting offer the best balance of accuracy and generalization.

---

## ⚙️ Features Used

- Panels, Weight, Miles, Trucks
- Fuel cost and engineered features:
  - `weight_per_truck`, `miles_x_fuel`, `trucks_x_miles`
  - `long_miles` flag
- Date components: Year, Month, Day, Weekday

---

## 🚀 Running the App Locally

### 1. Clone the repo
```bash
git clone https://github.com/Michstew/freight_predictor.git
cd freight_predictor
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 💡 Advanced Options

- Apply a 5% quote buffer: `prediction *= 1.05`
- Enable model ensembling or quantile prediction
- Add confidence intervals or fuel price APIs

---

## 👤 Author

**Michael Stewart**  
📫 stew.mich258@gmail.com  
🔗 [GitHub: Michstew](https://github.com/Michstew)

---

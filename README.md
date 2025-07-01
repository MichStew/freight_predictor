
# 📦 Freight Cost Predictor

This is a **Streamlit-powered web app** that predicts freight shipping costs based on user inputs such as number of panels, loaded mileage, and truck count.

🔗 **Live Demo**: [Launch the App](https://freight-predictor.streamlit.app)  
📂 **GitHub Repo**: [Michstew/freight_predictor](https://github.com/Michstew/freight_predictor)

---

## 🔍 How It Works

The app uses a trained `RandomForestRegressor` model built with:

- Preprocessing via `ColumnTransformer`
- Engineered features like:
  - weight per truck
  - miles × fuel cost
  - trucks × miles
  - long-haul mileage flag
- Scikit-learn pipeline saved as `model_pipeline.pkl`

---

## 🧑‍💻 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Michstew/freight_predictor.git
cd freight_predictor
```

### 2. Create a Virtual Environment (optional)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📈 Inputs

| Field            | Description                                 |
|------------------|---------------------------------------------|
| Panels           | Number of panels being shipped              |
| Miles            | Loaded miles (distance)                     |
| Trucks           | Number of trucks used                       |

The app automatically calculates additional features and returns a predicted freight cost.

---

## ⚙️ Model

Trained offline using historical Excel quote data (`Freight Quotes.xlsx`) and exported as a `.pkl` file using `joblib`.

If you want to retrain the model, use `retrain_model.py`.

---

## 📧 Contact

Developed by [Michael Stewart](https://github.com/Michstew)  
📫 Email: stew.mich258@gmail.com

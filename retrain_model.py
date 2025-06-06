import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

# Load and clean data
df = pd.read_excel("Freight Quotes.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.rename(columns={
    '#_of_panels': 'panels',
    'weight_(lbs)': 'weight',
    'loaded_miles': 'miles',
    'avg_fuel_cost_(weekly)': 'fuel_cost',
    'total_cost_($)': 'cost',
    '#_of_trucks': 'trucks',
    'quote_date': 'date_received'
})
df['weight_per_truck'] = np.where(df['weight'] == 0, 0, df['weight'] / 13440)
df['miles_x_fuel'] = df['miles'] * df['fuel_cost']
df['trucks_x_miles'] = df['trucks'] * df['miles']
df['long_miles'] = (df['miles'] > 500).astype(int)
df['date_received'] = pd.to_datetime(df['date_received'])
df['year'] = df['date_received'].dt.year
df['month'] = df['date_received'].dt.month
df['day'] = df['date_received'].dt.day
df['weekday'] = df['date_received'].dt.dayofweek

features = ['panels', 'weight', 'miles', 'weight_per_truck', 'trucks', 'fuel_cost',
            'long_miles', 'miles_x_fuel', 'trucks_x_miles', 'year', 'month', 'day', 'weekday']
X = df[features].replace([np.inf, -np.inf], np.nan).fillna(0)
y = df['cost']

# Preprocessor and model
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['panels', 'weight', 'miles', 'weight_per_truck', 'trucks',
                               'fuel_cost', 'long_miles', 'miles_x_fuel', 'trucks_x_miles',
                               'year', 'month', 'day']),
    ('cat', OneHotEncoder(), ['weekday'])
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

pipeline.fit(X, y)
joblib.dump(pipeline, "model_pipeline.pkl")
print("✅ Model retrained and saved.")

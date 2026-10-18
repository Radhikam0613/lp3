import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

df = pd.read_csv("uber.csv").drop(columns=['Unnamed: 0', 'key'], errors='ignore')

df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce', utc=True)
cols = ['fare_amount', 'pickup_longitude', 'pickup_latitude','dropoff_longitude', 'dropoff_latitude', 'passenger_count', 'pickup_datetime']
df = df.dropna(subset=cols)
df = df[(df.fare_amount > 0) & df.passenger_count.between(1, 6) &
        df.pickup_longitude.between(-180, 180) & df.dropoff_longitude.between(-180, 180) &
        df.pickup_latitude.between(-90, 90) & df.dropoff_latitude.between(-90, 90)].copy()

for col, value in {
    'hour': df.pickup_datetime.dt.hour,
    'day': df.pickup_datetime.dt.day,
    'day_of_week': df.pickup_datetime.dt.dayofweek,
    'month': df.pickup_datetime.dt.month,
    'year': df.pickup_datetime.dt.year
}.items():
    df[col] = value

def haversine(pickuplat, pickuplon, dropofflat, dropofflon):
    pickuplat, pickuplon, dropofflat, dropofflon = map(np.radians, [pickuplat, pickuplon, dropofflat, dropofflon])
    a = np.sin((dropofflat-pickuplat)/2)**2 + np.cos(pickuplat)*np.cos(dropofflat)*np.sin((dropofflon-pickuplon)/2)**2
    return 6371 * 2 * np.arcsin(np.sqrt(np.clip(a, 0, 1)))

df['distance_km'] = haversine(df.pickup_latitude, df.pickup_longitude,df.dropoff_latitude, df.dropoff_longitude)
df = df[df.distance_km.between(0.1, 100)].copy()

sns.boxplot(x=df.fare_amount)
plt.title("Fare Amount Outliers")
plt.show()

Q1, Q3 = df.fare_amount.quantile([0.25, 0.75])
IQR = Q3 - Q1
lower, upper = max(0, Q1 - 1.5*IQR), Q3 + 1.5*IQR
print("Number of outliers:", ((df.fare_amount < lower) | (df.fare_amount > upper)).sum())
df = df[df.fare_amount.between(lower, upper)].copy()

features = ['fare_amount', 'pickup_longitude', 'pickup_latitude','dropoff_longitude', 'dropoff_latitude', 'passenger_count','distance_km', 'hour', 'day', 'month', 'year', 'day_of_week']
corr = df[features].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

X = df[features[1:]]
y = df['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {'Linear Regression': LinearRegression(), 
        'Random Forest': RandomForestRegressor(n_estimators=100,random_state=42,n_jobs=-1)}

results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    results.append({
        'Model': name,
        'R2': r2_score(y_test, pred),
        'MAE': mean_absolute_error(y_test, pred),
        'RMSE': np.sqrt(mean_squared_error(y_test, pred))
    })
print(pd.DataFrame(results).round(3).to_string(index=False))
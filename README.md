# Demand-Forecasting-with-XGBoost-Streamlit
## 🧩 Background
### A retail business manages hundreds of products, each with fluctuating demand patterns across the year. They needed a system to:

#### Understand sales trends and volatility

#### Predict future demand across products

#### Visualize forecasts in an interactive dashboard

#### Improve stock planning and reduce inventory waste

## 🎯 Objective
### Design and implement a lightweight, scalable forecasting solution using machine learning that:

#### Segments products by volatility

#### Trains individualized models per product

#### Forecasts sales for the next 5 weeks

#### Presents results in a user-friendly dashboard

## 📦 Dataset
#### Weekly sales data for 800+ products

#### 52 weeks of historical transactions (W0 to W51)

#### Each row = one product's weekly sales timeline

## 🧠 Methodology
### 1. Volatility Segmentation
#### Calculated standard deviation of weekly sales per product

#### Used pd.qcut() to segment into:

#### Low volatility (predictable)

#### Medium volatility

#### High volatility (spiky, irregular)

### 2. Feature Engineering
### For each product:

#### lag_1, lag_2: Past sales

#### roll_mean_3: 3-week rolling average

#### roll_std_3: 3-week volatility

#### week_of_year: Seasonality cue

### 3. Modeling
#### Trained an XGBRegressor model per product

#### Forecasted last 5 known weeks for testing

#### Then predicted the next 5 weeks (future)

### 4. Evaluation
### Measured:

#### MAE (Mean Absolute Error)

#### RMSE (Root Mean Squared Error)

#### MAPE (Mean Absolute % Error)

#### Grouped errors by volatility segment for insight

## 📈 Results
#### Low volatility products had RMSE < 3.2 on average

#### High volatility products showed wider spread (MAPE > 25%)

#### Forecasts exported to xgboost_forecast_results.csv

#### Visualized via Streamlit dashboard for exploration by:

#### Volatility segment

#### Product code

## 💻 Deliverables
#### ✔️ Python forecasting engine (modular, reusable)

#### ✔️ Streamlit dashboard for business use

#### ✔️ Exported forecast CSV for reporting

#### ✔️ Visualizations by segment

## 🧩 Lessons Learned
#### Segmenting by volatility is crucial for forecast strategy

#### XGBoost handles limited historical data well

#### Visual tools (Streamlit) make results more accessible

#### Lightweight models can drive real business value when combined with smart features

## 🚀 Next Steps
#### Add recursive forecasting to predict further ahead

#### Train ensemble models for high-volatility segments

#### Incorporate external features (promotions, seasonality)

Deploy the dashboard online via Streamlit Cloud or Docker

🏁 Conclusion
This case study proves that with smart segmentation, engineered features, and accessible tools like XGBoost and Streamlit, you can build a powerful, modular demand forecasting solution that’s ready for real-world deployment.

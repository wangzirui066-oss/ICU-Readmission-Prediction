import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
from xgboost import XGBClassifier

# 加载模型（等会儿你会上传这个文件）
model = joblib.load('icu_model.pkl')

st.title("🏥 ICU 30天再入院风险预测")
st.write("20岁医学生独立开发 · AUC 0.813 · 基于MIMIC-III真实数据")

age = st.slider("年龄 Age", 18, 100, 65)
los = st.slider("ICU停留天数 LOS (天)", 0.1, 30.0, 3.0, 0.1)
unit = st.selectbox("首次入住科室 First Care Unit", 
                    ["MICU", "SICU", "TSICU", "CCU", "CSRU"])

# 构造输入
input_df = pd.DataFrame([[los, age]], columns=['los', 'age'])
unit_cols = [col for col in model.feature_names_in_ if col.startswith('first_careunit_')]
for col in unit_cols:
    input_df[col] = 1 if col == f'first_careunit_{unit}' else 0

prob = model.predict_proba(input_df)[0][1]

st.metric("30天再入院概率", f"{prob:.1%}", delta=None)

# SHAP 个人解释
explainer = shap.Explainer(model)
shap_values = explainer(input_df)
fig, ax = plt.subplots()
shap.plots.waterfall(shap_values[0], show=False)
st.pyplot(fig)

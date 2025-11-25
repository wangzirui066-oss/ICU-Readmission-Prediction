# ICU 30-day Unplanned Readmission Risk Prediction  
**XGBoost + SHAP Interpretable Model | MIMIC-III Demo | AUC = 0.813**

**20-year-old 4th-year Clinical Medicine Student**  
China University · Nov 2025  

**简体中文版见下方 ↓**

## Key Findings (SHAP)
- **ICU length of stay (LOS)** is the strongest predictor  
- **Age** ranks second  
- Patients first admitted to **MICU** have significantly higher risk

## Model Performance
- Dataset: MIMIC-III Demo (100 real ICU patients)  
- Model: XGBoost  
- AUC = **0.813**  
- Features: LOS, Age, First Care Unit (one-hot)

## Results
![AUC](auc.png)  
![SHAP Global Explanation](shap.png)

## Code
- Full notebook: `ICU_Readmission_AUC0.813.ipynb`

## Future Work
- Full MIMIC-III (50,000+ patients)  
- Deploy as web app (Streamlit)  
- Upgrade to LSTM/Transformer  
- Applying to Health Informatics / Public Health Master's programs in Canada

---

## ICU 30天非计划再入院风险预测（中文版）
**XGBoost + SHAP 可解释模型 | MIMIC-III Demo | AUC = 0.813**

20岁 临床医学大四在读 | 2025年11月独立完成

### 核心发现
- ICU停留时间（LOS）是对再入院风险影响最大的因素
- 年龄第二重要
- 首次入住MICU的患者风险显著高于其他科室

### 模型表现
- 数据集：MIMIC-III Demo（真实ICU患者）
- AUC = **0.813**
- 已包含完整特征工程与SHAP全局解释

### 下一步计划
- 接入完整版MIMIC-III
- 部署为在线预测网页
- 申请加拿大健康信息学/公共卫生硕士

**仓库作者：@wangzirui066-oss**  
**目标：23岁飞加拿大，25岁前拿PR**

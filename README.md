# Early Identification of At-Risk Students - Predicting Student Dropout and Academic Success  

Impact Certificate: Applied Machine Learning  
Challenge: Classification  
Tomorrow University - Calibration Phase (Sep 2025)  
Industry Focus: Social / Education  
Student: Enrico Vaccari  

---

## 1. Introduction
How can universities identify students at risk of dropping out before it is too late?  
In this project I apply **multi-class classification** to predict whether a student will **drop out, remain enrolled, or graduate**. The dataset includes demographic, socio-economic, and academic features collected from Portuguese higher education institutions. By modeling these outcomes, I aim to support universities in providing **timely, targeted interventions**, aligning with **SDG 4 (Quality Education)** and **SDG 10 (Reduced Inequalities)**.  

---

## 2. Problem Statement & Hypotheses
- **What to predict**: Student outcomes at the end of the program (*Dropout*, *Still Enrolled*, *Graduate*).  
- **Why it matters**: Dropouts represent lost opportunities for students and inefficiencies for institutions. Early prediction allows universities to intervene before it is too late.  
- **How it supports positive change**: Better retention improves equity, reduces financial strain for families, and strengthens communities by increasing educational attainment.  

**Hypotheses**  
- Students with **low first-semester performance** are more likely to drop out.  
- **Socio-economic background** (e.g., parental education, financial status) has a measurable impact on outcomes.  
- Early **academic engagement** (credits earned, evaluations completed) is the strongest predictor of graduation.  

---

## 3. Target Variable
- **Target**: `Target` column with three classes:  
  - `Dropout` → student left the program before completion.  
  - `Enrolled` → student still active at dataset snapshot.  
  - `Graduate` → student completed the degree.  
- **Classification suitability**: Categorical, mutually exclusive, and collectively exhaustive.  

---

## 4. Features
The dataset includes demographic, socio-economic, and academic features.  

- **Key categories**:  
  - Demographics: gender, age, marital status, nationality  
  - Family background: parents’ education and occupation  
  - Administrative: admission mode, tuition status, scholarship, displaced student flag  
  - Academic performance: admission grade, first-semester grades, units credited/enrolled/approved  
  - Macroeconomic context: unemployment, inflation, GDP  

- **Likely strong predictors**: admission grade, first-semester performance, number of approved units.  
- **Sensitive attributes**: gender, nationality, socio-economic proxies (require fairness monitoring).  

---

## 5. Dataset Info
- **Dataset name**: *Predict Students’ Dropout and Academic Success* (UCI Machine Learning Repository)  
- **Why chosen**: Directly aligned with the project goal of modeling educational outcomes; widely cited and reliable.  
- **Format**: CSV, tabular structure with ~37 features + target.  
- **Size**: ~4,000 student records.  
- **License**: Creative Commons (research use).  
- **Geographic coverage**: Portuguese higher education students.  
- **Temporal coverage**: Early 2000s data snapshot (semester-level).  
- **Source**: [UCI Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)  

---

## 6. Data Quality Assessment

| Dimension             | Assessment  | Notes |
|-----------------------|-------------|-------|
| **Accuracy**          | Good        | Data from official academic records |
| **Completeness**      | Moderate    | No health or behavioral data included |
| **Consistency**       | High        | Encoded categorical variables with codebook |
| **Timeliness**        | Moderate    | Data snapshot, not updated in real time |
| **Relevance**         | Strong      | Directly tied to dropout prediction problem |
| **Representativeness**| Limited     | Single-country dataset, may not generalize globally |

---

## 7. Limitations
- **Regional scope**: Data limited to Portuguese institutions.  
- **Missing dimensions**: No mental health, motivation, or social integration features.  
- **Temporal relevance**: Dataset reflects past cohorts; patterns may shift in current contexts.  
- **Class imbalance**: Dropout vs Graduate vs Enrolled distribution requires resampling or weighting.  

---

## 8. Stakeholders, Beneficiaries, and Impact
**Stakeholders (act on model outputs):**  
- Educators and advisors → target support to at-risk students.  
- University administrators → allocate resources effectively.  
- Policymakers and ministries → design dropout-prevention strategies.  

**Beneficiaries (impacted by outcomes):**  
- Students → receive timely support, higher graduation chances.  
- Families → reduced financial and emotional burden.  
- Communities & labor market → stronger educational attainment, better employment prospects.  

**Impact**:  
- **Reduced dropout rates** → improved equity and institutional performance.  
- **Resource optimization** → better use of scholarships, tutoring, and counseling.  
- **Sustainable outcomes** → contributes to SDGs 4, 8, and 10.  

---

## 9. Methodology Overview
The project will follow a full classification pipeline:  
1. **EDA**: Explore distributions, outliers, and correlations.  
2. **Data Cleaning & Preprocessing**: Handle missing values, encode categorical variables, scale numerics.  
3. **Feature Selection**: Remove leakage-prone features (Semester 2), monitor sensitive attributes.  
4. **Modeling**: Baseline Logistic Regression, Stretch Random Forest; consider Gradient Boosting later.  
5. **Evaluation**: Metrics include Accuracy, F1-score, Precision, Recall (with focus on *Dropout*).  
6. **Fairness & Ethics**: Sensitive attribute scanner, subgroup audits, human oversight.  
7. **Communication**: Visualizations, error-cost matrix, stakeholder-ready insights.  

---

## 10. Next Steps
- Perform class distribution analysis and address imbalance.  
- Implement baseline Logistic Regression model.  
- Compare with Random Forest as stretch model.  
- Evaluate subgroup fairness and ethical safeguards.  
- Document compliance (EU AI Act, GDPR) in `/docs/compliance.md`.  

---

## 11. References
- UCI dataset: [Predict Students’ Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)  
- OECD (2023). *Education at a Glance.*  
- UNESCO (2024). *Global Education Monitoring Report.*  

---

## 12. Acknowledgements
Dataset provided by UCI Machine Learning Repository.  
Prepared as part of an academic project on data-driven education and sustainability.  

---

## 13. Data Access & Project Structure

### Download Command
*(Placeholder – update once finalized)*  
```bash
# Example (replace with your actual link or script)
wget <dataset_download_link> -P data/raw/
```

### If Manaully Placing Files
# Place your dataset here
```bash
/data/raw/student_dropout_success.csv
```

### Install the ucimlrepo package
```bash
pip install ucimlrepo
```

```Python
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
predict_students_dropout_and_academic_success = fetch_ucirepo(id=697) 
  
# data (as pandas dataframes) 
X = predict_students_dropout_and_academic_success.data.features 
y = predict_students_dropout_and_academic_success.data.targets 
  
# metadata 
print(predict_students_dropout_and_academic_success.metadata) 
  
# variable information 
print(predict_students_dropout_and_academic_success.variables) 
```

Early_Identification_Of_At-Risk_Students/
│
├── data/
│   ├── raw/                <- Original immutable datasets (CSV, XLSX)
│   ├── interim/            <- Intermediate data (cleaned, preprocessed)
│   ├── processed/          <- Final feature sets ready for modeling
│   └── checksums.txt       <- SHA-256 integrity checks
│
├── notebooks/              <- Jupyter notebooks (EDA, modeling, reports)
├── src/                    <- Source scripts for data cleaning, preprocessing, modeling
├── docs/                   <- Documentation (PRD, compliance.md, etc.)
├── visuals/                <- Plots, diagrams, and figures
├── requirements.txt        <- Python dependencies
└── README.md


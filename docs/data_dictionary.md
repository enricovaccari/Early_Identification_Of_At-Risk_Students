---
title: "Predicting Student Dropout and Academic Success"
author: "Enrico Vaccari"
date: 2025-09-08
stage: "Idea Only – PRD Draft"
---

# Problem Requirement Document (PRD)

## Problem Statement

“Predict whether a student will drop out, remain enrolled, or graduate within the normal program duration, using data recorded up to the end of the first semester, so that universities can trigger timely support interventions and improve retention.”

This project aims to automate the early identification of students at risk of dropping out of higher education programs.  
The **unit of prediction** is an individual student.  
The **outcome event** is the final academic status: *Dropout*, *Still Enrolled*, or *Graduate*.  
The **prediction horizon** is set at the end of the first semester, using only demographic, socio-economic, and first-semester academic features.  
The decision supported by the model is whether to trigger early interventions (tutoring, financial aid, counseling).

---
## Breakdown

Unit = student  
Event = drop out / remain enrolled / graduate  
Horizon = end of the program (normal duration of studies)  
Prediction time = end of Semester 1  
Impact = enable proactive support (tutoring, financial aid, counseling) to improve outcomes

features_to_keep = [
    "Marital status",
    "Application mode",
    "Application order",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Previous qualification (grade)",
    "Nationality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
    "Admission grade",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "International",
    # Semester 1
    "Curricular units 1st sem (credited)",
    "Curricular units 1st sem (enrolled)",
    "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 1st sem (without evaluations)",
    # Macroeconomic
    "Unemployment rate",
    "Inflation rate",
    "GDP"
]

---

## Success Metrics
The model’s success will be measured in terms of classification accuracy and fairness across subgroups.  
Baseline values will be set using simple heuristics (e.g., majority class) and improved in later milestones.  
Aspirational goals are aligned with practical utility for universities.

| Metric              | Baseline (placeholder) | Target |
|---------------------|-------------------------|--------|
| Accuracy            | 0.50                    | 0.75   |
| F1-score (Dropout)  | 0.40                    | 0.70   |
| Recall (Dropout)    | 0.50                    | 0.80   |
| Precision (Dropout) | 0.40                    | 0.70   |

**Primary metric:** *F1-score (Dropout)*.  
This balances **precision** (avoiding false alarms that could waste resources) and **recall** (avoiding missed at-risk students). Accuracy alone could be misleading due to class imbalance. The trade-off is that maximizing recall may increase false positives, requiring careful threshold setting to avoid alert fatigue.

## Error-Cost Matrix

In this project, not all errors are equal. The cost of a **false negative** (failing to identify a student at risk of dropping out) is much higher than the cost of a **false positive** (flagging a student who would have succeeded without intervention).

| Prediction ↓ / Reality → | Dropout (Positive)                | Graduate / Enrolled (Negative)         |
|--------------------------|-----------------------------------|----------------------------------------|
| **Predicted Dropout**    | True Positive (✅ correctly flagged) | False Positive (⚠️ unnecessary support) |
| **Predicted Not Dropout**| False Negative (❌ missed student, no support) | True Negative (✅ no intervention)     |

**Interpretation:**  
- *False Negative (high cost)* → A student who needed help does not receive it. Consequences: increased dropout, wasted potential, reputational loss for the university.  
- *False Positive (moderate cost)* → A student receives support unnecessarily. Consequences: some wasted resources, but generally beneficial for the student.  

➡️ **Priority:** Optimize recall for the Dropout class, even if it means tolerating more false positives.  

---

## Stakeholders & Impact
**Direct beneficiaries (benefits):**  
- *Students* → timely interventions increase graduation odds.  
- *Universities* → improved retention rates and optimized resource allocation.  

**Indirect beneficiaries (benefits):**  
- *Families* → reduced stress and financial burden.  
- *Labor market & society* → more skilled graduates, stronger social mobility.  

**Stakeholders (actors using the model):**  
- *Educators and academic advisors* → target at-risk students with tailored support.  
- *University administrators and policy-makers* → optimize allocation of financial and human resources.  
- *Government and education ministries* → design national or regional dropout-prevention strategies.  

**Potential harms / risks:**  
- *Alert fatigue* among educators if models flag too many students without prioritization.  
- *Policy misuse* if predictions are used punitively for funding or admission instead of supportive measures.  

Quadrant visual (conceptual):  
- Direct/Benefit → Students, Universities  
- Indirect/Benefit → Families, Labor Market  
- Direct/Harm → Alert fatigue (risk item)  
- Indirect/Harm → Policy misuse (risk item)

---

## Prediction Horizon & Feature Timing
The chosen prediction horizon is the **end of the first semester**.  

- **Features available at prediction time:** demographics, socio-economic background, entry grades, and Semester 1 performance.  
- **Features excluded:** all Semester 2 or later data (to avoid leakage).  
- **Target labels:** *Dropout*, *Still Enrolled*, or *Graduate* observed at the end of program duration.  

**Why this matters:**  
- An enrollment-only horizon would be too early and inaccurate.  
- A Semester 2 horizon would be more predictive but too late for early interventions.  
- Semester 1 is the compromise: enough evidence to predict risk, with enough time for universities to act.

---

## Data Overview
Anticipated data will come from **UCI’s “Predict Students’ Dropout and Academic Success” dataset**, containing records of Portuguese higher education students.  
Expected **5 V’s**:  
- **Volume:** ~4,000 student records (manageable for ML pipelines).  
- **Variety:** Demographic, socio-economic, academic, and macroeconomic indicators.  
- **Velocity:** Static, semester-level updates (no streaming).  
- **Veracity:** Reasonably reliable (institutional records), but cultural/context bias is possible.  
- **Value:** High — predictive insights can reduce dropouts and improve resource allocation.  
Uncertainties include dataset representativeness across countries and handling missing values.

The class distribution analysis shows that the dataset is moderately imbalanced: Graduate is the majority class (49.9%), followed by Dropout (32.1%) and Enrolled (17.9%). All classes are well above the 5% threshold, so there are no extreme minority categories. However, the imbalance still matters: a model trained without adjustments could be biased toward predicting the majority outcome (Graduate). To mitigate this, I will monitor performance using class-sensitive metrics such as F1-score and recall for the Dropout and Enrolled classes, and consider class weighting or resampling strategies if needed.

---

## Model Scope
- **Baseline model:** Logistic Regression (fast, interpretable, well-suited to numeric + encoded categorical data, to provide a transparent performance floor and highlight issues like class imbalance or leakage).  
- **Stretch model:** Random Forest Classifier (captures non-linearities and interactions, robust to outliers, handles mixed feature types, to raise predictive performance while still keeping interpretability via feature importance).  
- Later, I could explore Gradient Boosting (XGBoost/LightGBM), but Logistic Regression + Random Forest is already a strong and professional choice.  

Model interpretability will be prioritized to ensure trust by educators.

---

## Ethics & Compliance

### Regulatory & Privacy Constraints

**AI Risk Tier (EU AI Act 2024 Draft)**  
The domain of this project is **education & student success monitoring**.  
This does **not fall into the EU AI Act’s “high-risk” categories** (such as biometric identification, medical diagnosis, or employment decisions).  
Therefore, the project is likely classified as **Limited Risk**.  

**Privacy Considerations**  
- Dataset includes demographic and socio-economic variables (e.g., gender, nationality, parental education).  
- These attributes are sensitive under GDPR if misused.  
- No directly “special category” data (health, religion, biometrics) is included.  

**Planned Compliance Steps**  
- Treat all personal data as pseudonymized research data.  
- Run a **Sensitive Attribute Scanner** (documented in notebook).  
- Ensure **human oversight**: predictions are decision-support only, not automated exclusion.  
- Maintain **transparent documentation** (problem spec, leakage guard, fairness audits).  
- Align with **GDPR principles**: purpose limitation, minimization, and fairness.  

**Personal ethical risk**  
The main ethical concern I anticipate is that the model could unintentionally stigmatize or disadvantage certain student groups (e.g., by over-predicting dropout for international or low-income students). This risk highlights the need for fairness checks, subgroup analysis, and ensuring outputs are used only for *supportive interventions*, not punitive actions.

*Conclusion:* While this is not a legally high-risk system, fairness and transparency are critical to avoid reinforcing inequalities in education.  
For detailed governance, see [/docs/compliance.md](./docs/compliance.md).

---

## Deployment Context
Predictions will be made in **batch mode** at the end of each semester.  
Latency is not critical (hours are acceptable), but outputs will be human-reviewed before action.  
The model will support educators, not replace them, ensuring human oversight for every flagged student.

---

## Capstone Hook
This PRD is a **living document**. In Milestone 3:  
- Replace placeholder metrics with dataset-based baselines.  
- Update 5 V’s with actual statistics.  
- Refine model scope after exploratory data analysis.  
- Reassess ethical implications with real distribution insights.

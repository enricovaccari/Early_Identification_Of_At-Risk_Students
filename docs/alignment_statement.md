# Alignment Statement

For this classification project, I selected the **“Predict Students’ Dropout and Academic Success” dataset** from the **UCI Machine Learning Repository**. It contains approximately 4,000 anonymized student records from Portuguese higher education, with demographic, socio-economic, academic, and macroeconomic features. This dataset directly aligns with the project’s aim: predicting educational outcomes to enable timely institutional support.  

The dataset defines three mutually exclusive classes: **Dropout**, **Enrolled**, and **Graduate**. These categories match my prediction task without modification. Each student is labeled with one outcome, making it a well-structured multi-class classification problem.  

Ethically and technically, the dataset is a strong fit. It is publicly available for research use, anonymized, and well-documented. No personally identifiable information (PII) is included. Sensitive attributes such as gender, nationality, and parental background are present, but these can be mitigated through fairness audits, subgroup analysis, and optional feature removal. Technically, the dataset includes features observable before the prediction horizon (end of Semester 1), reducing the risk of label leakage.  

Remaining gaps include **moderate class imbalance** (Graduate ≈ 50%, Dropout ≈ 32%, Enrolled ≈ 18%) and limited geographic scope (Portugal only). I plan to address imbalance with class weighting or resampling and highlight representativeness limitations in my reporting.  

**Why this dataset is fit:**  
- **Classes covered:** It directly provides the three classes needed (*Dropout, Enrolled, Graduate*), fully aligned with the prediction task.  
- **Gaps/risks:** The main risks are class imbalance, socio-economic bia and geographic limitation; mitigation includes resampling, fairness monitoring, and careful contextualization of findings.  
- **Social impact alignment:** The dataset supports **SDG 4 (Quality Education)** by improving graduation rates, **SDG 10 (Reduced Inequalities)** by identifying disadvantaged groups, and indirectly contributes to **SDG 8 (Decent Work & Economic Growth)** by strengthening workforce readiness.  

This makes it both a technically sound and socially impactful choice for the project.

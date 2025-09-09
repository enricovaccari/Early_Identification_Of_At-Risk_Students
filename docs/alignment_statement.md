# Alignment Statement

For this classification project, I selected the **“Predict Students’ Dropout and Academic Success” dataset** from the **UCI Machine Learning Repository**. It contains approximately 4,000 anonymized student records from Portuguese higher education, with demographic, socio-economic, academic, and macroeconomic features. This dataset directly aligns with the project’s aim: predicting educational outcomes to enable timely institutional support.  

The dataset defines three mutually exclusive classes: **Dropout**, **Enrolled**, and **Graduate**. These categories match my prediction task without modification. Each student is labeled with one outcome, making it a well-structured multi-class classification problem.  

Ethically and technically, the dataset is a strong fit. It is publicly available for research use, anonymized, and well-documented. No personally identifiable information (PII) is included. Sensitive attributes such as gender, nationality, and parental background are present, but these can be mitigated through fairness audits, subgroup analysis, and optional feature removal. Technically, the dataset includes features observable before the prediction horizon (end of Semester 1), reducing the risk of label leakage.  

Remaining gaps include **moderate class imbalance** (Graduate ≈ 50%, Dropout ≈ 32%, Enrolled ≈ 18%) and limited geographic scope (Portugal only). I plan to address imbalance with class weighting or resampling and highlight representativeness limitations in my reporting.

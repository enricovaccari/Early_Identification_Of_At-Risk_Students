---
title: "Predicting Student Dropout and Academic Success"
author: "Enrico Vaccari"
date: 2025-09-08
stage: "Idea Only – PRD Draft"
---

# Metadata Summary – Student Dropout and Academic Success Dataset

This dataset contains anonymized records of approximately 4,000 higher education students from a Portuguese institution. Each record corresponds to an individual student and includes demographic, socio-economic, and academic information, along with macroeconomic indicators at the time of enrollment. The **target variable** is the student’s final academic outcome: *Dropout*, *Still Enrolled*, or *Graduate*. These labels are mutually exclusive and collectively exhaustive, and they reflect the student’s official status at the end of the standard program duration. Features include marital status, admission mode, parental qualifications, admission grades, first-semester course performance, and financial/administrative status.

The dataset is structured in tabular CSV format, with each row representing a student and each column representing a feature. All categorical attributes are encoded as integers with specific codebooks provided (e.g., *Marital Status: 1 = Single, 2 = Married*). Continuous features include grades (0–200 for admission, 0–20 for semester averages) and macroeconomic values (unemployment, inflation, GDP). Data are **single-label classification** (each student has exactly one target outcome). Importantly, **temporal context matters**: features from Semester 2 should not be used when modeling predictions at the Semester 1 horizon, as they would introduce leakage. The dataset includes a detailed data dictionary and license on the UCI repository, which must be referenced to interpret each code correctly. Misinterpreting coded values (e.g., confusing “application order” with admission priority) or mixing post-horizon features would result in invalid models.

---

## Dataset Source
- **Repository:** UCI Machine Learning Repository  
- **Dataset name:** *Predict Students’ Dropout and Academic Success*  
- **Link:** [UCI Repository – Dataset 697](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)  
- **Original context:** Data from Portuguese higher education students (2009–2019).  

---

## Features (High-Level Groups)
- **Demographics:** gender, age at enrollment, marital status, nationality.  
- **Family background:** parental education, parental occupation.  
- **Administrative:** application mode, application order, tuition status, scholarship holder, displaced student flag, special needs.  
- **Academic performance:** admission grade, first-semester grades, credits enrolled, approved, and evaluations.  
- **Macroeconomic context:** unemployment rate, inflation rate, GDP.  

---

## Target Variable
- **Column:** `Target`  
- **Classes:**  
  - `Dropout` → student left the program before completion.  
  - `Enrolled` → student remained in the program at dataset snapshot.  
  - `Graduate` → student completed the degree successfully.  

---

## License
- Distributed through the **UCI Machine Learning Repository**.  
- Available for **public research use**.  
- Attribution required; commercial use restrictions may apply depending on institutional policies.  

---

## Known Limitations & Caveats
- **Temporal leakage risk:** Semester 2 features must be excluded if predicting after Semester 1.  
- **Geographic scope:** Limited to Portuguese institutions; results may not generalize globally.  
- **Socio-economic bias:** Features like nationality and parental occupation may introduce fairness risks.  
- **Class imbalance:** Classes are uneven (Graduate ≈ 50%, Dropout ≈ 32%, Enrolled ≈ 18%); needs handling in modeling.  
- **Metadata reliance:** Codebooks must be referenced carefully; some encoded values are non-intuitive.  

---

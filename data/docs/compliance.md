# Compliance & Risk Tier (Student Dropout Prediction)

## AI Risk Tier (EU AI Act, 2024 Draft)
- **Domain:** Higher education, dropout prediction  
- **Expected Tier:** Limited Risk  
- **Rationale:**  
  - Not medical, biometric, or law enforcement  
  - Supports but does not replace human decision-making  
  - Used for resource allocation & student support

## Privacy Considerations
- Dataset includes demographic and socio-economic variables
- GDPR relevance:  
  - *Direct identifiers*: none  
  - *Sensitive attributes*: Gender, Nationality (potential bias)  
  - *Proxies*: Parental education/occupation  
- Mitigation: sensitive attribute scanning, fairness checks, and optional feature removal

## Compliance Plan
- **Data Protection Principles:** pseudonymize student IDs, minimize unnecessary features
- **Oversight:** human-in-the-loop for all interventions
- **Logging:** keep experiment runs reproducible (git + metadata)
- **Stress Testing:** robustness checks for class imbalance and missing data
- **Fairness Monitoring:** subgroup precision/recall checks in Milestone 6

## References
- EU AI Act (Draft 2024): [Summary](https://artificialintelligenceact.eu/)  
- GDPR Article 9: Special Category Data  
- Course Visual Aid: `/visuals/ai_risk_flow.png`

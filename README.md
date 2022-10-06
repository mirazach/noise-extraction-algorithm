
# Noise Extraction Algorithm
Inspired by Kahneman, Sunstein and Sibony's book *Noise: A Flaw in Human Judgement*, 
this algorithm extracts the amount of noise within a given set of decisions. 

This set of decisions should be the result of a **Noise Audit**:  a process that helps organisations measure their level of noise. 
To perform a noise audit, little experiments are designed to give the same judgement decision to different decision makers. 
The results are the input of this algorithm which is provided in both R and Python. 


**Input** 

A *n x m* matrix with n decision makers who have recorded their decisions for m separate cases 


**Output** 

**System Noise:** Overall variability within system of judgments. This is then decomposed into:

    - **Level Noise:** The variability of an individual’s average judgement ie. is a person harsher or more lenient on average?
    - **Pattern Noise:** Variations due to individuals’ specific responses to cases/people ie.a generally harsh judge being unusually lenient with older defendants who shoplift. 


***
You can find out more about the mathematical theory behind this algorithm in this article:  
https://newnowgroup.medium.com/the-mathematics-of-noise-f74d0dcbe2b4


### ch18-19 Comparing two samples: pooled standard error
雙樣本比例檢定 

Sample1:Xcont, Ncount
Sample2:Xexp, Nexp 

Ppool=(Xcount+Xexp)/(Ncout+Nexp)

### ch29

*NOTE
- what change matter to us? substantive = practically significance
- In medical or tranditional science, need 5-15% change to really be substantive. 
- In online biz like google, ***1-2%*** is quite large
- You want repeatability. It's statistical significant
- Sizing statistical significant bar is actually lower than practical significance bar

### ch21-23 statistic power, power tradeoff size
- to measure smaller change or higher result cofidence  > more sclae of experienment

- alpha = p(reject null |null true)
- beta = p(fail to reject|null false)
- power=sensibility = 1-beta (often 80%)
- confidence level = 1-alpha
- practical significance = minimum detectable effect = dmin (detect 最小改變量)

Example: how many page views affect sensibility

1. less sample size
    - alpha low, beta high
    - easy to fail to reject null
    - sensibility is low

2. more sample size
    - beta low
    - power increase
    - easy to reject null > sensitive

### ch24 Calculating Number of Pages Views Needed

H0:Pcont=Pexp
H1:Pcont=\=Pcont

Updated:
H0: Pexp-Pcont > dmin
H1: Pexp-Pcont =< dmin

d-hat= Pexp-Pcont
dmin=minimum detectable effect, use 2% here.

confidential level = often use 95% 

SE=sqrt(p*(1-p)*((1/n1)+(1/n2)))
m=z-score*SE

CI=[d-m,d+m]

Decision: If dmin not in CI, then reject null. Otherwise, accept null.

---
### Reference

https://www.dataquest.io/blog/a-b-testing-the-definitive-guide-to-improving-your-product/

https://www.evanmiller.org/ab-testing/sample-size.html
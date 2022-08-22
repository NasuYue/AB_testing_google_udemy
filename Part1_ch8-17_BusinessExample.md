

### Binomial Distribution
- Pros: use formula to know how variable of overall CTP
- Assumption
    - Two types of outcomees
    - independant event : tricky part
    - identical distribution: p same for all


### ch14 Caculating confidentail interval
單樣本比例檢定

- p=p-hat=x/N
- SE=sqrt(p*(1-p)/total trail)
- Margin of error=z-score*SE
- CI=[p-SE,p+SE]
- rule of thumb: if N*p-hat>5 & N*(1-p-hat)>5 then use normnal distribution


### ch15 Example & Quiz

x=400
N=2000

p=300/2000=0.15
SE=sqrt(0.15*0.85/2000)

z-score 99%=2.58

M=2.58*sqrt(0.15*0.85/2000)=0.0205996481

CI=[p-SE,p+SE]=[0.1294,0.17063]

### ch16,17

單尾：是否有變化
雙尾：是否有增加or減少

H0:Pcont=Pexp
H1:Pcont=\=Pcont

Process
1. Mesure Pcont and Pexp
2. Caculate P(Pexp-Pcont|H0)
3. Reject null if alpha<0.05

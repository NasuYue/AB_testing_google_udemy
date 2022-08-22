
## Premise
- Design and analyze experient
- basic statistics
- Process
    1. Choose a metric
    2. Review statistics
    3. Design
    4. Analyze

### What's A/B Testing
- use contronl (existing festure) and experiment (new feature) to find out which is better to user
- Expect robust and repeatable result > make decision of launching feature
- in online, your data with lower resolution, you cannot distinguish each user (vs clinical data)
- help you to climb the perk of current mountain,  not for  "choosing the right mountain" 
- AB testing doesn't apply to new experience
    - what's the baseline
    - how long does it take to accept the new experience
    - cannot tell you what's missing

### Example
- Based on customer funnel model, to increase more student use "Adacity"
- Does new button help user enter the second level of funnel?

hypothesis: change "start" button from orange to pink will increse ***how many students explore audacity courses***

Metrics:
1. Total number of course comleted > bad, too much time to verifiy
2. CTR=(number of click/number of page views) > hard, if a version of page with higher of clicks and the result is not accurate
3. CTP=(uniquue visitor who click/unique visitors ot page)> better, click-through-probability

>> updated hypothesis: Change "start" button from orange to pink will increse ***"click-through-probability"***

Note: rate vs probability 
1. Rate: the usability of a button, how often they find the button
2. Probability: trial clicks / page views, how many user enter 2nd level pages, filter out reload, wrong cliks...etc

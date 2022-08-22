
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
- Expect consistantly response of contronl and experient group
- robust and repeatable result > make decision of launching feature
- help you to climb the perk of current mountain,  not for  "choosing the right mountain" 
- in online, your data with lower resolution, you cannot distinguish each user (<>clinical data)

- AB testing doesn't apply to new experience
    - what's the baseline
    - how long does it take to accept the new experience
    - cannot tell you what's missing


### Example
- Based on customer funnel model, to increase more student use "Adacity"
- More accurate, does user entr the second level of funnel

1. hypothesis: change "start" button from orange to pink will increse ***how many students explore audacity courses***

2. Metric
- total number of course comleted > bad, too much time to verifiy
- (number of click/number of page views) > hard, if a version of page with higher of clicks aand the result is not accurate
- (uniquue visitor who click/unique visitors ot page)> better, click-through-probability

3. updated hypothesis change "start" button from orange to pink will increse ***"click-through-probability"*** of the button

- Pick a metrics: 
1. Rate: the usability of a button, how often they find the button
2. Probability: how many user enter 2nd level pages, filter reload, wrong cliks...etc
- trial clicks / page views

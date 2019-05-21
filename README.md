# Bert-Analysis
Simple CLI for analyzing Google's Bert predicted data
![](https://i.imgur.com/9bEI1KI.png)

## Motivation
bert-text is designed to allow simple statistics measurement's of binary classifier's output preditions. By deafult bert crated the predicted classes colums by their order of apperence in the train.tsv file, bert-text takes care of rememering how the values were presented and uses this information to evaluate the predicted data. 
## Requirements
bert-analysis uses npyscreen to create comand line interface
```
pip install npyscreen
```
## Files input
![](https://i.imgur.com/XtytwZ4.png)

#### Bert takes 3 files as input:
**1.  Traning file(train.tsv)**
This is the file used while traning bert, the file is needed to analyze and remeber the classes order of apperence.

*Example*

| Index | class | a | text|
| -------- | -------- | -------- |---|
|1|0|'a'|'opinion 1'|
|2|0|'a'|'opinion 2'|
|3|1|'a'|'opinion 3'|
|4|0|'a'|'opinion 4'|

**2.  Testing file**
This is the file where you keep the classes for data used for testing bert.This file is needed because bert doesn't take the actual class for it's traning data so the file is there for comparison.

*Example*

| class | text|
| ------|---|
|0|'opinion 1'|
|0|'opinion 2'|
|1|'opinion 3'|
|0|'opinion 4'|

**2.  Predicted file(test_results.tsv)**
This is the file returned by bert after prediction. This file is needed to test the accuracy of bert output.

*Example*

| class 1| class 2|
| ------|---|
|0.00029595374|	0.99970406
|0.9983991|	0.0016009521
|0.00059712224	|0.9994029
|0.00059151126|	0.9994085

## Returned data:

* True Positives
* False Positives
* False Negatives
* False Positives
* Accuracu
* Specificity
* Sensitivity
* Precision
* F-score
* Matthews correlation coefficient
* Youden Index
## Limitations:
bert-analysis is currently limited to analyzing binary classifiers, this might change in future.

## Future of the project
- [ ] Confussion martix as image
- [ ] ROC curve
- [ ] AUC
- [ ] Multinomial classifiers
- [ ] Returning hard sentences 


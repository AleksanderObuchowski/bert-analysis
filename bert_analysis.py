import npyscreen
import csv
import math
import sys
TP = 0
TN = 0
FP = 0
FN = 0

def read_data(filename):
    csv.field_size_limit(sys.maxsize)
    with open(filename) as file:
        reader = csv.reader(file,delimiter='\t')
        labels = []
        for index,label,a,text in reader:
          if label not in labels:
              labels.append(label)
    label_dict= {}
    for i in range(len(labels)):
        label_dict[labels[i]] = i

    return label_dict



def read_test_data(filename):
    csv.field_size_limit(sys.maxsize)
    labels= []
    with open(filename) as file:

        reader = csv.reader(file,delimiter='\t')

        for label,text in reader:
            labels.append(label)



    return labels

class TUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", Select, name="Bert Analysis")
        self.addForm("RESULT", Result, name="Bert Analysis-results")


class Select(npyscreen.ActionForm):
    def activate(self):
        self.edit()
        self.parentApp.setNextForm("RESULT")

    def create(self):

        self.train= self.add(npyscreen.TitleFilenameCombo,
                                name="Select traning file", label=True)
        self.test= self.add(npyscreen.TitleFilenameCombo,
                                name="Select testing file", label=True)
        self.predicted = self.add(npyscreen.TitleFilenameCombo,
                                name="Select predicted file", label=True)

    def on_ok(self):



        dictionary = read_data(self.train.value)
        labels = read_test_data(self.test.value)

        global TP,TN,FP,FN

        with open(self.predicted.value) as file:
            reader = csv.reader(file,delimiter='\t')
            i = 0
            c_t = []
            for line in reader:
                line = [float(l) for l in line]
                maxposition = line.index(max(line))
                c = int(dictionary[str(maxposition)])


                if(int(c)==0):
                    if(int(labels[i])==0):
                        TN+=1
                    elif(int(labels[i])==1):
                        FN+=1

                elif(int(c)==1):
                    if(int(labels[i])==0):
                        FP+=1
                    elif(int(labels[i])==1):
                        TP+=1
                    else:
                        c_t.append(int(labels[i]))
                else:
                    c_t.append(c)

                i+=1

            Accuracy = (TP +TN)/(TP+TN+FP+FN)

            Specificity = TN/(TN+FP)
            Sensitivity = TP /(TP+FN)
            Precision = TP/(TP+FP)

            Fm = 2*(Precision * Sensitivity)/(Precision + Sensitivity)
            Mcc = ((TP *TN) - (FP*FN))/(math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))

            Yi = Sensitivity -(1-Specificity)





            toResult = self.parentApp.getForm("RESULT")

            toResult.TP.value= TP
            toResult.TN.value= TN
            toResult.FP.value= FP
            toResult.FN.value= FN
            toResult.Ac.value= Accuracy
            toResult.Sp.value= Specificity
            toResult.Se.value = Sensitivity
            toResult.Pr.value= Precision
            toResult.Fm.value= Fm

            toResult.Mcc.value= Mcc

            toResult.Yi.value= Yi

            self.parentApp.switchForm("RESULT")


class Result(npyscreen.Form):
    def activate(self):
        self.edit()
        self.parentApp.setNextForm(None)

    def create(self):
        self.TP = self.add(npyscreen.TitleFixedText, name='True Positives:')
        self.TN = self.add(npyscreen.TitleFixedText, name='True Negatives:')
        self.FP = self.add(npyscreen.TitleFixedText, name='False Positives:')
        self.FN = self.add(npyscreen.TitleFixedText, name='False Negatives:')
        self.Ac = self.add(npyscreen.TitleFixedText, name='Accuracy:')
        self.Sp = self.add(npyscreen.TitleFixedText, name='Specificity:')
        self.Se = self.add(npyscreen.TitleFixedText, name='Sensitivity:')
        self.Pr = self.add(npyscreen.TitleFixedText, name='Precision:')
        self.Fm = self.add(npyscreen.TitleFixedText, name='F1-score:')
        self.Mcc = self.add(npyscreen.TitleFixedText,name='Matthews correlation coefficient:')

        self.Yi = self.add(npyscreen.TitleFixedText, name='Youden Index')



if __name__ == "__main__":
    npyscreen.wrapper(TUI().run())

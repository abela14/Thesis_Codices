import weka.core.Instances as Instances
import weka.classifiers.trees.RandomForest as RandomForest
import weka.classifiers.Evaluation as Evaluation
from numpy import genfromtxt, savetxt

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('Data/train.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('Data/test.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForest.setNumTrees(100)
    rf.Evaluation(train, target)

    savetxt('Data/submission2.csv', rf.predict(test), delimiter=',', fmt='%f')

if __name__=="__main__":
    main()
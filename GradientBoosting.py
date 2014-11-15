from sklearn.ensemble import GradientBoostingClassifier
import sys

# input
X = []
y = []
D = 14654

print "Start reading the data."
trainf = open(sys.argv[1], 'r')
for line in trainf:
    line = line.strip("\n")
    ins = line.split(" ")
    label = int(ins[0])
    features = [0] * D
    for j in range(1, len(ins)-1):
        pair = ins[j].split(":")
        index = int(pair[0])
        value = float(pair[1])
        features[index-1] = value
    y.append(label)
    X.append(features)
trainf.close()

X_test = []
y_test = []
testf = open(sys.argv[2], 'r')
for line in testf:
    line = line.strip("\n")
    ins = line.split(" ")
    label = int(ins[0])
    features = [0] * D
    for j in range(1, len(ins)-1):
        pair = ins[j].split(":")
        index = int(pair[0])
        value = float(pair[1])
        features[index-1] = value
    y_test.append(label)
    X_test.append(features)
testf.close()
print "End reading the data."

#------------------------------------------------------
''' Training '''
print "Training..."
g = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
clf = g.fit(X, y)
#------------------------------------------------------
''' Testing '''
accuracy = clf.score(X_test, y_test) 
print "accuracy: ", accuracy
#------------------------------------------------------


from sklearn.ensemble import RandomForestClassifier
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
clf = RandomForestClassifier(n_estimators=50)
clf = clf.fit(X, y)
print "Training.. end.."
y_predict = clf.predict(X_test)
accuracy = clf.score(X_test, y_test) 
print "accuracy: ", accuracy
pred_out = open("rfc_pred", 'w')
for pred in y_predict:
    pred_out.write(str(pred_out) + "\n")
pred_out.close()
#------------------------------------------------------


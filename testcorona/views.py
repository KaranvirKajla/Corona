from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Create your views here.
def testcorona(request):
    return render(request,"testcorona.html")

def report(request):
    if request.method=='POST':
        f = open('model.pkl','rb')
        clf = pickle.load(f)
        f.close()
        fever = request.POST.get("fever")
        backpain = request.POST.get("backpain")
        nose = request.POST.get("nose")
        age = request.POST.get("age")
        breath = request.POST.get("breath")
        
        print(fever,backpain,age,nose,breath)
        # inputFeatures = [100,1,22,1,1]
        inputFeatures = [int(fever),int(backpain),int(age),int(nose),int(breath)]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        print("infprob")
        print(infProb)
        context = {
            "probabilty": int(infProb*100)
        }
        return render(request,"report.html",context)


def training():
    df = pd.read_csv("data.csv")
    train, test = data_split(df, 0.2)
    X_train = train[['fever','bpain','age','runnyNose','diffBreadth']].to_numpy()
    X_test = test[['fever','bpain','age','runnyNose','diffBreadth']].to_numpy()
    Y_train = train[['infProb']].to_numpy().reshape(2012 ,)
    Y_test = test[['infProb']].to_numpy().reshape(503 ,)
    clf = LogisticRegression()
    clf.fit(X_train,Y_train)

    file = open('model.pkl','wb')
    pickle.dump(clf,file)
    file.close()
    inputFeatures = [100,1,22,1,1]
    infProb = clf.predict_proba([inputFeatures])[0][1]
    print("infprob")
    print(infProb)




def data_split(data,ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
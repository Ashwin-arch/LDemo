import random

from django.http import HttpResponse
from django.shortcuts import render

from display01.forms import inputform

# Create your views here.

index=0
len1 = 3
def home(request):
    global index
    global len1
    
    words=getWord(len1)
    random.shuffle(words)
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            len1=data.get("len1")
            words=getWord(len1)
            random.shuffle(words)
            if words==[] and len(words)>=index:
                outText="No text"
            else:
                outText=words[index]
        index+=1
    if words==[] and len(words)>=index:
        outText="No text"
    else:
        outText=words[index]
    return render(request,"html/index.html",{"param1":outText,"form":form1})


def getWord(lenWord):
    with open("../next.txt", "r") as f:
        list1=f.read().split()
        list2=[]
    
        for i in list1:
            if len(i)==lenWord:
                list2.append(i) 
    return list2
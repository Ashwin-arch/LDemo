import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

index=0
def home(request):
    global index
    words=[]
    with open("/home/ashwin/word_display/next.txt", "r") as f:
        words = f.read().split()
        random.shuffle(words)
    if request.method=="POST":
        index+=1
        
    return render(request,"html/index.html",{"param1":words[index]})
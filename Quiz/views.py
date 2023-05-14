from django.shortcuts import redirect,render
from .forms import addQusetionform
from .models import *
from django.http import HttpResponse

# Create your views here.
def Home(request):
    if request.method == 'POST':
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            x = request.POST.get(q.question)
            print(x)
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)

def addQuestion(request):    
        form=addQusetionform()
        if(request.method=='POST'):
            form=addQusetionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Addquestion.html',context)
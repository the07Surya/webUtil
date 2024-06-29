from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  #get the text
 # demo=request.GET.get('text','default')
#  print(demo)
  return render(request,'index.html')
def analyze(request):
  demo=request.GET.get('text','default')
  removePunc=request.GET.get('removePunc','off')
  capitalize=request.GET.get('capitalize','off')
  LineRemover=request.GET.get('LineRemover','off')
  extraSpaceRemover=request.GET.get('extraSpaceRemover','off')
  charcount=request.GET.get('charcount','off')
  ans=""
  punc='''!()-[]{}:;'"\,<>/?@#$%^&*~_'''
  if removePunc=='on':
    for i in demo:
      if i not in punc:
        ans=ans+i
    param={'analyzed_text':ans} 
    demo=ans 
  if capitalize=='on':
    for i in demo:
      ans=ans+i.upper()
    param={'analyzed_text':ans}  
    demo=ans
  if LineRemover=='on':
    for i in demo:
      if i!='\n':
        ans=ans+i  
    param={'analyzed_text':ans}  
    demo=ans
  if extraSpaceRemover=='on':
    for i,j in enumerate(demo):
      if not (demo[i]==" " and demo[i+1]==" "):
        ans=ans+j  
    param={'analyzed_text':ans}  
    demo=ans 
 # if charcount=='on':
   # count=len(demo) 
  #  param={'analyzed_text':count}  
           
  return render(request,'features.html',param)  
#def capitalizeFirst(request):
#  return HttpResponse("capitalize function")
#def newlineRemove(request):
#  return HttpResponse("new line remover")
#def spaceRemover(request):
#  return HttpResponse("space remover")
#def charCount(request):
#  return HttpResponse("count character")  


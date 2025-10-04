from django.shortcuts import render,get_object_or_404,redirect
from .models import DiaryEntry
from .forms import DiaryEntryForm
# Create your views here.

def entry_list(request):
    list=DiaryEntry.objects.all().order_by('-created_at')
    return render(request,'diary/entry_list.html',{'list':list})
def entry_detail(request,pk):
    detail=get_object_or_404(DiaryEntry,pk=pk)
    return render(request,'diary/entry_detail.html',{'detail':detail})
def entry_form(request):
    if request.method=='POST':
        form=DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary:entrylist')
    else:
        form=DiaryEntryForm()
    return render(request,'diary/entry_form.html',{'form':form})
def entry_update(request,pk):
    update=get_object_or_404(DiaryEntry,pk=pk)
    if request.method=='POST':
        form=DiaryEntryForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return redirect('diary:entrylist')
        else:
            form=DiaryEntryForm(instance=update)
    return render(request,'diary/entry_form.html',{'form':form})
def entry_confirm_delete(request,pk):
    delt=get_object_or_404(DiaryEntry,pk=pk)
    if request.method=='POST':
        delt.delete()
        return redirect('diary:entry-list')
    return render(request,'diary/entry_confirm_delete.html',{'delete':delt})
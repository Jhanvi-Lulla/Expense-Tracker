from django.shortcuts import render,redirect
from tracker.models import expense
from .forms import ItemForm, ItemFormModel
from django.db.models import Sum


#------------------------index------------------------------
def index(request):
    expense_list=expense.objects.all()
    data={
        'expense_list': expense_list,
    }
    return render(request,'tracker/index2.html',data)
#------------------------first page "welcome"------------------------------
def welcome(request):
    return render(request,'tracker/welcome.html')
#------------------------detail "for seeing 1 item "------------------------------
def detail(request,expense_id):
    obj=expense.objects.get(pk=expense_id)
    data={
        'obj': obj,
    }
    return render(request,'tracker/detail.html',data)
#------------------------delete------------------------------
def delete_item(request,expense_id):
    obj=expense.objects.get(id=expense_id)
    if(request.method=="POST"):
        obj.delete()
        return redirect('index')
    return render(request, 'tracker/delete_item.html',{'obj': obj})
#------------------------add------------------------------
def add_item(request):
    if request.method=="POST":
        Expense_reason=request.POST.get('Expense_reason')
        Amount=request.POST.get('Amount')
        Image=request.POST.get('Image')
        print("Expense: ",Expense_reason)
        print("in if part")
        obj=expense(Expense_reason=Expense_reason, Amount=Amount, Image=Image)
    
        obj.save()
        form=ItemForm(request.POST)
        return redirect('index')
    else:
        print("in else part")
        form=ItemForm()
        data={'form': form }
        return render(request, 'tracker/addItem.html', data)
#------------------------update------------------------------
def update_item(request,expense_id):
    item=expense.objects.get(id=expense_id)
    form=ItemFormModel(request.POST or None , instance=item)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form': form,
        'item1': item}
    return render(request,'tracker/addItem.html', data)

def unique_user(request):
    salary=0
    if request.method == "POST":
        data=request.POST
        salary=int(data.get('salary', 0))
        Expense_reason=data.get('Expense_reason')
        Amount= int(data.get('Amount', 0))
        Image= data.get('Image')
        
        expense.objects.create(
            user=request.user,
            salary=salary,
            Amount=Amount,
            Expense_reason=Expense_reason,
            Image=Image, 
        )
        return redirect('index')
    queryset= expense.objects.filter(user=request.user.id)
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search')
        )
    total_sum= sum(exp.Amount for exp in queryset)
    context={'expenses': queryset, 'total_sum': total_sum }
    return render(request, 'tracker/index2.html', context )
def pdf(request):
    if request.method=='POST':
        data= request.POST
        salary= int(data.get('salary'))
        Expense_reason=data.get('Expense_reason')
        Amount= int(data.get('Amount', 0))
        Image= data.get('Image')
        print("user in create",request.user)
        expense.objects.create(
            user=request.user,
            salary=salary,
            Amount=Amount,
            Expense_reason=Expense_reason,
            Image=Image, 
            
        )
        return redirect('pdf')
    print("username",request.user.username)
    print("userid",request.user.id)
    queryset= expense.objects.filter(user=request.user.id)
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search')
        )
    print("QuerySet",queryset)
    user = request.POST.get('user')  
    total_sum= expense.objects.filter(user=user).aggregate(total=Sum('Amount'))['total'] or 0
    print("total sum",total_sum)
    username= request.user.username
    context={'expenses':queryset, 'total_sum': total_sum, 'username': username }
    return render(request, 'tracker/pdf.html', context)



    




    

        


    

    



# Create your views here.

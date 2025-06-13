from django.db import models
from django.contrib.auth.models import User
class expense(models.Model):
    def __str__(self):
        return f'Expense:{self.Expense_reason}.'
    
    Expense_reason=models.CharField(max_length=100)
    Amount=models.FloatField(0)
    Image=models.CharField(max_length=500,null=True, default="https://www.lystloc.com/blog/wp-content/uploads/2023/02/How-To-Manage-Field-Employee-Expenses-1.webp")
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    salary= models.IntegerField(default=0)

    

# Create your models here.

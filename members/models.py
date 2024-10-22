from django.db import models
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class User(models.Model):
    userid = models.CharField(max_length=100, unique=True, null=True) 
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.username}"
class expence(models.Model):
    #request.session['uname'] = User.username 
    particular = models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')  # Main user relation
   
    def __str__(self):
        return f'{self.user.username} - {self.amount}'

# Create your models here.

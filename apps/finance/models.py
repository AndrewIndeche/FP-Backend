from django.db import models

# Create your models here.
class Approve(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount=models.DecimalField(decimal_places=2, max_digits=40)

    def __str__(self):
        return self.name

class Support(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message

class Payroll(models.Model):
    MPESA= 'MOBILE'
    DIRECT_DEPOSIT='BANK'

    PAYMENT_TYPES = (
        (MPESA, 'mobile'),
        (DIRECT_DEPOSIT, 'bank account'),
    )
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length =30)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES, default='')
    hours = models.IntegerField(default='0')
    purposes = models.CharField(max_length =30,default='')



class Staff(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount=models.DecimalField(decimal_places=2, max_digits=40)
    position = models.CharField(max_length=100)
    full_name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    work_email=models.CharField(max_length=100)
    personal_email=models.CharField(max_length=100)
    mobile_number=models.IntegerField()
    employee_id=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    date_processed=models.DateTimeField(auto_now_add=True)
    employment_date=models.DateTimeField(auto_now_add=True)
    insurance_number=models.CharField(max_length=100)
    tax_pin_number=models.CharField(max_length=100)
    paye=models.DecimalField(decimal_places=2,max_digits=40)
    gross_pay=models.DecimalField(decimal_places=2,max_digits=40)
    net_pay=models.DecimalField(decimal_places=2,max_digits=40)
    tax_deducted=models.DecimalField(decimal_places=2,max_digits=40)
    insurance=models.DecimalField(decimal_places=2,max_digits=40)
    pension=models.DecimalField(decimal_places=2,max_digits=40)
    sacco=models.DecimalField(decimal_places=2,max_digits=40)
    medical_cover=models.DecimalField(decimal_places=2,max_digits=40)

    @classmethod
    def get_name_by_id(cls, name_id):
        name = cls.objects.get(id=name_id)
        return name

    def __str__(self):
        return self.name

class Expenses(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=40)
    merchant = models.CharField(max_length=100,default='MERCHANTS')
    date_processed = models.DateTimeField(auto_now_add=True)
    approved_expenses = models.IntegerField(default='0')
    total_amount = models.DecimalField(decimal_places=2,max_digits=40,default='0')
    PENDING= 'pending'
    ACCEPTED='accepted'
    REJECTED = 'rejected'

    STATUS = (
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    def __str__(self):
        return self.total_amount

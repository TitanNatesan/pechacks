from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Patient(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,primary_key=True)
    phone = PhoneNumberField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    report = models.ForeignKey("home.XrayReport", on_delete=models.CASCADE,null=True,blank=True)


class XrayReport(models.Model):
    user = models.ForeignKey(Patient,on_delete=models.CASCADE)
    report = models.FileField(upload_to='xray_reports/pdf/')
    src = models.FileField(upload_to='xray_reports/src/')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Xray Report {self.id}"


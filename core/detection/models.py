from django.db import models
import time


# Create your models here.
class Company(models.Model):
    using = 'default'
    CID = models.CharField(max_length=100, primary_key=True, unique=True, null=False)
    Cname = models.CharField(max_length=100)
    Description = models.CharField(max_length=300, null=True)

    class Meta:
        db_table = 'companies'


class Department(models.Model):
    using = 'default'
    DID = models.CharField(max_length=100, primary_key=True, unique=True, null=False)
    Dname = models.CharField(max_length=100)
    # Dmanager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Description = models.CharField(max_length=300, null=True)
    CID = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'departments'


class Employee(models.Model):
    using = 'default'
    EID = models.CharField(max_length=100, primary_key=True, unique=True, null=False)
    CID = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    Password = models.CharField(max_length=100)
    Ename = models.CharField(max_length=100)
    DID = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    ContactNum = models.CharField(max_length=20, null=True)
    Role = models.CharField(max_length=20, choices=(('A', 'admin'), ('M', 'manager'), ('P', 'operator')))

    class Meta:
        db_table = 'employees'


# 为Department新增外键
Department.add_to_class('Dmanager',
                        models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='manager_related',
                                          null=True))


class Sheet(models.Model):
    using = 'default'
    SID = models.CharField(max_length=100, primary_key=True, unique=True, null=False)
    EID = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default='unknown', related_name='employee')
    Production = models.JSONField(null=True)
    OrderDate = models.DateTimeField(null=True)
    TargetDate = models.DateTimeField(null=True)
    EndDate = models.DateTimeField(null=True)
    Approval = models.BooleanField(null=False, default=False)

    def setCNTime(self):
        self.OrderDate.strftime('%Y年%m月%d日 %H时%M分%S秒')
        self.TargetDate.strftime('%Y年%m月%d日 %H时%M分%S秒')
        self.EndDate.strftime('%Y年%m月%d日 %H时%M分%S秒')

    class Meta:
        db_table = 'sheets'


class ADModel(models.Model):
    using = 'default'
    MID = models.CharField(max_length=100, primary_key=True, unique=True, null=False)
    Params = models.JSONField(null=True)
    Description = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = 'models'


class Approvals(models.Model):
    using = 'default'
    AID = models.CharField(max_length=100, primary_key=True, unique=True, null=False)
    RequesterID = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='requester')
    AcceptorID = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='acceptor')
    Content = models.JSONField(null=True)
    Action = models.CharField(max_length=20, null=True)
    State = models.CharField(max_length=20, null=True)


class Image(models.Model):
    name = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    img = models.ImageField(upload_to='image/',
                            default='image/' + str(int(round(time.time() * 1000))) + '.jpg',
                            null=True, blank=True)

    class Meta:
        db_table = 'images'

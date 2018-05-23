from django.db import models

# Create your models here.


class CHCMProject(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(blank=False, null=False, max_length=128)
    location = models.CharField(max_length=32)
    created_date = models.DateField(auto_created=True)
    end_date = models.DateField(null=True)
    active = models.BooleanField()

    def __str__(self):
        return self.project_name

    class Meta:
        managed = True
        db_table = 'chcm_project'


class HeadCount(models.Model):
    record_id = models.AutoField(primary_key=True)
    po_num = models.CharField(max_length=32, blank=True, null=True)
    invoice_num = models.CharField(max_length=32, blank=True, null=True)
    labor_cost = models.BooleanField(default=True)
    date = models.DateField()
    year = models.IntegerField(blank=True, null=True)
    financial_year = models.IntegerField(blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)

    project_id = models.IntegerField(blank=False, null=False, default=1)
    role_id = models.IntegerField(blank=False, null=False, default=1)

    headcountreg = models.FloatField()
    headcountot = models.FloatField()
    ot_rate = models.FloatField(blank=True, null=True)
    comments_reg = models.TextField(blank=True, null=True)
    comments_ot = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_id) + str(self.role_id)

    class Meta:
        managed = True
        db_table = 'chcm_head_count'


class HeadCountPredict(models.Model):
    record_id = models.AutoField(primary_key=True)
    po_num = models.CharField(max_length=32, blank=True, null=True)
    invoice_num = models.CharField(max_length=32, blank=True, null=True)
    labor_cost = models.BooleanField()
    date = models.DateField()
    year = models.IntegerField()
    financial_year = models.IntegerField()
    quarter = models.IntegerField()
    month = models.IntegerField(blank=True, null=True)

    project_id = models.IntegerField(blank=False, null=False, default=1)
    role_id = models.IntegerField(blank=False, null=False, default=1)

    headCount_reg = models.FloatField()
    headCount_ot = models.FloatField()
    ot_rate = models.FloatField()
    comments_reg = models.TextField(blank=True, null=True)
    comments_ot = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_id) + str(self.role_id)

    class Meta:
        managed = True
        db_table = 'chcm_head_count_predict'


class CHCMRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(blank=False, null=False, max_length=128)

    def __str__(self):
        return self.role_name

    class Meta:
        managed = True
        db_table = 'chcm_role'


class CHCMHoliday(models.Model):
    holiday = models.CharField(primary_key=True, max_length=32)
    rate = models.FloatField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'chcm_holiday'

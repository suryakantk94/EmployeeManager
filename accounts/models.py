import uuid
from django.db import models

# Create your models here.
class EmployeeUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    username = models.CharField(max_length=35, unique=True, blank=False, null=False, default='')
    first_name = models.CharField(max_length=30, blank=False, null=False,default='')
    last_name = models.CharField(max_length=30, blank=False, null=False,default='')
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True,default='')
    password = models.CharField(max_length=50, blank=False,default='')

    class Meta:
        db_table = "regdata"



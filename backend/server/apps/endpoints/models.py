from django.db import models

class EndpointInfo(models.Model):
    name = models.CharField(max_length=256)
    owner = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)

class AlgoInfo(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    parent_endpoint = models.ForeignKey(EndpointInfo,on_delete=models.CASCADE)

class AlgoRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    info = models.ForeignKey(AlgoInfo,on_delete=models.CASCADE)


    
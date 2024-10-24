from django.db import models

class CommondBase(models.Model):
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



        
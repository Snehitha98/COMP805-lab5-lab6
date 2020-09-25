from django.db import models
from model_utils.models import TimeStampedModel
class Cheese(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)

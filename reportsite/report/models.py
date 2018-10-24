from django.db import models
from django.utils import timezone

# Create your models here.
class Code(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)
    group = models.ForeignKey('CodeGroup', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class CodeGroup(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    author = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    remark = models.TextField(null=True)
    target_time = models.DateTimeField(
        default=timezone.now)
    created_date = models.DateTimeField(
            default=timezone.now)
    class Meta:
        abstract = True

class App(Report):
    login = models.BooleanField()
    recharge = models.BooleanField()
    wallet = models.BooleanField()
    earn = models.BooleanField()
    gem = models.BooleanField()


class ApplicationLog(Report):
    info = models.IntegerField()
    warn = models.IntegerField()
    error = models.IntegerField()
    cs = models.IntegerField()

class NetworkLog(Report):
    WAN_in = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    WAN_out = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    port15_in = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    port15_out = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    port16_in = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    port16_out = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    p2p_in = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    p2p_out = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    wfd_in = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)
    wfd_out = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True)


class EscalationMatrix(models.Model):
    receiver = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    level = models.IntegerField(default=0)
    responsibility = models.CharField(max_length=30, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.receiver.username


class Incident(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Code',on_delete=models.CASCADE, limit_choices_to={'group__name':'category'}, null=True, blank=True)
    description = models.TextField()
    escalated_to = models.ForeignKey('EscalationMatrix', on_delete=models.CASCADE)
    document = models.ImageField(upload_to='documents/%Y/%m/%d/', null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from pmanager.models import Leaders


class Initi(models.Model):
    mub_name = models.CharField(max_length=250)
    leader = models.ForeignKey(Leaders, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('initiatives:reports', kwargs={'pk': self.pk})

    def __str__(self):
        return self.mub_name


class Goals(models.Model):
    goal = models.CharField(max_length=500)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)

    def __str__(self):
        return self.goal


class Supports(models.Model):
    support = models.CharField(max_length=500)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)

    def __str__(self):
        return self.support


class Reports(models.Model):
    week_ar = models.CharField(max_length=250)
    week_no = models.CharField(max_length=250)
    mub_r = models.ForeignKey(Initi, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('initiatives:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.week_ar + ' ' + self.mub_r.mub_name


class Comment(models.Model):
    report = models.ForeignKey(Reports, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    grade = models.IntegerField(default=0)
    comment = models.TextField(blank=True)


class MainStage(models.Model):
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)
    week_ar = models.ForeignKey(Reports, on_delete=models.CASCADE)
    stage = models.CharField(max_length=250)
    ratio = models.IntegerField(default=0)
    end_date = models.DateField()
    progress_num = models.IntegerField(default=0)
    info = models.TextField()
    final_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.stage


class Risks(models.Model):
    risk = models.CharField(max_length=500)
    mub_risk = models.ForeignKey(Initi, on_delete=models.CASCADE)
    owner_risk = models.CharField(max_length=250)
    probability = models.CharField(max_length=250)
    influence = models.CharField(max_length=250)
    plan = models.TextField()

    def __str__(self):
        return self.risk


class Challenges(models.Model):
    challenge = models.CharField(max_length=500)
    mub = models.ForeignKey(Initi, on_delete=models.CASCADE)
    week_ar = models.ForeignKey(Reports, on_delete=models.CASCADE)
    owner = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    info = models.TextField()


class MdaAdmin(models.Model):
    mda_admin = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.mda_admin.username


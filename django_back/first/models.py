from django.db import models


class JobTitle(models.Model):
    name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)


class Task(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)


class Users(models.Model):
    job_title_id = models.CharField(max_length=800)
    age = models.IntegerField(default=0)
    first_name = models.CharField(max_length=800)
    last_name = models.CharField(max_length=800)
    father_name = models.CharField(max_length=800)


class WorkOnTask(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT)
    task_id = models.ForeignKey(Task, on_delete=models.PROTECT)
    work_date = models.DateField()
    work_time = models.IntegerField(default=0)


from django.db import models


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    code_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class linkedin(models.Model):
    profile_url = models.URLField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.profile_url


class Certificate(models.Model):
    name = models.CharField(max_length=200)

    issuing_organization = models.CharField(max_length=200)

    issue_date = models.DateField()

    credential_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
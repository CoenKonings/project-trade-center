from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return "Course: " + self.name


class Project(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)

    def __str__(self):
        return "Project: " + self.name


class SwitchProposal(models.Model):
    from_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="offers")
    to_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="requests")
    name = models.CharField(max_length=127, unique=True)
    accepted = models.BooleanField(default=False)
    accepted_by = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return "Switch proposal from {} to {} by {} - accepted: {}".format(
            self.from_project, self.to_project, self.name, self.accepted
        )

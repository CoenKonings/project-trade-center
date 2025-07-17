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

    def accept_matches(matches):
        for i in range(len(matches)):
            proposal_a = matches[i]

            for j in range(i + 1, len(matches)):
                proposal_b = matches[j]
                proposal_a.accepted_by.add(proposal_b)

            proposal_a.accepted = True
            proposal_a.save()

    def find_matches(self):
        queue = []
        visited = [self.to_project]
        target_node = self.from_project
        queue.append([self])

        while queue:
            path = queue.pop(0)
            current_node = path[-1].to_project

            if current_node == target_node:
                SwitchProposal.accept_matches(path)

            for edge in current_node.offers.filter(accepted=False):
                if edge.to_project.id not in visited:
                    visited.append(edge.to_project.id)
                    new_path = path.copy()
                    new_path.append(edge)
                    queue.append(new_path)

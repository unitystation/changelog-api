from django.db import models

class BuildVersion(models.Model):
    class Meta:
        ordering = ['-version_number']

    version_number = models.TextField(
        max_length=50,
        primary_key=True,
        help_text="The version number of the build. Must be unique.")

    date_created = models.DateField()

    def __str__(self):
        return f"Build Version {self.version_number} created on {self.date_created}"


class ChangeCategory(models.TextChoices):
    NEW = "NEW", "New"
    IMPROVEMENT = "IMPROVEMENT", "Improvement"
    BALANCE = "BALANCE", "Balance"
    FIX = "FIX", "Fix"


class Change(models.Model):
    class Meta:
        ordering = ['date_added']

    author_username = models.TextField(
        max_length=50,
        verbose_name="Author's Username",
        help_text="The username of the author of the PR")

    author_url = models.URLField(
        max_length=512,
        verbose_name="Author's URL",
        help_text="The URL of the author's GitHub profile")

    description = models.TextField(
        max_length=512,
        verbose_name="Description",
        help_text="A short description of the change")

    pr_url = models.URLField(
        max_length=512,
        verbose_name="PR URL",
        help_text="The URL of the PR that this change is associated with")

    pr_number = models.IntegerField(
        verbose_name="PR Number",
        help_text="The number of the PR that this change is associated with")

    category = models.CharField(
        max_length=11,
        choices=ChangeCategory.choices,
        verbose_name="Category",
        help_text="The category of the change")

    # auto managed fields
    date_added = models.DateField(
        null=True,
        blank=True,
    verbose_name="Date Added",
    help_text="The date that this change was added to the game")

    build = models.ForeignKey(
        BuildVersion,
        on_delete=models.CASCADE,
        related_name="changes",
        null=True,
        default=None,
        verbose_name="Build",
        help_text="The build that this change is associated with")


    def __str__(self) -> str:
        return f"{self.category}: {self.description} by {self.author_username} on PR #{self.pr_number}"

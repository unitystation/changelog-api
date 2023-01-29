from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = CKEditor5Field()
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=12,
        choices=(
            ('no-type', 'No category'),
            ('weekly', 'Weekly update'),
            ('announcement', 'Announcement'),
            ('community', 'Community Highlight'),
        ),
        default='no-type'
    )
    state = models.CharField(max_length=10, choices=(('draft', 'Draft'), ('published', 'Published')), default='draft')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.date_created.year, self.date_created.strftime('%m'), self.date_created.strftime('%d'), self.slug])
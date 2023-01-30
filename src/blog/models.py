from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a title for this post. This will displayed as an H1.')
    slug = models.SlugField(max_length=200, unique=True, help_text='Unique value for post URL, created from title.')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', help_text='Select the author of this post')
    deprecated_body = CKEditor5Field(help_text='Enter the body of this post (deprecated, use sections instead)', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, help_text='Date and time this post was created')
    type = models.CharField(
        max_length=12,
        choices=(
            ('no-type', 'No category'),
            ('weekly', 'Weekly update'),
            ('announcement', 'Announcement'),
            ('community', 'Community Highlight'),
        ),
        default='no-type',
        help_text='Select the type of this post',
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

class Section(models.Model):
    heading = models.CharField(max_length=200, help_text='Enter a heading for this section. This will displayed as an H2.')
    body = CKEditor5Field(help_text='Enter the body of this section')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='sections')

from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class InstagramPost(models.Model):
    photo_url = models.TextField(default='')
    tag_text = models.TextField(default='')
    caption = models.TextField(default='')
    user_name = models.TextField(default='')
    fullname = models.TextField(default='')
    like_count = models.TextField(default='')
    creation_date = models.TextField(default='')
    
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' % (
            self.id,
            self.fullname,
            self.user_name,
            self.caption,
            self.like_count, 
            self.tag_text, 
            self.creation_date
        )

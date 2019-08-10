from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    NOT_RATED = 0
    RATED_G  = 1
    RATED_PG = 2
    RATED_R  = 3
    RATINGS = (
        (NOT_RATED, 'NR-NOT RATED'),
        (RATED_G, 'G-GENERAL AUDIENCES'),
        (RATED_PG, 'PG-PARENTAL GUIDANCES'),
        (RATED_R, 'R-RESTRICTED'),
    )
    title = models.CharField(max_length = 100) #varchar column with length 100
    plot = models.TextField()
    year     = models.PositiveIntegerField()
    rating   = models.IntegerField(choices=RATINGS, default= NOT_RATED)
    runtime  = models.PositiveIntegerField()
    website  = models.URLField(blank = True) # it's varchar -200 by default

    class Meta:
        ordering = ('year', 'title') #ORDER BY year DESC year, title 

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)
# ==========================================================================================================
# creating a vote-model to allow different users to vote movie they love or hate
class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = (
        ('UP', 'u'),
        ('DOWN', 'd'),
    )
    value = models.SmallIntegerField(choices= VALUE_CHOICES)
    # add custom user model not AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)

    class Meta:
    # 'unique_together' attribute of Meta creates a unique constraint on the table. A unique
    # constraint will prevent two rows having the same value for both 'user' and 'movie', enforcing
    # our rule of one vote per user per movie.
        unique_together = ('user', 'movie')



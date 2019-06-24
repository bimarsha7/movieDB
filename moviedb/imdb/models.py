from django.db import models

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

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)
    



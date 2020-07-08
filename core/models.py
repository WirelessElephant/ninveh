from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    is_author = models.BooleanField(default=False)
    is_critic = models.BooleanField(default=True) # Everyone is a critic


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Person, related_name='author', on_delete=models.CASCADE, limit_choices_to={'is_author': True})
    recommender = models.ForeignKey(Person, related_name="recommender", on_delete=models.CASCADE, limit_choices_to={'is_critic': True})
    source = models.URLField(max_length=255)
    amazon_link = models.URLField(max_length=255)
    description = models.TextField()
    book_type = models.CharField(max_length=255)
    book_genre = models.CharField(max_length=255)
    book_length = models.CharField(max_length=255)
    publish_datetime = models.DateTimeField(blank=True, null=True)

    def get_count(self):
        return self.objects.filter(title=self.title, author__name=self.author.name).count()


class BookList(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

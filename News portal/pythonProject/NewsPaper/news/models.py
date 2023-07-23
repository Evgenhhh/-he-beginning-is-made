from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_User = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_Author = models.SmallIntegerField(default=0)

    def update_rating(self):  # не пойму почему подсвечивает предупреждение "objects"
        post_rating = 0
        rating_article_sum = Post.objects.aggregate(post_rating=Sum('rating_article'))
        post_rating += rating_article_sum('post_rating')

        com_autor = 0
        com_autor_sum = Comment.objects.aggregate(com_autor=Sum('comment_user'))
        com_autor += com_autor_sum('com_autor')

        comment_rating_ = 0
        comment_rating_sum = Comment.objects.aggregate(comment_rating_=Sum('comment_rating'))
        comment_rating_ += comment_rating_sum('comment_rating')
        self.author_rating = post_rating * 3 + com_autor + comment_rating_
        self.save()


class Category(models.Model):
    name_Category = models.CharField(max_length=255, unique=True)


news = 'NE'
article = 'AR'

POST = [
    (news, 'Новость'), 
    (article, 'Статья')
]


class Post(models.Model):
    post = models.ForeignKey(Author, on_delete=models.CASCADE)
    field_choice = models.CharField(max_length=2, choices=POST, default=news)
    time_Post = models.DateTimeField(auto_now_add=True)
    post_in = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=30)
    text_article = models.CharField(max_length=1000)
    rating_article = models.IntegerField()

    def like(self):
        self.rating_article += 1
        self.save()

    def dislike(self):
        self.rating_article -= 1
        self.save()

    def preview(self):
        return self.text_article[:124]+'...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.CharField(max_length=255)
    text_coment = models.CharField(max_length=500)
    creation_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField()

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

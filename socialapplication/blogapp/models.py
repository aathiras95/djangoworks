from django.db import models
from django .contrib.auth .models import User
import random

class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to='profilepics',null=True)
    bio=models.CharField(max_length=120)
    phone=models.CharField(max_length=20)
    date_of_birth=models.DateField(null=True)
    options=(
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    gender=models.CharField(max_length=12,choices=options,default='male')
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='users')
    following=models.ManyToManyField(User,related_name='followings',blank=True)


    @property
    def fetch_followings(self):
        return self.following.all()

    @property
    def fetch_following_count(self):
        return self.fetch_followings.count()

    def get_followers(self):
        my_follower=[]
        all_userprofile=UserProfile.objects.all()
        for profile in all_userprofile:
            if self.user in profile.fetch_follwings:
                my_follower.append(profile)
        return my_follower

    def my_follower_count(self):
        return len(self.get_followers())

    @property
    def get_invitations(self):
        alluserprofile=UserProfile.objects.all().exclude(user=self.user)# fetch all users user expect logined user
        user_list=[userprofile.user for userprofile in alluserprofile]
        followinglist=[user for user in self.fetch_followings]# fetch all my following
        invitations=[user  for user in user_list if user not in followinglist]# exclude myfollowings from all users
        return invitations


class Blogs(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=230)
    image=models.ImageField(upload_to='blogimages',null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    posted_date=models.DateTimeField(auto_now=True)
    liked_by=models.ManyToManyField(User)

    @property
    def get_like_count(self):
        like_count=self.liked_by.all().count()
        return like_count

    @property
    def get_liked_user(self):
        liked_users=self.liked_by.all()
        users=[user.username for user in liked_users]
        return  users



    def __str__(self):
        return self.title

class Comments(models.Model):
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment=models.CharField(max_length=160)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


    # fetching  all comments related to blog
    # blog.comments_set.all()
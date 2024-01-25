from django.db import models


class SiteInfo(models.Model):
    site_logo = models.ImageField(upload_to='site_logo/')
    site_name = models.CharField(max_length=100)
    footer_description = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name


class Banner(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    img = models.ImageField(upload_to='banner_photo/')
    partnerships = models.ManyToManyField(to='Brand')

    def __str__(self):
        return self.title


class Brand(models.Model):
    logo = models.ImageField(upload_to='brand_logo/')


class FeaturedHouse(models.Model):
    house_img = models.ImageField(upload_to='house_photo/')
    name = models.CharField(max_length=150)
    HOUSE_TYPE = (
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment')
    )
    type = models.CharField(max_length=150, choices=HOUSE_TYPE)
    price = models.BigIntegerField(default=0)
    HOUSE_STATUS = (
        ('Popular', 'Popular'),
        ("New house", 'New House'),
        ('Best deals', 'Best deals'),
    )
    status = models.CharField(max_length=150, choices=HOUSE_STATUS)
    user_photo = models.ImageField(upload_to='user_photo/')
    user_full_name = models.CharField(max_length=150)
    user_job = models.CharField(max_length=100)
    user_phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    carport = models.IntegerField()
    floors = models.IntegerField()
    photo_and_videos = models.ManyToManyField(to='Files')

    def __str__(self):
        return self.name


class Files(models.Model):
    file = models.FileField(upload_to='photos_and_videos/')


class Testimonials(models.Model):
    house_img = models.ImageField(upload_to='testimonials_house_photo/')
    title = models.CharField(max_length=200)
    comment = models.TextField()
    rating = models.FloatField(default=0)
    user_photo = models.ImageField(upload_to='user_photo/')
    user_full_name = models.CharField(max_length=150)
    user_job = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class AboutHomes(models.Model):
    house_img = models.ImageField(upload_to='about_homes_photo/')
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    user_photo = models.ImageField(upload_to='user_photo/')
    user_full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.address

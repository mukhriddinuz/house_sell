from rest_framework import serializers
from .models import *


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Banner
        fields = '__all__'


class FeaturedHouseSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = FeaturedHouse
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class AboutHomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHomes
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'





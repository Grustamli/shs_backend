from rest_framework import serializers

from .models.user import (
                        Person,
                        UserAddress,
                        PhoneNumber
                        )
from .models.ads import (
                        Ad,
                        AdImage,
                        Favourite,
                        AdAddress
                        )
from .models.categories import Category

from .models.ad_extensions import (
                        Property,
                        Vehicle,
                        )

from django.contrib.auth.models import User




class PhoneNumberListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='phone-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    class Meta:
        model = PhoneNumber
        fields = ('url','number','person')




class PhoneNumberDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='phone-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)

    class Meta:
        model = PhoneNumber
        fields = ('url','number', 'person')



class UserAddressListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    class Meta:
        model = UserAddress
        fields = ('url', 'person', 'address', 'region', 'city')

class UserAddressDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username', read_only=True)
    class Meta:
        model = UserAddress
        fields = ('url', 'person', 'address', 'region', 'city')


class RegisterSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


    class Meta:
        model = Person
        fields = ('username','password','first_name', 'last_name', 'email')



class ProfileListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
    view_name='profile-detail',
    lookup_field='username'
    )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('url','username','password','first_name', 'last_name', 'email')
        # extra_kwargs={
        #     'password':{'write_only':'True'}
        # }

class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='person-detail',
    #     lookup_field='username')

    phone_numbers = serializers.HyperlinkedRelatedField(view_name='phone-detail',read_only=True, many=True)
    addresses = serializers.HyperlinkedRelatedField(view_name='address-detail', read_only=True, many=True)
    ads = serializers.HyperlinkedRelatedField(view_name='ad-detail', lookup_field='slug', read_only=True, many=True)
    favourites = serializers.HyperlinkedRelatedField(view_name='favourite-detail', read_only=True, many=True)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('username','password','first_name', 'last_name', 'email', 'phone_numbers', 'addresses',
        'favourites', 'ads')
        extra_kwargs={
            'phone_numbers':{'read_only':'True'},
            'addresses':{'read_only':'True'},
            'password':{'write_only':'True'}
        }



class AdListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ad-detail', lookup_field='slug')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    category = serializers.HyperlinkedRelatedField(view_name='category-detail',
            queryset=Category.objects.all(),
            lookup_field='name')
    # catalogue = serializers.HyperlinkedRelatedField(view_name='category-detail',
    #         queryset=SubCategory.objects.all())
    class Meta:
        model = Ad
        fields = ('url', 'person', 'title' , 'description' , 'price', 'published',
         'active_from', 'spotlight','category','address')
        extra_kwargs = {
                'category':{'view_name':'category-detail',
                            'lookup_field':'name'}
        }


class AdDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ad-detail', lookup_field='slug')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    images = serializers.HyperlinkedRelatedField(view_name='adimage-detail', read_only=True, many=True)
    address = serializers.HyperlinkedRelatedField(view_name='address-detail', queryset=AdAddress.objects.all())
    category = serializers.HyperlinkedRelatedField(view_name='category-detail',
            queryset=Category.objects.all(),
            lookup_field='name')
    class Meta:
        model = Ad
        fields = ('url','person', 'title' , 'description' , 'price', 'published', 'active_from',
        'spotlight', 'images','address', 'category')



class AdImageListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='adimage-detail')
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            queryset=Ad.objects.all(),
            lookup_field='slug')

    class Meta:
        model= AdImage
        fields = ('url', 'ad', 'image')


class AdImageDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='adimage-detail')
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            lookup_field='slug',
            read_only=True)
    class Meta:
        model= AdImage
        fields = ('url', 'ad', 'image')



class FavouriteListSerializer(serializers.HyperlinkedModelSerializer):
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            queryset=Ad.objects.all(),
            lookup_field='slug')
    url = serializers.HyperlinkedIdentityField(view_name='favourite-detail')
    class Meta:
        model= Favourite
        fields = ('url', 'person', 'ad')


class FavouriteDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='favourite-detail')
    person = serializers.HyperlinkedRelatedField(view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    ad = serializers.HyperlinkedRelatedField(view_name='ad-detail',
            lookup_field='slug',
            read_only=True)
    class Meta:
        model= Favourite
        fields = ('url', 'person', 'ad')



# can implement later
class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail', lookup_field='name')
    categories = serializers.StringRelatedField(many=True)
    main_category = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = ('url','main_category','name','categories')


class PropertyListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='property-detail', lookup_field='id')
    title = serializers.CharField(source='ad.title')
    description = serializers.CharField(source = 'ad.description')
    price = serializers.CharField(source='ad.price')
    address = UserAddressListSerializer(source='ad.address')
    spotlight = serializers.CharField(source='ad.spotlight')
    published = serializers.DateTimeField(source='ad.published')
    active_from = serializers.DateField(source='ad.active_from')



    class Meta:
        model = Property
        fields = ('url','title','price', 'kind','status','no_bed_room','area','spotlight',
                'payment', 'published', 'active_from', 'address', 'description')



class PropertyCreateSerializer(serializers.HyperlinkedModelSerializer):
    ad = AdListSerializer()
    person = serializers.HyperlinkedRelatedField(source='ad.person',
            view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    def create(self, validated_data):
        ad_data = validated_data.pop('ad')
        person_data = validated_data.pop('person')
        ad = Ad.objects.create(person=person_data, **ad_data)
        ads= Ad.objects.get
        property_obj = Property.objects.create(ad=ad, **validated_data)
        return property_obj
    class Meta:
        model = Property
        fields = ('person','ad','kind', 'status', 'no_bed_room', 'area', 'payment')


class PropertyUpdateSerializer(serializers.HyperlinkedModelSerializer):
    ad = AdListSerializer()
    def update(self, instance, validated_data):
        print(validated_data)
        ad_data = validated_data.pop('ad')
        ad = instance.ad

        instance.kind = validated_data.get('kind', instance.kind)
        instance.status = validated_data.get('status', instance.status)
        instance.no_bed_room = validated_data.get('no_bed_room', instance.no_bed_room)
        instance.area = validated_data.get('area', instance.area)
        instance.payment = validated_data.get('payment', instance.payment)
        instance.save()

        ad.title = ad_data.get('title', ad.title)
        ad.price = ad_data.get('price', ad.price)
        ad.description = ad_data.get('description', ad.description)
        ad.active_from = ad_data.get('active_from', ad.active_from)
        ad.spotlight = ad_data.get('spotlight', ad.spotlight)
        ad.category = ad_data.get('category', ad.category)
        ad.address = ad_data.get('address', ad.category)
        ad.save()

        return instance

    class Meta:
        model = Property
        fields = ('ad','kind', 'status', 'no_bed_room', 'area', 'payment')





class PropertyDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='property-detail', lookup_field='id')
    title = serializers.CharField(source='ad.title')
    price = serializers.IntegerField(source='ad.price')
    description = serializers.CharField(source='ad.description')
    address = UserAddressListSerializer(source='ad.address')
    spotlight = serializers.CharField(source='ad.spotlight')
    active_from = serializers.DateField(source='ad.active_from')
    category = serializers.CharField(source='ad.category')
    published = serializers.DateTimeField(source='ad.published')

    class Meta:
        model= Property
        fields= ('url', 'title', 'price', 'description','category', 'spotlight', 'published',
                'active_from', 'kind', 'status', 'no_bed_room', 'area', 'payment', 'address')


class VehicleListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vehicle-detail', lookup_field='id')
    title = serializers.CharField(source='ad.title')
    description = serializers.CharField(source = 'ad.description')
    price = serializers.CharField(source='ad.price')
    address = UserAddressListSerializer(source='ad.address')
    spotlight = serializers.CharField(source='ad.spotlight')
    published = serializers.DateTimeField(source='ad.published')
    active_from = serializers.DateField(source='ad.active_from')
    category = serializers.CharField(source='ad.category')


    class Meta:
        model = Vehicle
        fields = ('url','title','price', 'category', 'make', 'body', 'fuel', 'transmission',
                'mileage', 'year', 'engine_size', 'spotlight', 'published', 'active_from', 'address', 'description')




class VehicleCreateSerializer(serializers.HyperlinkedModelSerializer):
    ad = AdListSerializer()
    person = serializers.HyperlinkedRelatedField(source='ad.person',
            view_name='profile-detail',
            lookup_field='username',
            read_only=True)
    def create(self, validated_data):
        ad_data = validated_data.pop('ad')
        person_data = validated_data.pop('person')
        ad = Ad.objects.create(person=person_data, **ad_data)
        ads= Ad.objects.get
        vehicle_obj = Property.objects.create(ad=ad, **validated_data)
        return property_obj
    class Meta:
        model = Vehicle
        fields = ('person','ad', 'make', 'mileage', 'body', 'fuel', 'transmission', 'year', 'engine_size' )

class VehicleUpdateSerializer(serializers.HyperlinkedModelSerializer):
    ad = AdListSerializer()
    def update(self, instance, validated_data):
        ad_data = validated_data.pop('ad')
        ad = instance.ad

        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.body = validated_data.get('body', instance.body)
        instance.fuel = validated_data.get('fuel', instance.fuel)
        instance.transmission = validated_data.get('transmission', instance.transmission)
        instance.year = validated_data.get('year', instance.year)
        instance.engine_size = validated_data.get('engine_size', instance.engine_size)
        instance.save()

        ad.title = ad_data.get('title', ad.title)
        ad.price = ad_data.get('price', ad.price)
        ad.description = ad_data.get('description', ad.description)
        ad.active_from = ad_data.get('active_from', ad.active_from)
        ad.spotlight = ad_data.get('spotlight', ad.spotlight)
        ad.category = ad_data.get('category', ad.category)
        ad.address = ad_data.get('address', ad.category)
        ad.save()

        return instance

    class Meta:
        model = Vehicle
        fields = ('ad', 'make', 'mileage', 'body', 'fuel', 'transmission',
                    'year', 'engine_size')


class VehicleDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vehicle-detail')
    title = serializers.CharField(source='ad.title')
    price = serializers.IntegerField(source='ad.price')
    description = serializers.CharField(source='ad.description')
    address = UserAddressListSerializer(source='ad.address')
    spotlight = serializers.CharField(source='ad.spotlight')
    active_from = serializers.DateField(source='ad.active_from')
    category = serializers.CharField(source='ad.category')
    published = serializers.DateTimeField(source='ad.published')

    class Meta:
        model = Vehicle
        fields = ('url', 'title', 'price', 'description', 'address', 'spotlight',
                    'active_from', 'category', 'published', 'make', 'mileage',
                    'body', 'fuel', 'transmission', 'year', 'engine_size')

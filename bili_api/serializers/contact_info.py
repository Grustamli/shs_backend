from rest_framework.serializers import RelatedField
from ..models.contact_info import *
from ..models.ads import Ad
from ..models.user import Profile

class AddressRelatedField(RelatedField):

    def to_representation(self, value):
        print('value: ', str(value.__class__))

        # if isinstance(value.content_type, Profile):
        #     return 'Profile ' + value.city
        # elif isinstance(value.content_type, Ad):
        #     return 'Ad ' + value.city
        raise Exception('Unexpected type of address object')

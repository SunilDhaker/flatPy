from rest_framework import serializers
from .models import Venders

class VenderSerializer(serializers.Serializer):
	pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
	name = serializers.CharField( max_length=100)
	vender_type = serializers.CharField( max_length=100000)
	location = serializers.CharField(max_length=50)
	is_varified = serializers.BooleanField() 
	def restore_object(self, attrs, instance=None):
		"""
		Create or update a new snippet instance, given a dictionary
		of deserialized field values.

		Note that if we don't define this method, then deserializing
		data will simply return a dictionary of items.
		"""
		if instance:
			# Update existing instance
			instance.name = attrs.get('name', instance.name)
			instance.vender = attrs.get('vender', instance.vender)
			instance.location = attrs.get('location', instance.location)
			instance.is_varified = attrs.get('is_varified', instance.is_varified)
			
			return instance

		# Create new instance
		return Venders(**attrs)


class BillSerializer(serializers.Serializer):
	pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
	consumer = serializers.Field(source='consumer.username')
	venders = serializers.Field(source='venders.name')
	amount = serializers.CharField( max_length=100000)
	created_at = serializers.DateTimeField()
	is_paid = serializers.BooleanField()
	tax = serializers.CharField(max_length=50)
	# def restore_object(self, attrs, instance=None):
	# 	"""
	# 	Create or update a new snippet instance, given a dictionary
	# 	of deserialized field values.

	# 	Note that if we don't define this method, then deserializing
	# 	data will simply return a dictionary of items.
	# 	"""
	# 	if instance:
	# 		# Update existing instance
	# 		instance.name = attrs.get('name', instance.name)
	# 		instance.vender = attrs.get('vender', instance.vender)
	# 		instance.location = attrs.get('location', instance.location)
	# 		instance.is_varified = attrs.get('is_varified', instance.is_varified)
			
	# 		return instance

	# 	# Create new instance
	# 	return Venders(**attrs)

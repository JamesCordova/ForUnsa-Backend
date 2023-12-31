from django.core.exceptions import ValidationError

class MaxWeightValidator:
    def __init__(self, max_weight):
        self.max_weight = max_weight # We should enter values of MB

    def __call__(self, value):
        if value.size > self.max_weight * 1024 * 1024:
            raise ValidationError(f"File weight should not exceed {self.max_weight} MB.")
        
    def deconstruct(self): # Required for no problems with serializers (post and customUser)
        path = 'apps.forum.validators.MaxWeightValidator'
        args = (self.max_weight,)
        kwargs = {}  # Additional keyword arguments, if any
        return path, args, kwargs
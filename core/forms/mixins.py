

class UserModelFormMixin(object):

    def __init__(self, *args, **kwargs):
        try:
            self.user = kwargs.pop('user')
        except KeyError as e:
            print("KeyError key %s not in kwargs." % e)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super().save(*args, **kwargs)

        if hasattr(self, 'user'):
            self.instance.user = self.user
            self.instance.save()

        return obj

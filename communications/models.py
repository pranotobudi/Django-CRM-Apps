from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from accounts.models import Account

from shortuuidfield import ShortUUIDField


class Communication(models.Model):
    uuid = ShortUUIDField(unique=True)
    TYPE_LIST = (
        (1, 'Meeting'),
        (2, 'Phone'),
        (3, 'Email'),
    )
    subject = models.CharField(max_length=50)
    notes = models.TextField()
    kind = models.PositiveSmallIntegerField(choices=TYPE_LIST)
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'communications'

    def __unicode__(self):
        return u"%s" % self.subject


    def get_absolute_url(self):
        return reverse('comm_detail', args=[self.uuid])

    def get_update_url(self):
        return reverse('comm_update', args=[self.uuid])

    def get_delete_url(self):
        return reverse('comm_delete', args=[self.id])

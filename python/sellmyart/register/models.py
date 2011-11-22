#/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from django.db import models
from django.forms import EmailField, CharField, ModelForm
from manageart.models import ArtModel
from django.contrib.auth.models import User
# Create your models here.

#Django features several builtin forms from django.contrib.auth.forms
class ArtistInfo(models.Model):
    website = models.URLField(blank=True)
    avatar = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    authuser = models.OneToOneField(User, editable=False)
#Deal with client info later when we have invoices and whatever set up

class ArtistInfoForm(ModelForm):
    class Meta:
        model=ArtistInfo
        
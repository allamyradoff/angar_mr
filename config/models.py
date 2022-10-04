# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'car'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dukanlar(models.Model):
    ady = models.CharField(max_length=150)
    welayat = models.CharField(max_length=15)
    salgy = models.CharField(max_length=255)
    tel1 = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15)
    geo = models.CharField(max_length=200)
    user_id_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dukanlar'


class Ussa(models.Model):
    faa = models.CharField(max_length=100, db_collation='utf8mb4_unicode_ci')
    longi = models.CharField(max_length=25)
    lat = models.CharField(max_length=25)
    region = models.CharField(max_length=15, db_collation='utf8mb4_general_ci')
    ugur = models.CharField(max_length=255, db_collation='utf8mb4_general_ci')
    salgy = models.CharField(max_length=255, db_collation='utf8mb4_general_ci')
    tel = models.CharField(max_length=50)
    bellik = models.TextField(db_collation='utf8mb4_general_ci')
    barlandy = models.IntegerField()
    surat = models.CharField(max_length=100)
    rating = models.IntegerField()
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ussa'


class Ussabranches(models.Model):
    ady = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ussabranches'


class Zapcas(models.Model):
    title = models.CharField(max_length=100)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.
    priceusd = models.FloatField(db_column='priceUsd')  # Field name made lowercase.
    priceman = models.FloatField(db_column='priceMan')  # Field name made lowercase.
    notes = models.CharField(max_length=255)
    carids = models.CharField(db_column='carIds', max_length=255)  # Field name made lowercase.
    catid = models.IntegerField(db_column='catId')  # Field name made lowercase.
    yagday = models.IntegerField()
    tel = models.CharField(max_length=100)
    user_id = models.IntegerField()
    car = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zapcas'

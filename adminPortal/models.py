# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminUser(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    pic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CarDetails(models.Model):
    car_id = models.CharField(max_length=100, blank=True, null=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    rider_reg_name = models.CharField(max_length=50, blank=True, null=True)
    rider_phoneno = models.CharField(max_length=50, blank=True, null=True)
    register_datetime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    car_rc_url = models.CharField(max_length=100, blank=True, null=True)
    car_insurance_url = models.CharField(max_length=100, blank=True, null=True)
    rider_carno = models.CharField(max_length=50, blank=True, null=True)
    rider_cartype = models.CharField(max_length=50, blank=True, null=True)
    rider_carmodel = models.CharField(max_length=50, blank=True, null=True)
    rider_license_url = models.CharField(max_length=100, blank=True, null=True)
    rider_adhar_url = models.CharField(max_length=100, blank=True, null=True)
    rider_age = models.CharField(max_length=15, blank=True, null=True)
    car_color = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_details'


class CarInfo(models.Model):
    sr_no = models.AutoField(primary_key=True)
    car_id = models.CharField(max_length=50, blank=True, null=True)
    car_info = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_info'


class CarMaster(models.Model):
    sr_no = models.AutoField(primary_key=True)
    car_id = models.CharField(max_length=50, blank=True, null=True)
    car_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_master'


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


class FcmDjangoFcmdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    registration_id = models.TextField()
    type = models.CharField(max_length=10)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fcm_django_fcmdevice'


class GroupMaster(models.Model):
    sr_no = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    group_desc = models.TextField(blank=True, null=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    group_datetime = models.DateTimeField(blank=True, null=True)
    group_status = models.CharField(max_length=50, blank=True, null=True)
    origin_lat = models.CharField(max_length=50, blank=True, null=True)
    origin_name = models.TextField(blank=True, null=True)
    origin_lng = models.CharField(max_length=50, blank=True, null=True)
    dest_lat = models.CharField(max_length=50, blank=True, null=True)
    dest_name = models.TextField(blank=True, null=True)
    dest_lng = models.CharField(max_length=50, blank=True, null=True)
    total_member = models.CharField(max_length=50, blank=True, null=True)
    group_img_url = models.CharField(max_length=100, blank=True, null=True)
    offer_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_master'


class Notification(models.Model):
    sr_no = models.AutoField(primary_key=True)
    notify_id = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    notify_datetime = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    notify_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'


class RideRequest(models.Model):
    sr_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    rider_id = models.CharField(max_length=50, blank=True, null=True)
    request_status = models.CharField(max_length=50, blank=True, null=True)
    trip_id = models.CharField(max_length=100, blank=True, null=True)
    request_datetime = models.DateTimeField(blank=True, null=True)
    offer_id = models.CharField(max_length=100, blank=True, null=True)
    car_id = models.CharField(max_length=100, blank=True, null=True)
    request_type = models.CharField(max_length=50, blank=True, null=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    notify_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ride_request'


class RiderDetails(models.Model):
    sr_no = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    offer_id = models.CharField(max_length=100, blank=True, null=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    rider_origin_name = models.CharField(max_length=300, blank=True, null=True)
    rider_origin_lat = models.CharField(max_length=50, blank=True, null=True)
    rider_origin_long = models.CharField(max_length=50, blank=True, null=True)
    rider_start_date = models.DateField(blank=True, null=True)
    rider_start_time = models.TimeField(blank=True, null=True)
    ride_stops = models.CharField(max_length=500, blank=True, null=True)
    rider_dest_name = models.CharField(max_length=300, blank=True, null=True)
    rider_dest_lat = models.CharField(max_length=50, blank=True, null=True)
    rider_dest_long = models.CharField(max_length=50, blank=True, null=True)
    ride_datetime = models.DateTimeField(blank=True, null=True)
    ride_status = models.CharField(max_length=50, blank=True, null=True)
    rider_return_date = models.DateField(blank=True, null=True)
    estidatetime = models.CharField(db_column='estiDateTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rider_return_time = models.TimeField(blank=True, null=True)
    ride_distance = models.CharField(max_length=50, blank=True, null=True)
    ride_duration = models.CharField(max_length=50, blank=True, null=True)
    rider_seat = models.IntegerField(blank=True, null=True)
    user_seat = models.IntegerField(blank=True, null=True)
    ride_fare = models.CharField(max_length=50, blank=True, null=True)
    ride_detail = models.CharField(max_length=200, blank=True, null=True)
    car_backsheet = models.CharField(max_length=50, blank=True, null=True)
    offer_type = models.CharField(max_length=20, blank=True, null=True)
    car_id = models.CharField(max_length=50, blank=True, null=True)
    rider_phone_no = models.CharField(max_length=10, blank=True, null=True)
    cancel_datetime = models.DateTimeField(blank=True, null=True)
    ride_comp_datetime = models.DateTimeField(blank=True, null=True)
    notify_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rider_details'


class RiderDetailsOld(models.Model):
    sr_no = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    offer_id = models.CharField(max_length=100, blank=True, null=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    rider_origin_name = models.CharField(max_length=300, blank=True, null=True)
    rider_origin_lat = models.CharField(max_length=50, blank=True, null=True)
    rider_origin_long = models.CharField(max_length=50, blank=True, null=True)
    rider_start_date = models.DateField(blank=True, null=True)
    rider_start_time = models.TimeField(blank=True, null=True)
    ride_stops = models.CharField(max_length=100, blank=True, null=True)
    rider_dest_name = models.CharField(max_length=300, blank=True, null=True)
    rider_dest_lat = models.CharField(max_length=50, blank=True, null=True)
    rider_dest_long = models.CharField(max_length=50, blank=True, null=True)
    ride_datetime = models.DateTimeField(blank=True, null=True)
    ride_status = models.CharField(max_length=50, blank=True, null=True)
    rider_return_date = models.DateField(blank=True, null=True)
    estidatetime = models.CharField(db_column='estiDateTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rider_return_time = models.TimeField(blank=True, null=True)
    ride_distance = models.CharField(max_length=50, blank=True, null=True)
    ride_duration = models.CharField(max_length=50, blank=True, null=True)
    rider_sheet = models.IntegerField(blank=True, null=True)
    user_count = models.IntegerField(blank=True, null=True)
    ride_fare = models.CharField(max_length=50, blank=True, null=True)
    ride_detail = models.CharField(max_length=200, blank=True, null=True)
    car_backsheet = models.CharField(max_length=50, blank=True, null=True)
    offer_type = models.CharField(max_length=20, blank=True, null=True)
    car_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rider_details_old'


class TblChat(models.Model):
    sr_no = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    sender_id = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    message_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_chat'


class TblCities(models.Model):
    name = models.CharField(max_length=30)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_cities'


class TblCountries(models.Model):
    sortname = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_countries'


class TblMsgMaster(models.Model):
    msgid = models.AutoField(primary_key=True)
    msgtype = models.CharField(max_length=30, blank=True, null=True)
    msgbody = models.TextField(blank=True, null=True)
    msgsubject = models.CharField(max_length=100, blank=True, null=True)
    msgfooter = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    custtypeid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_msg_master'


class TblRating(models.Model):
    sr_no = models.AutoField(primary_key=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    user_rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rating'


class TblRideStopover(models.Model):
    rider_id = models.CharField(max_length=50, blank=True, null=True)
    offer_id = models.CharField(max_length=50, blank=True, null=True)
    stopover_lat = models.CharField(max_length=100, blank=True, null=True)
    stopover_long = models.CharField(max_length=100, blank=True, null=True)
    stopover_city = models.CharField(max_length=200, blank=True, null=True)
    stopover_sequence = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    ride_status = models.CharField(max_length=10, blank=True, null=True)
    ride_start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ride_stopover'


class TblShorten(models.Model):
    row_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=11, blank=True, null=True)
    phone_no = models.CharField(max_length=11, blank=True, null=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_shorten'


class TblStates(models.Model):
    name = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_states'


class TripDetails(models.Model):
    sr_no = models.AutoField(primary_key=True)
    trip_id = models.CharField(max_length=100, blank=True, null=True)
    trip_status = models.CharField(max_length=50, blank=True, null=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    user_origin_name = models.CharField(max_length=200, blank=True, null=True)
    user_origin_lat = models.CharField(max_length=50, blank=True, null=True)
    user_origin_long = models.CharField(max_length=50, blank=True, null=True)
    user_date = models.DateField(blank=True, null=True)
    user_time = models.TimeField(blank=True, null=True)
    user_flex_time = models.CharField(max_length=50, blank=True, null=True)
    user_des_name = models.CharField(max_length=200, blank=True, null=True)
    user_dest_lat = models.CharField(max_length=50, blank=True, null=True)
    user_dest_long = models.CharField(max_length=50, blank=True, null=True)
    user_trip_distance = models.CharField(max_length=50, blank=True, null=True)
    user_trip_duration = models.CharField(max_length=50, blank=True, null=True)
    seats = models.CharField(max_length=50, blank=True, null=True)
    estidatetime = models.CharField(db_column='estiDateTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ride_fare = models.CharField(max_length=50, blank=True, null=True)
    offer_id = models.CharField(max_length=100, blank=True, null=True)
    car_id = models.CharField(max_length=50, blank=True, null=True)
    trip_book_datetime = models.DateTimeField(blank=True, null=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    trip_type = models.CharField(max_length=100, blank=True, null=True)
    trip_comp_datetime = models.DateTimeField(blank=True, null=True)
    trip_accept_datetime = models.DateTimeField(blank=True, null=True)
    cancel_datetime = models.DateTimeField(blank=True, null=True)
    notify_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_details'


class UserGroup(models.Model):
    sr_no = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    join_datetime = models.DateTimeField(blank=True, null=True)
    left_datetime = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    rider_id = models.CharField(max_length=100, blank=True, null=True)
    group_status = models.CharField(max_length=50, blank=True, null=True)
    user_status = models.CharField(max_length=8, blank=True, null=True)
    notify_type = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'


class UserInfo(models.Model):
    sr_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    fcm_token = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=15, blank=True, null=True)
    email_id = models.CharField(max_length=50, blank=True, null=True)
    profile_status = models.CharField(max_length=50, blank=True, null=True)
    social_id = models.CharField(max_length=100, blank=True, null=True)
    login_status = models.CharField(max_length=50, blank=True, null=True)
    login_type = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    profile_url = models.CharField(max_length=200, blank=True, null=True)
    phone_no = models.CharField(unique=True, max_length=50, blank=True, null=True)
    user_doc_type = models.CharField(max_length=100, blank=True, null=True)
    user_doc_url = models.CharField(max_length=100, blank=True, null=True)
    user_bio = models.CharField(max_length=100, blank=True, null=True)
    reg_datetime = models.DateTimeField(blank=True, null=True)
    rides_done = models.CharField(max_length=50, blank=True, null=True)
    notify_type = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserInfoOld(models.Model):
    sr_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email_id = models.CharField(max_length=50, blank=True, null=True)
    profile_status = models.CharField(max_length=50, blank=True, null=True)
    social_id = models.CharField(max_length=100, blank=True, null=True)
    login_status = models.CharField(max_length=50, blank=True, null=True)
    login_type = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    profile_url = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(unique=True, max_length=50, blank=True, null=True)
    user_doc_type = models.CharField(max_length=100, blank=True, null=True)
    user_doc_url = models.CharField(max_length=100, blank=True, null=True)
    user_bio = models.CharField(max_length=100, blank=True, null=True)
    reg_datetime = models.DateTimeField(blank=True, null=True)
    rides_done = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info_old'


class VerfiyRequest(models.Model):
    sr_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    request_type = models.CharField(max_length=50, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    request_status = models.CharField(max_length=50, blank=True, null=True)
    approve_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verfiy_request'

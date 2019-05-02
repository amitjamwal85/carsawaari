# Generated by Django 2.1.3 on 2019-04-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'admin_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('pic', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_reg_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_phoneno', models.CharField(blank=True, max_length=50, null=True)),
                ('register_datetime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('car_rc_url', models.CharField(blank=True, max_length=100, null=True)),
                ('car_insurance_url', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_carno', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_cartype', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_carmodel', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_license_url', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_adhar_url', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_age', models.CharField(blank=True, max_length=15, null=True)),
                ('car_color', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'car_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('car_id', models.CharField(blank=True, max_length=50, null=True)),
                ('car_info', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'car_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarMaster',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('car_id', models.CharField(blank=True, max_length=50, null=True)),
                ('car_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'car_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FcmDjangoFcmdevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('registration_id', models.TextField()),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fcm_django_fcmdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupMaster',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.CharField(blank=True, max_length=100, null=True)),
                ('group_name', models.CharField(blank=True, max_length=50, null=True)),
                ('group_desc', models.TextField(blank=True, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('group_datetime', models.DateTimeField(blank=True, null=True)),
                ('group_status', models.CharField(blank=True, max_length=50, null=True)),
                ('origin_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('origin_name', models.TextField(blank=True, null=True)),
                ('origin_lng', models.CharField(blank=True, max_length=50, null=True)),
                ('dest_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('dest_name', models.TextField(blank=True, null=True)),
                ('dest_lng', models.CharField(blank=True, max_length=50, null=True)),
                ('total_member', models.CharField(blank=True, max_length=50, null=True)),
                ('group_img_url', models.CharField(blank=True, max_length=100, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'group_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('notify_id', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('notify_datetime', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('notify_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'notification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RiderDetails',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.CharField(blank=True, max_length=100, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_origin_name', models.CharField(blank=True, max_length=300, null=True)),
                ('rider_origin_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_origin_long', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_start_date', models.DateField(blank=True, null=True)),
                ('rider_start_time', models.TimeField(blank=True, null=True)),
                ('ride_stops', models.CharField(blank=True, max_length=500, null=True)),
                ('rider_dest_name', models.CharField(blank=True, max_length=300, null=True)),
                ('rider_dest_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_dest_long', models.CharField(blank=True, max_length=50, null=True)),
                ('ride_datetime', models.DateTimeField(blank=True, null=True)),
                ('ride_status', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_return_date', models.DateField(blank=True, null=True)),
                ('estidatetime', models.CharField(blank=True, db_column='estiDateTime', max_length=100, null=True)),
                ('rider_return_time', models.TimeField(blank=True, null=True)),
                ('ride_distance', models.CharField(blank=True, max_length=50, null=True)),
                ('ride_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_seat', models.IntegerField(blank=True, null=True)),
                ('user_seat', models.IntegerField(blank=True, null=True)),
                ('ride_fare', models.CharField(blank=True, max_length=50, null=True)),
                ('ride_detail', models.CharField(blank=True, max_length=200, null=True)),
                ('car_backsheet', models.CharField(blank=True, max_length=50, null=True)),
                ('offer_type', models.CharField(blank=True, max_length=20, null=True)),
                ('car_id', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_phone_no', models.CharField(blank=True, max_length=10, null=True)),
                ('cancel_datetime', models.DateTimeField(blank=True, null=True)),
                ('ride_comp_datetime', models.DateTimeField(blank=True, null=True)),
                ('notify_status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'rider_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RiderDetailsOld',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.CharField(blank=True, max_length=100, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_origin_name', models.CharField(blank=True, max_length=300, null=True)),
                ('rider_origin_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_origin_long', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_start_date', models.DateField(blank=True, null=True)),
                ('rider_start_time', models.TimeField(blank=True, null=True)),
                ('ride_stops', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_dest_name', models.CharField(blank=True, max_length=300, null=True)),
                ('rider_dest_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_dest_long', models.CharField(blank=True, max_length=50, null=True)),
                ('ride_datetime', models.DateTimeField(blank=True, null=True)),
                ('ride_status', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_return_date', models.DateField(blank=True, null=True)),
                ('estidatetime', models.CharField(blank=True, db_column='estiDateTime', max_length=100, null=True)),
                ('rider_return_time', models.TimeField(blank=True, null=True)),
                ('ride_distance', models.CharField(blank=True, max_length=50, null=True)),
                ('ride_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('rider_sheet', models.IntegerField(blank=True, null=True)),
                ('user_count', models.IntegerField(blank=True, null=True)),
                ('ride_fare', models.CharField(blank=True, max_length=50, null=True)),
                ('ride_detail', models.CharField(blank=True, max_length=200, null=True)),
                ('car_backsheet', models.CharField(blank=True, max_length=50, null=True)),
                ('offer_type', models.CharField(blank=True, max_length=20, null=True)),
                ('car_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'rider_details_old',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=50, null=True)),
                ('request_status', models.CharField(blank=True, max_length=50, null=True)),
                ('trip_id', models.CharField(blank=True, max_length=100, null=True)),
                ('request_datetime', models.DateTimeField(blank=True, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('car_id', models.CharField(blank=True, max_length=100, null=True)),
                ('request_type', models.CharField(blank=True, max_length=50, null=True)),
                ('group_id', models.CharField(blank=True, max_length=100, null=True)),
                ('notify_status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ride_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblChat',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.CharField(blank=True, max_length=100, null=True)),
                ('sender_id', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('message_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_chat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_cities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortname', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=150)),
                ('phonecode', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMsgMaster',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('msgtype', models.CharField(blank=True, max_length=30, null=True)),
                ('msgbody', models.TextField(blank=True, null=True)),
                ('msgsubject', models.CharField(blank=True, max_length=100, null=True)),
                ('msgfooter', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('custtypeid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_msg_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblRating',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblRideStopover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_id', models.CharField(blank=True, max_length=50, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('stopover_lat', models.CharField(blank=True, max_length=100, null=True)),
                ('stopover_long', models.CharField(blank=True, max_length=100, null=True)),
                ('stopover_city', models.CharField(blank=True, max_length=200, null=True)),
                ('stopover_sequence', models.IntegerField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('ride_status', models.CharField(blank=True, max_length=10, null=True)),
                ('ride_start_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_ride_stopover',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblShorten',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(blank=True, max_length=11, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=11, null=True)),
                ('group_id', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'tbl_shorten',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TripDetails',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('trip_id', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_status', models.CharField(blank=True, max_length=50, null=True)),
                ('device_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user_origin_name', models.CharField(blank=True, max_length=200, null=True)),
                ('user_origin_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('user_origin_long', models.CharField(blank=True, max_length=50, null=True)),
                ('user_date', models.DateField(blank=True, null=True)),
                ('user_time', models.TimeField(blank=True, null=True)),
                ('user_flex_time', models.CharField(blank=True, max_length=50, null=True)),
                ('user_des_name', models.CharField(blank=True, max_length=200, null=True)),
                ('user_dest_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('user_dest_long', models.CharField(blank=True, max_length=50, null=True)),
                ('user_trip_distance', models.CharField(blank=True, max_length=50, null=True)),
                ('user_trip_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('seats', models.CharField(blank=True, max_length=50, null=True)),
                ('estidatetime', models.CharField(blank=True, db_column='estiDateTime', max_length=100, null=True)),
                ('ride_fare', models.CharField(blank=True, max_length=50, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('car_id', models.CharField(blank=True, max_length=50, null=True)),
                ('trip_book_datetime', models.DateTimeField(blank=True, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_type', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_comp_datetime', models.DateTimeField(blank=True, null=True)),
                ('trip_accept_datetime', models.DateTimeField(blank=True, null=True)),
                ('cancel_datetime', models.DateTimeField(blank=True, null=True)),
                ('notify_status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'trip_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.CharField(blank=True, max_length=100, null=True)),
                ('join_datetime', models.DateTimeField(blank=True, null=True)),
                ('left_datetime', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rider_id', models.CharField(blank=True, max_length=100, null=True)),
                ('group_status', models.CharField(blank=True, max_length=50, null=True)),
                ('user_status', models.CharField(blank=True, max_length=8, null=True)),
                ('notify_type', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'user_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=100, null=True)),
                ('fcm_token', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=15, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_status', models.CharField(blank=True, max_length=50, null=True)),
                ('social_id', models.CharField(blank=True, max_length=100, null=True)),
                ('login_status', models.CharField(blank=True, max_length=50, null=True)),
                ('login_type', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_url', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('user_doc_type', models.CharField(blank=True, max_length=100, null=True)),
                ('user_doc_url', models.CharField(blank=True, max_length=100, null=True)),
                ('user_bio', models.CharField(blank=True, max_length=100, null=True)),
                ('reg_datetime', models.DateTimeField(blank=True, null=True)),
                ('rides_done', models.CharField(blank=True, max_length=50, null=True)),
                ('notify_type', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfoOld',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_status', models.CharField(blank=True, max_length=50, null=True)),
                ('social_id', models.CharField(blank=True, max_length=100, null=True)),
                ('login_status', models.CharField(blank=True, max_length=50, null=True)),
                ('login_type', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_url', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('user_doc_type', models.CharField(blank=True, max_length=100, null=True)),
                ('user_doc_url', models.CharField(blank=True, max_length=100, null=True)),
                ('user_bio', models.CharField(blank=True, max_length=100, null=True)),
                ('reg_datetime', models.DateTimeField(blank=True, null=True)),
                ('rides_done', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'user_info_old',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VerfiyRequest',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('request_type', models.CharField(blank=True, max_length=50, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('request_status', models.CharField(blank=True, max_length=50, null=True)),
                ('approve_datetime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'verfiy_request',
                'managed': False,
            },
        ),
    ]

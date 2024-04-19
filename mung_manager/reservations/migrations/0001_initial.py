# Generated by Django 4.2.11 on 2024-04-07 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet_kindergardens', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='daily_reservation_id', db_comment='일일 예약 아이디', primary_key=True, serialize=False)),
                ('reserved_at', models.DateField(db_comment='예약 날짜')),
                ('total_pet_count', models.SmallIntegerField(db_comment='총 반려동물 수', default=0)),
                ('time_pet_count', models.SmallIntegerField(db_comment='시간권 반려동물 수', default=0)),
                ('all_day_pet_count', models.SmallIntegerField(db_comment='종일권 반려동물 수', default=0)),
                ('hotel_pet_count', models.SmallIntegerField(db_comment='호텔 반려동물 수', default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_comment='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, db_comment='수정 일시')),
            ],
            options={
                'db_table': 'daily_reservation',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='reservation_id', db_comment='예약 아이디', primary_key=True, serialize=False)),
                ('is_attended', models.BooleanField(db_comment='출석 여부', null=True)),
                ('reserved_at', models.DateTimeField(db_comment='예약 시간')),
                ('updated_reserved_at', models.DateTimeField(db_comment='예약 수정 시간', null=True)),
                ('attendance_time', models.TimeField(db_comment='출석 시간')),
                ('is_cancelled', models.BooleanField(db_comment='취소 여부', default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_comment='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, db_comment='수정 일시')),
                ('customer', models.ForeignKey(db_comment='고객 아이디', on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='customers.customer')),
                ('customer_pet', models.ForeignKey(db_comment='고객 펫 아이디', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservations', to='customers.customerpet')),
                ('customer_ticket', models.ForeignKey(db_comment='고객 티켓 아이디', on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='customers.customerticket')),
                ('pet_kindergarden', models.ForeignKey(db_comment='펫 유치원 아이디', on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='pet_kindergardens.petkindergarden')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]

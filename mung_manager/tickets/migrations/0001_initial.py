# Generated by Django 4.2.11 on 2024-04-07 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet_kindergardens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='ticket_id', db_comment='티켓 아이디', primary_key=True, serialize=False)),
                ('usage_time_count', models.IntegerField(db_comment='사용 시간 횟수')),
                ('usage_count', models.IntegerField(db_comment='사용 횟수')),
                ('usage_period_in_days_count', models.IntegerField(db_comment='사용 기간(일) 횟수')),
                ('price', models.IntegerField(db_comment='금액')),
                ('ticket_type', models.CharField(choices=[('시간', 'TIME'), ('종일', 'ALL_DAY'), ('호텔', 'HOTEL')], db_comment='티켓 타입', max_length=32)),
                ('deleted_at', models.DateTimeField(blank=True, db_comment='삭제 일시', null=True)),
                ('is_deleted', models.BooleanField(db_comment='삭제 여부', default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_comment='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, db_comment='수정 일시')),
                ('pet_kindergarden', models.ForeignKey(db_comment='펫 유치원 아이디', on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='pet_kindergardens.petkindergarden')),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
    ]

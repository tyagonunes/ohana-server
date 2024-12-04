# Generated by Django 4.2.9 on 2024-12-04 16:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('papel', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Comum')], default=2, verbose_name='Papel')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('metodo_registro', models.IntegerField(choices=[(1, 'Email'), (2, 'Google')], default=1)),
                ('foto_rede_social', models.URLField(blank=True, null=True, verbose_name='Foto rede social')),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Trabalhador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('data_ingresso', models.DateField(blank=True, null=True, verbose_name='Data de ingresso no corpo mediunico')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('telefone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('criado_por', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Trabalhador',
                'verbose_name_plural': 'Trabalhadores',
            },
        ),
        migrations.CreateModel(
            name='Consulente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('telefone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('telefone_whatsapp', models.BooleanField(default=False, verbose_name='Telefone é Whatsapp')),
                ('descricao_medicacao', models.TextField(blank=True, null=True, verbose_name='Quais?')),
                ('motivo_atendimento', models.TextField(blank=True, null=True, verbose_name='Motivo da procura pelo atendimento (o que procura obter?)')),
                ('criado_por', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Consulente',
                'verbose_name_plural': 'Consulentes',
            },
        ),
    ]
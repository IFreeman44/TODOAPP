from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, first_name, last_name, birth_date, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be set.')
        email = self.normalize_email(email)
        if not first_name:
            raise ValueError('First name must be set.')
        if not last_name:
            raise ValueError('Last name must be set.')
        if not birth_date:
            raise ValueError('Birth date must be set.')
        if self.model.objects.filter(email=email).exists():
            raise ValueError('A user with this Email address already exists.')
        user = self.model(email=email, first_name=first_name, last_name=last_name, birth_date=birth_date, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, birth_date, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, first_name, last_name, birth_date, password, **extra_fields)
    

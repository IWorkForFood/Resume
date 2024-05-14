from django import forms
import datetime


class CVForm(forms.Form):

    current_datetime = datetime.datetime.now()
    current_year = current_datetime.year
    DAYS = [('День', 'День')]+[(x, str(x)) for x in range(1, 32)]
    MONTHS = [('Месяц', 'Месяц'),
              (1, 'Январь'),
              (2, 'Февраль'),
              (3, 'Март'),
              (4, 'Апрель'),
              (5, 'Май'),
              (6, 'Июнь'),
              (7, 'Июль'),
              (8, 'Август'),
              (9, 'Сентябрь'),
              (10, 'Октябрь'),
              (11, 'Ноябрь'),
              (12, 'Декабрь')]
    YEARS = [(x, str(x)) for x in range(current_year)]
    YEARS = ([('Год', 'Год')]+ YEARS[::-1])
    ''''''
    LEVELS = [('A1-Начальный', 'A1-Начальный'),
              ('B1-Базовый', 'B1-Базовый'),
              ('В1-Средний', 'В1-Средний'),
              ('В2-Выше среднего', 'В2-Выше среднего'),
              ('С1-Продвинутый', 'С1-Продвинутый'),
              ('С2-Профессиональный', 'С2-Профессиональный')]

    name = forms.CharField(max_length=50,  label='Имя', required=False)
    surname = forms.CharField(max_length=50,  label='Фамилия', required=False)
    position = forms.CharField(max_length=50, label='Желаемая должность', required=False)
    email = forms.EmailField(label='Электронная почта', required=False)
    profile_photo = forms.ImageField(label='Фотография профиля', required=False)
    desired_salary = forms.IntegerField(min_value=0, max_value=1000000000000000000000000, label='Желаемая зарплата', required=False)
    phone = forms.IntegerField(label='Телефон', required=False)
    birthday = forms.ChoiceField(choices = DAYS, widget=forms.Select(attrs={'class':'select'}), label='День рождения', required=False)
    birthmonth = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class':'select'}), label='Месяц рождения', required=False)
    birthyear = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class':'select'}), label='Год рождения', required=False)
    city = forms.CharField(max_length=50, label='Город', required=False)
    citizenship = forms.CharField(max_length=50, label='Гражданство', required=False)
    '''
    language = forms.CharField(max_length=1000, label='Язык')
    knowledge_level = forms.ChoiceField(choices=LEVELS, widget=forms.Select, label='Уровень владения языком')
    '''

    experience_position1 = forms.CharField(max_length=1000, label='Позиция', required=False)
    experience_firm1 = forms.CharField(max_length=1000, label='Компания', required=False)
    position_achieve1 = forms.CharField(max_length=2000, label='Достижения', required=False)
    experience_position2 = forms.CharField(max_length=1000, label='Позиция', required=False)
    experience_firm2 = forms.CharField(max_length=1000, label='Компания', required=False)
    position_achieve2 = forms.CharField(max_length=2000, label='Достижения', required=False)
    experience_position3 = forms.CharField(max_length=1000, label='Позиция', required=False)
    experience_firm3 = forms.CharField(max_length=1000, label='Компания', required=False)
    position_achieve3 = forms.CharField(max_length=2000, label='Достижения', required=False)
    experience_position4 = forms.CharField(max_length=1000, label='Позиция', required=False)
    experience_firm4 = forms.CharField(max_length=1000, label='Компания', required=False)
    position_achieve4 = forms.CharField(max_length=2000, label='Достижения', required=False)

    educational_institution1 = forms.CharField(max_length=300, label='Образование', required=False)
    specialization1 = forms.CharField(max_length=300, label='Специальность', required=False)
    senior_year1 = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class':'select'}), label='Год выпуска', required=False )
    educational_institution2 = forms.CharField(max_length=300, label='Образование', required=False)
    specialization2 = forms.CharField(max_length=300, label='Специальность', required=False)
    senior_year2 = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class':'select'}), label='Год выпуска', required=False)
    educational_institution3 = forms.CharField(max_length=300, label='Образование', required=False)
    specialization3 = forms.CharField(max_length=300, label='Специальность', required=False)
    senior_year3 = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class':'select'}), label='Год выпуска', required=False)

    skill8 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите описания навыков через запятую'}), required=False)
    about_yourself = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80, 'class': 'about-yourself', 'placeholder': 'Расскажите о себе'}), required=False)
data_base = list()
data_base_profile = {}
id = 0

def registr(email:str, password:str, name="AnonymusUser", *args, **kwargs): #логика регистрации 
    email_list = ['@gmail.com', '@yandex.ru', '@mail.ru']
    count = 0

    data = data_base_email(flag=True)

    for user in data:
        if user['email'] == email:
            raise ValueError('Пользователь с таким email существует') 

    for email_name in email_list:
        if email.endswith(email_name):
            count += 1
            break
    
    if not count:
        raise ValueError(f'email должен быть зареган на таких сервисах {email_list}')

    if len(password) >= 8:
        if password == kwargs['password_confirm']:
            print(data_base_email(email=email, password=password, name=name))
            print(f'Пользователь с email-ом: {email} был создан')
        else:
            raise 'Пароли не совпадают'
    else:
        raise 'Длина пароля должно быть не меньше 8 символов'

def data_base_summa(id_user, summa): #базаданных профиля кошелбка
    global id
    data = data_base_email(flag=True)


    for user in data:
        if user["id"] == id_user:
            if user["login"]:
                data_base_profile.update({"id": id, "id_user": id_user, "summa": summa})
                return "Ваш профиль был успешно создан"
            else:
                return "Вы не не залогинились"
        else:
            raise f'нет такого пользователя с id: {id_user}'



def data_base_email(flag=False, **kwargs): #базаданных email
    global data_base, id

    if flag:
        return data_base
    else:
        data_base.append({"id": id, "email": kwargs.get('email'), 'password': kwargs.get('password'), 'first_name': kwargs['name'], 'login': False})
        id += 1
        return f'Пользователь был добален с id: {id}'

def login(*args): #логика авторизации 
    try:
        email = args[0]
        password = args[1]
    except IndexError:
        print("Вы не полностью передал входные данные")
    else:
        data = data_base_email(flag=True)
        for user in data:
            if user.get('email') == email and user.get('password') == password:
                user['login'] = True
                id = user['id']
                return f'Вы успешно залогинелись ваш id: {id}'



dict_acction = {
    1: registr,
    2: data_base_email,
    3: login,
    4: data_base_summa
}

def main(): #главная функция
    TEXT = 'Здорово смотри есть такое, как \n1) регистрация\n2) Вывод базыданных '
    print(TEXT)
    while True:
        number = int(input('Введите выбор: '))
        if number == 0:
            break
        elif number == 1:
            result = dict_acction[1]
            result(email='test@mail.ru', password='12345678', password_confirm='12345678')
        elif number == 2:
            result = dict_acction[2]
            print(result(flag=True))
        elif number == 3:
            result = dict_acction[3]
            print(result('test@mail.ru', '12345678'))
        elif number == 4:
            result = dict_acction[number]
            print(result(0, 15500))
        elif number == 5:
            print(data_base_profile)



if __name__ == '__main__':
    main()

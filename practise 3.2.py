def user_info(name, by, email, tel):
    print('{} rodilsya(las) v {} godu, elektronnyay pochta - {}, nomer telefona {}'.format(name, by, email, tel))


user_info(name=input('fio: '), by=input('god rojdeniya: '), email=input('elektronnaya pochta: '), tel=input('nomer telefona: '))

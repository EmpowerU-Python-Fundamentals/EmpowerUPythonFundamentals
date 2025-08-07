import sys
import os
import ldap

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import module as m
from network_tester import tester as t



# Параметры подключения
## Будут перенесены в основной модуль который будет формировать окно
### И логику программы и передаватся в модули
# ldap_server = '' #'ldap://s-kiev-r03.uvk.ua'
# bind_dn =  '' #'CN=Администратор Федчун Артем,OU=DOMAIN_ADMINS,OU=SYS,OU=GROUPS,OU=UVK,DC=uvk,DC=ua'
# bind_password = '' #'*YfM28~y9u'
# base_dn = '' #'OU=UVK,DC=uvk,DC=ua'
# search_filter = '(&(objectClass=user)(cn=Fedchun Artem))'
search_attributes = ['sAMAccountName', 'displayName', 'mail', 'telephonenumber']
#static variables
l = None
search_info_dict = list()
#Function to work With Ldap
def log_message(message):
    log_file_name = "LDAP.log"
    log_pass = m.get_log_file_path(log_file_name)
    """ Writes a timestamped message to the specified log file. """
    try:
        with open(log_pass, 'a', encoding='utf-8') as log_f:
            log_f.write(f"{m.date_time()}:{message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}") 

def create_list(lst:list, dt:dict):
    lst.append(dt)
    return lst

def create_dict():
    usr_dct = dict()
    return usr_dct

log_message("-----Module For Warcking with LDAP Initialized-----")

# def bind(l_s, b_dn, b_pass):
#     try:
#         l_i = None
#         print("Инициализация соединения...")
#         log_message("Инициализация соединения...")
#         l_i = ldap.initialize(l_s)
#         l_i.set_option(ldap.OPT_REFERRALS, 0)
#         print("Попытка аутентификации...")
#         log_message("Попытка аутентификации...")
#         l_i.simple_bind_s(b_dn, b_pass)
#         print("Аутентификация прошла успешно! ✅")
#         log_message("Аутентификация прошла успешно! ✅")
#     except ldap.LDAPError as e:
#         log_message(f"Произошла ошибка LDAP: {e}")
#         print(f"Произошла ошибка LDAP: {e}")
def bind(ldap_server_uri, bind_dn, bind_password):

    l = None
    try:
        print("Инициализация соединения...") # Сообщение, которое вы видите в консоли
        l = ldap.initialize(ldap_server_uri)
        l.set_option(ldap.OPT_REFERRALS, 0) # Отключить следование за рефералами (часто полезно для AD)
        l.set_option(ldap.OPT_PROTOCOL_VERSION, 3) # Использовать LDAPv3

        print("Попытка аутентификации...") # Сообщение, которое вы видите в консоли
        # Пароль часто требуется в байтах для simple_bind_s
        l.simple_bind_s(bind_dn, bind_password.encode('utf-8')) 
        
        print("Аутентификация прошла успешно! ✅") # Сообщение, которое вы видите в консоли
        return l # <-- КЛЮЧЕВОЙ МОМЕНТ: Возвращаем объект соединения при успехе
    except ldap.INVALID_CREDENTIALS as e:
        print(f"Ошибка LDAP: Неверные учетные данные: {e}")
        if l:
            l.unbind_s()
        return None
    except ldap.SERVER_DOWN as e:
        print(f"Ошибка LDAP: Сервер недоступен: {e}")
        if l:
            l.unbind_s()
        return None
    except ldap.LDAPError as e:
        print(f"Произошла ошибка LDAP: {e}")
        if l:
            l.unbind_s()
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        if l:
            l.unbind_s()
        return None
            
    except Exception as e:
        print(f'Not Correct input: {e}')
        log_message(f'Not Correct input: {e}')
    

def search_user_test(l_ll, bas_dn, search_attribut, dct):#user_name_input
    try:
        print("Попытка поиска...")
        log_message("Попытка поиска...")
        # search_filter = '(&(objectClass=user)(cn=Fedchun Artem))'
        search_filter = '(&(objectClass=user)(cn=*'
        search_filter += search_attribut()
        print(search_filter)
        h = "\\"
        counter = 0
        result_set = l_ll.search_s(bas_dn, ldap.SCOPE_SUBTREE, search_filter, search_attribut)
        print(result_set)
        log_message(f"Result of search {result_set}")
        lst1 = []
        user_list = []
        if result_set:
            print("Пользователь найден! 🎉")
            log_message("Пользователь найден! 🎉")
            for dn, entry in result_set:
                dct = create_dict()
                if dn is not None and entry:  # Проверяем, что DN и entry не пустые
                    f_i = dn.split(',')
                    f_i = f_i[-3::-1]
                    for i in f_i:
                        c = ''
                        c += f"{i}\\"
                        c = c[3::]
                        h += c
                        counter += 1
                    f_i = h[:-1:]
                    print(f"Distinguished Name: {f_i}")
                    log_message(f"Distinguished Name: {f_i}")
                    dct["Distinguished Name"] = f_i
                    for attr, value in entry.items():
                        if value:
                            print(f"  {attr}: {value[0].decode('utf-8')}")
                            log_message(f"  {attr}: {value[0].decode('utf-8')}")
                            dct[attr] = value[0].decode('utf-8')
                        else:
                            print(f"  {attr}: (значение отсутствует)")
                            log_message(f"  {attr}: {value[0].decode('utf-8')}")
                    print(dct)
                    user_list = create_list(lst1, dct)
                    lst1 = user_list
                    # print(f"  {attr}: {value[0].decode('utf-8')}")
                        # log_message(f"  {attr}: {value[0].decode('utf-8')}")
            pars_list_in_dict(lst1)
            return lst1
                    
        else:
            print("Пользователь не найден. 😔")
            log_message("Пользователь не найден. 😔")
        print(user_list)
        lst1 = []
        return user_list

    except ldap.LDAPError as e:
        print(f"Произошла ошибка LDAP: {e}")
        log_message(f"Произошла ошибка LDAP: {e}")
        
    except Exception as e:
        print(f"Error {e}")
        log_message(f"Error {e}")

def create_user():
    pass

def cerate_group():
    pass

def search_group():
    pass

def close_bind(ll):
        ll.unbind_s()
        ll = None
        log_message("Соединение закрыто. 👋")
        print("Соединение закрыто. 👋")

def pars_list_in_dict(list_to_dic):
    for i in list_to_dic:
        print(f"{i} \n")

    

import sys
import os
import ldap

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from keylooker import module as m

def log_message(message):
    log_file_name = "LDAP.log"
    log_pass = m.get_log_file_path(log_file_name)
    """ Writes a timestamped message to the specified log file. """
    try:
        with open(log_pass, 'a', encoding='utf-8') as log_f:
            log_f.write(f"{m.date_time()}:{message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}") 

log_message("-----Module For Working with LDAP Initialized-----")

def bind(ldap_server_uri, bind_dn, bind_password):
    """
    Initializes LDAP connection and performs a simple bind (authentication).
    
    Args:
        ldap_server_uri (str): URI of the LDAP server (e.g., 'ldap://your.server.com:389').
        bind_dn (str): Distinguished Name (DN) of the user for binding.
        bind_password (str): Password of the user for binding.

    Returns:
        ldap.LDAPObject or None: The LDAP connection object on success, otherwise None.
    """
    l = None
    try:
        print("Инициализация соединения...") 
        l = ldap.initialize(ldap_server_uri)
        l.set_option(ldap.OPT_REFERRALS, 0) 
        l.set_option(ldap.OPT_PROTOCOL_VERSION, 3) 

        print("Попытка аутентификации...") 
        
        
        l.simple_bind_s(bind_dn, bind_password.encode('utf-8')) 
        
        print("Аутентификация прошла успешно! ✅") 
        return l # Return the LDAP connection object on success
    except ldap.INVALID_CREDENTIALS as e:
        print(f"Ошибка LDAP: Неверные учетные данные: {e}")
        log_message(f"LDAP Error: Invalid credentials: {e}")
        if l:
            l.unbind_s()
        return None
    except ldap.SERVER_DOWN as e:
        print(f"Ошибка LDAP: Сервер недоступен: {e}")
        log_message(f"LDAP Error: Server down: {e}")
        if l:
            l.unbind_s()
        return None
    except ldap.LDAPError as e:
        print(f"Произошла ошибка LDAP: {e}")
        log_message(f"LDAP Error: {e}")
        if l:
            l.unbind_s()
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        log_message(f"Unexpected error: {e}")
        if l:
            l.unbind_s()
        return None
            
def search_user_test(ldap_connection_object, base_dn, search_filter_string, search_attributes_list):
    """
    Performs an LDAP search for a user.
    
    Args:
        ldap_connection_object (ldap.LDAPObject): An active LDAP connection object.
        base_dn (str): The base Distinguished Name (DN) for the search.
        search_filter_string (str): The LDAP filter string (e.g., "(&(objectClass=user)(cn=John*))").
        search_attributes_list (list): A list of strings representing attributes to retrieve.
        
    Returns:
        list: A list of tuples (dn, entry) for found users, or an empty list.
    """
    if not ldap_connection_object:
        print("Ошибка: LDAP соединение не установлено для поиска.")
        log_message("Error: LDAP connection not established for search.")
        return []
        
    try:
        print("Попытка поиска...")
        log_message("Попытка поиска...")
        
        # Perform the LDAP search
        # Arguments for search_s: base, scope, filterstr, attrlist
        result_set = ldap_connection_object.search_s(
            base_dn,             # Argument 1: The base DN (string)
            ldap.SCOPE_SUBTREE,  # Argument 2: The search scope (constant for subtree search)
            search_filter_string, # Argument 3: The LDAP filter string (string)
            search_attributes_list # Argument 4: The list of attributes to return (list of strings)
        )
        
        print(f"Result of search: {result_set}")
        log_message(f"Result of search: {result_set}")
        
        if result_set:
            print("Пользователь найден! 🎉")
            log_message("Пользователь найден! 🎉")
            return result_set # Return the raw result_set for processing in LDAP_app.py
        else:
            print("Пользователь не найден. �")
            log_message("Пользователь не найден. 😔")
            return [] # Return empty list if no user found

    except ldap.LDAPError as e:
        print(f"Произошла ошибка LDAP при поиске: {e}")
        log_message(f"LDAP Error during search: {e}")
        return []
    except Exception as e:
        print(f"Непредвиденная ошибка при поиске: {e}")
        log_message(f"Unexpected error during search: {e}")
        return []

# These functions are not used 
# def create_user():
#     pass

# def cerate_group():
#     pass

# def search_group():
#     pass

def close_bind(ldap_connection_object):
    """
    Closes the LDAP connection.
    
    Args:
        ldap_connection_object (ldap.LDAPObject): The LDAP connection object to close.
    """
    if ldap_connection_object:
        try:
            ldap_connection_object.unbind_s()
            print("Соединение закрыто. 👋")
            log_message("Соединение закрыто. 👋")
            return True
        except ldap.LDAPError as e:
            print(f"Ошибка LDAP при закрытии соединения: {e}")
            log_message(f"LDAP Error during closing connection: {e}")
            return False
        except Exception as e:
            print(f"Непредвиденная ошибка при закрытии соединения: {e}")
            log_message(f"Unexpected error during closing connection: {e}")
            return False
    else:
        print("Нет активного LDAP соединения для закрытия.")
        log_message("No active LDAP connection to close.")
        return False

from Urls.sites_url import ApplicationData as Url
import requests
class Body:
    @staticmethod
    def build_user_body(email, password, name):
        user_body = {"email": email,
                     "password": password,
                     "name": name}
        return user_body

    @staticmethod
    def build_login_pass_body(email, password):
        login_pass_body = {"email": email,
                           "password": password}
        return login_pass_body

class Request:
    @staticmethod
    def create_user(body_user):
        return requests.post(f'{Url.MAIN_URL}{Url.ENDPOINT_CREATING_ACCOUNT}', json=body_user)

    @staticmethod
    def login_user(login_pass):
        return requests.post(f'{Url.MAIN_URL}{Url.ENDPOINT_LOGIN}', data=login_pass)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{Url.MAIN_URL}{Url.ENDPOINT_USER}',
                               headers={'Authorization': token})
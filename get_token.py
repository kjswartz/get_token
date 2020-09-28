import requests, subprocess, json, sys, getopt

def main():
    try:
        _, args = getopt.getopt(sys.argv[1:], "")
        if len(args) < 2: exit_script()
    except getopt.GetoptError:
        exit_script(2)
    user_dict = dict([('username', args[0]), ('password', args[1])])
    get_token(user_dict)

def get_token(user: dict):
    response = requests.post('https://stage-api.gooee.io/auth/login', data={'username': user['username'], 'password': user['password'] })
    token = response.json()
    print(token['token'])
    subprocess.run('pbcopy', universal_newlines=True, input=token['token'])

def exit_script(code: str = ''):
    print('get_token.py -u <username/email> -p <password>')
    sys.exit(code) if code else sys.exit()

if __name__ == "__main__":
    main()
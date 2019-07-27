
def _get_server_env_vars(host):
	env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
	return dict(l.split('=') for l in env_lines if l)

def create_session_on_server(host, email):
	manage_dot_py = _get_managate_dot_py(host)
	with settings(host_string=f'elspeth@{host}'):
		env_vars = _get_server_env_vars(host)
		with shell_env(**env_vars):
			session_key = run(f'{manage_dot_py} create_session {email}')
			return session_key.strip()
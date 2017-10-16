import sys
import yaml
from bot import ItaBot

if __name__ == '__main__':
    if len(sys.argv) > 1:
        env = sys.argv[1]
        with open('settings.yml', 'r') as settings_yml:
            try:
                settings = yaml.load(settings_yml)
                client_id = settings[env]['client_id']
            except yaml.YAMLError as e:
                exit(e)
            except Exception as e:
                exit(e)
    else:
        exit('ERROR: No command line arguments found.')

    bot = ItaBot()
    bot.run(client_id)

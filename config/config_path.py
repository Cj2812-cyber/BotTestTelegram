import inspect

ROOT_DIRECTORY = inspect.stack()[0][1].replace("config\config_path.py", "")
#print(ROOT_DIRECTORY)

PATH_TO_SAVE_VOICE = ROOT_DIRECTORY + r'static\voice\\' #пусть для сохранения голосовых сообщений для бота

PATH_TO_CLIENT_FROM_ORACLE = r'C:\Oracle\instantclient_19_9' # путь до клиента Oracle необходимый для работы с БД

PATH_TO_HELP = ROOT_DIRECTORY + r'static\file\help\help.txt' # путь к файлу с описанием команда бота

PATH_TO_LOG = ROOT_DIRECTORY + r'static\file\logs_app\\' # путь к файлу для записи лога

PATH_TO_STICS_START = ROOT_DIRECTORY + r'static\stickers\start' # путь к стикерам команды /start
PATH_TO_STICS_HELP = ROOT_DIRECTORY + r'static\stickers\help' # путь к стикерам команды /help


URL_GET_DRAFT = 'http://172.16.40.143/drafts2/internal/api/drafts/v3/' # + order_id. сервис для получения черновика по заявлениям из Cassandra для услуг ЕПГУ 2
PATH_TO_SAVE_DRAFT = ROOT_DIRECTORY + r'static\file\save_draft\\' # путь к сохранению полученных черновиков

URL_GET_FILE_S3 = 'http://p00pgudsnlb01.00.egov.local/hs3/' # + epgu202101/REAL_PATH(14/0/0/23/49/79/4/8NwGd52QBKQP) сервис для получения файлов с хранилища s3
PATH_TO_FILE_S3 = ROOT_DIRECTORY + r'SaveFiles\\' # путь к сохранению полученных черновиков

PATH_TO_SAVE_SSH_FILE = ROOT_DIRECTORY + r'SaveFiles\\' # путь, куда сохранять файлы полученные по ssh

PATH_TO_LOGS_HORUS = '/egov/logs/prod/horus/' # путь к новым логам на сервере логов ЕПГУ, приложений на kubernetes
PATH_TO_LOGS_OLD = '/egov/logs/prod/P0004-PGU/' # путь к старым логам на сервере логов ЕПГУ
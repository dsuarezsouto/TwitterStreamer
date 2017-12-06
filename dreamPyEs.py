from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from time import gmtime, strftime, localtime
import logging, datetime
import time
import os

class FileListener(StreamListener):
    # Constructor
    def __init__(self, path, restart_time):
        self.path = path
        self.current_file = None
        self.restart_time = restart_time
        self.file_start_time = time.time()
        self.file_start_date = datetime.datetime.now()

    # Me llegan los datos de un tweet
    def on_data(self, data):
        # Guardo la fecha
        current_time = datetime.datetime.now()
        # Creo un fichero nuevo si:
        # - No existe fichero anterior( inicializar)
        # - Si se ha superado el tiempo para restart
        # - Si se ha cambiado de dia
        if self.current_file == None or time.time() - self.restart_time > self.file_start_time \
                or self.file_start_date.day != current_time.day:
            self.startFile()
            self.file_start_date = datetime.datetime.now()
        # Escribo los datos en el fichero
        if data.startswith('{'):
            self.current_file.write(data)
            if not data.endswith('\n'):
                self.current_file.write('\n')

    def on_error(self, status_code):
        # Error 420: Rate Limited -> We want disconnect
        logger.error(status_code)
        if status_code == 420:
            exit()
            return False


    def startFile(self):
        if self.current_file:
            self.current_file.close()

        local_time_obj = localtime()
        datetime = strftime("%Y_%m_%d_%H_%M_%S", local_time_obj)
        year = strftime("%Y", local_time_obj)
        month = strftime("%m", local_time_obj)
        day = strftime("%d", local_time_obj)

        full_path = os.path.join(self.path, year)
        full_path = os.path.join(full_path, month)
        full_path = os.path.join(full_path, day)
        try:
            # Creo un directorio con la fecha de hoy
            os.makedirs(full_path)
            logger.info('Created %s' % full_path)
        except:
            pass
        # Creo el fichero de nombre: fecha y hora
        filename = os.path.join(full_path, '%s.json' % datetime)
        #self.current_file = gzip.open(filename, 'w')
        self.current_file = open(filename,'w')
        self.file_start_time = time.time()
        logger.info('Starting new file: %s' % filename)



# Al lanzarlo como script
if __name__ == '__main__':
 
    consumer_key = 'n9j2KmkV3FFWkzgGeq4XdPWCp'
    consumer_secret = 'TszufpKDVtR9rkEkfBS8SdljhqMuxO26ohnUqqDjfTNk2xvJrx'
    access_token = '367437965-UHlGKsxK2WfYNptu2tOPBgT7jxgFvSwJ5fuS59C3'
    access_token_secret = 'qYJQdSzBfdNMPllmA5jU5xJAuyTGxzEs6G7uKRoENRsSu'
    output_directory = 'tweetsEs'
    if not os.path.isdir('log'):
        os.makedirs('log')
    log_filename = 'log/logEs'

    logger = logging.getLogger('tweepy_streaming')
    handler = logging.FileHandler(log_filename, mode='a')
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


    stream_args=['sueño','insomnio','dormir','melatonina','Ambien','zolpidem','edluar','intermezzo','lunesta','#insomnio']
    if not os.path.isdir('pid'):
        os.makedirs('pid')
    pid_file = 'pid/pidSpanish'
    file = open(pid_file, 'w')
    file.write(str(os.getpid()))
    file.close()

    #Creo el Listener:
    # - Con el directorio donde colocar los tweets
    # - Y con el tiempo de crear un fichero nuevo
    listener = FileListener(output_directory, 3600)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    logger.warning("Connecting Process Spanish")
    api = API(auth)
    logger.warning(api.me().name)

    stream = Stream(auth=auth, listener=listener)
    stream.filter(track=stream_args)


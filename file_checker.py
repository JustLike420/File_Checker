import configparser
from datetime import datetime

config = configparser.ConfigParser()
config.read("settings.ini")
config_dict = list(config['FILES'])

for i in range(0, len(config_dict), 2):

    main_file = config['FILES'][config_dict[i]]
    archive_file = config['FILES'][config_dict[i+1]]

    try:
        main = open(main_file)
        lines = main.readlines()
        main.close()

        archive = open(archive_file, 'a')
        new_file = []
        for line in lines:
            check_date = line.split('//')
            if len(check_date) == 2:
                date = line.split('//')[1].strip()
                file_date = datetime.strptime(date, '%d.%m.%Y')

                today = datetime.today()
                today = today.strftime('%d.%m.%Y')
                today = datetime.strptime(today, '%d.%m.%Y')
                if file_date < today:
                    archive.write(line)
                else:
                    new_file.append(line)
            else:
                new_file.append(line)
        main = open(main_file, 'w')
        for line in new_file:
            main.write(line)

    except Exception as e:
        print(e)

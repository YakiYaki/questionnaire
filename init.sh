#! /bin/bash

root_path=app
project_name=questionnaire
email=brmgeometric@yandex.ru

locale-gen "en_US.UTF-8"
export LC_ALL=en_US.UTF-8 
export LANGUAGE=en_US.UTF-8

# Находимся мы в /CocktailManager
# Установим PostgreSQL и nginx
apt-get update
apt-get -y upgrade
apt-get install -y nginx python3 python3.5-dev python3-pip libpq-dev libpcre3 libpcre3-dev

cd /
mkdir $root_path
cd $root_path
mv /$project_name .
mkdir media
mkdir static

# Устанавливаем необходимые компоненты
pip3 install -r conf/requirements.txt

# Настраиваем приложение и создаем суперпользователя
python3 manage.py makemigrations
python3 manage.py migrate
chmod a+w manager.log

mkdir /var/uwsgi
mkdir /var/uwsgi/log
chown www-data:www-data -R /var/uwsgi

echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', '$email', '12345pass')" | python3 manage.py shell
echo yes | python3 manage.py collectstatic

cd /$root_path
chown -R www-data:www-data *
chmod g+rxw -R *

cd /etc/nginx/sites-enabled
unlink default
rm /etc/nginx/sites-available/default
ln -s /$root_path/conf/nginx.conf /etc/nginx/sites-enabled/

uwsgi --ini conf/uwsgi.ini
service nginx restart

echo -e "\n [DONE]"


exit 0
#!/bin/bash

WORK_DIR="/home/box"
PROJ_DIR="$WORK_DIR/web"


init_nginx()
{
	# include our settings to nginx main config
	sudo ln -sf $PROJ_DIR/etc/nginx.conf /etc/nginx/sites-enabled/nginx.conf
	# delete default location settings
	sudo rm -rf /etc/nginx/sites-enabled/default
	# start/restart nginx
	sudo /etc/init.d/nginx restart
}

init_gunicorn()
{
	# delete example settings
	sudo rm /etc/gunicorn.d/*
	# include setting for hello.py to gunicorn
	sudo ln -sf $PROJ_DIR/etc/hello.conf /etc/gunicorn.d/hello.conf
	# start gunicorn
	sudo /etc/init.d/gunicorn start
}


################
####  MAIN  ####
################
case "$1" in
	init)
		init_nginx
		init_gunicorn
	;;
	start)
		sudo /etc/init.d/nginx start
		sudo /etc/init.d/gunicorn start
	;;
	restart)
		sudo /etc/init.d/nginx restart
		sudo /etc/init.d/restart restart
	;;
	stop)
		sudo /etc/init.d/nginx stop
		sudo /etc/init.d/gunicorn stop
	;;
	*)
		echo "Usage: $0 {init|start|stop|restart}" >&2
		exit 1
	;;
esac
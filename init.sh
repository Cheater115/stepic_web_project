#!/bin/bash

WORK_DIR="/home/box"
PROJ_DIR="$WORK_DIR/web"


################
####  MAIN  ####
################
case "$1" in
	init)
		# include our settings to nginx main config
		sudo ln -sf $PROJ_DIR/etc/nginx.conf /etc/nginx/sites-enabled/nginx.conf
		# delete default location settings
		sudo rm -rf /etc/nginx/sites-enabled/default
		# start nginx
		sudo /etc/init.d/nginx stop
		sudo /etc/init.d/nginx start
	;;
	start)
		sudo /etc/init.d/nginx start
	;;
	restart)
		sudo /etc/init.d/nginx restart
	;;
	stop)
		sudo /etc/init.d/nginx stop
	;;
	*)
		echo "Usage: $0 {init|start|stop|restart}" >&2
		exit 1
	;;
esac
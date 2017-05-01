# Flask Youtube Downloader (fyd)

This flask app throws a web-gui front-end on pytube youtube video downloader. 

It works by creating a flat-file queue system and running a worker thread that periodically goes through the queue and downloads all the videos.

Install:
 1. `./prepare.sh` to install dependencies using apt (requires flask, pytube, and gunicorn if you want it)
 2. Use `python run.py` in a terminal to drop into debug mode
 3. Consider using gunicorn for deployment. 

*Foreground Gunicorn Usage*
 1. Install gunicorn from pip: `pip install gunicorn`
 2. Run gunicorn --bind 0.0.0.0:5000 -w 1 "fyd:create_app()"

*Background Gunicorn Usage*
 1. Install gunicorn from apt repository: `sudo apt-get install gunicorn`
 2. Create a gunicorn config file for fyd: `sudo vim /etc/gunicorn.d/fyd`
`CONFIG = {`
`    'mode': 'wsgi',`
`    'working_dir': '/path/to/fyd',`
`      'python': '/usr/bin/python',`
`    'user': 'daemon',`
`    'group': 'daemon',`
`    'args': (`
`        '--bind=0.0.0.0:5000',`
`        '--workers=1',`
`        '--umask=0027',`
`        '--log-level=info',`
`        '--access-logfile=/var/log/gunicorn/fyd_access.log',`
`        'fyd:create_app()',`
`    ),`
`}`

 3. Start the gunicorn server: `service gunicorn start` 

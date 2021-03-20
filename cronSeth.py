from crontab import CronTab

cron = CronTab(user='sppedi1103')
job = cron.new(command='python /home/sppedi1103/python_scripts/instaBot/instaRick/instaSeth.py >> outCron2.txt')
job.every(23).hours()
#job.minute.every(0)
cron.write()


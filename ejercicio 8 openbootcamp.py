import time

hours = int(time.strftime('%H')) 
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

if hours >= 19:
	print (f'Es hora de irse a casa son las {hours}:{minutes}:{seconds}hs') 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- hours, 59-minutes))
# CPX400DP_API
Python class to connect a CPX400DP power supply to the PC with the USB cable

PIP link : https://pypi.org/project/CPX400/0.0.1/
To install : pip install CPX400==0.0.1

<pre><code>
from CPX400DP import *
 
v1= 12			# tension de départ
v2 = 6			# tension d'arrivée
v_step = -1		# delta de tension
t=2				# fréquence des steps en s
 
alim=CPX400DP()

alim.connection()
alim.switchOn()
alim.disconnection()

for v in range(v1, v2, v_step):
	alim.connection()
	print('Tension '+str(v))
	alim.setVoltage(v)
	print('Courrant '+str(alim.getCurrent())+'\n')
	alim.disconnection()
	time.sleep(t)
	
alim.connection()
alim.switchOff()
alim.disconnection()
</code></pre>

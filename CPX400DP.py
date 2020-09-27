import sys
import serial
import serial.tools.list_ports
import time

class CPX400DP:
	
	serialName=None
	serialPort=None
	verbose=False
	def __init__(self):
		pass
		
	def autoDetection(self):
		# produce a list of all serial ports. The list contains a tuple with the port number, 
		# description and hardware address
		ports = list(serial.tools.list_ports.comports())		
		print("Detection des appareils")
		for port_no, description, address in ports:
			print(description)
			if 'CPX400' in description:
				return port_no
		print("Aucun appareil détecté")
		return None
		
	def connection(self, name=None, retry=True, timeout=3):
		cpt=0
		output=False
		while output==False:
			cpt+=1
			if self.verbose: 
				print(str(cpt))
			if name==None:
				if self.serialName==None:
					self.serialName=self.autoDetection()
					#print("Appareil non connecté")
				else:
					name=self.serialName
					if self.verbose: 
						print("Appareil "+name+" présent")
			if self.serialName!=None:
				try:
					# open serial port
					self.serialPort = serial.Serial(name,115200)
					if self.serialPort.name!=None:
						output=True
				except:
					print(self.serialName+" occupée")
					output=False
			if output==False:
				time.sleep(timeout)
		if self.verbose and output: 
			if self.serialPort.name!=None:
				print("Connecté à "+self.serialPort.name)
			else:
				print("Erreur de connection")
		return output
	
	def disconnection(self):
		self.serialPort.close()
	
	def setVoltage(self, v, channel=1):
		cmd='V'+str(channel)+' '+str(v)+'\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
		
	def getVoltage(self):
		return 0.0
	
	def setCurrent(self, i, channel=1):
		cmd='I'+str(channel)+' '+str(v)+'\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
		
	def getCurrent(self, channel=1):
		cmd='I'+str(channel)+'O?\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
		answer=self.serialPort.readline()
		return float(answer[:-3])
	
	def unlock(self):
		cmd='IFUNLOCK\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
	
	def lock(self):
		cmd='IFLOCK\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
		
	def switchOn(self, channel=1):
		cmd='OP'+str(channel)+' 1\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
		
	def switchOff(self, channel=1):
		cmd='OP'+str(channel)+' 0\n'
		self.serialPort.write(bytes(cmd.encode('utf-8')))
	
		
class Laptop:
	def __init__(self,ram,processorSpeed,operatingSystem,memory,usbPorts):
		self.ram = ram
		self.processorSpeed = processorSpeed
		self.operatingSystem = operatingSystem
		self.memory = memory
		self.usbPorts = usbPorts
	
	def save_file(self):
		if self.memory < 2:
			print("Cant save file due to low memory")
		else:
			print("File has been saved")
			
			
lenovo = Laptop('2GB','300mHZ','windows',3,4)
print(lenovo.memory)
lenovo.save_file()

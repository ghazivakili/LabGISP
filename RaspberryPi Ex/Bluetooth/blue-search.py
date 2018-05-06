import bluetooth as bt 
devs = bt.discover_devices(lookup_names=True) 
for addr, name in devs:
	print addr, name

from airline import Spider
for x in range(0,10):
	flight = Spider('DEL','BOM','31/07/2017','2','0','0')
	print(flight.GetDictionary())

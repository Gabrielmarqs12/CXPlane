gnd = "ground"
twr = "tower"
app = "approach"
req = "request"

def start(info):
	for ln in info:
			data = ln.split(":")
			data[1] = data[1].replace('\n','')
			if data[0] == "Callsign":
				cs = data[1]
			elif data[0] == "Departure":
				dp = data[1]
			elif data[0] == "Arrival":
				ar = data[1]
			elif data[0] == "RunWay":
				rwy = data[1]
		print("[V] Information logged")
	pass

def frequency_select(frequency):
    with open("FreqList", "r") as freq
    nbr = freq.readlines()
        for ln in nbr:
            data.split(":")
            data[1] = data[1].replace("\n", "")
            if data[0] == frequency:
                if data[1] = dep:
                return("[V]frequency selected successfully ")
                elif "Approach" in data[3]:
                return("[V]frequency selected successfully ")
                else
                return("[!]Frequency out of range")
            else
            return ("[!]frequency not found")
pass

def recognize(message):
	if gnd in message:
		if req in message:
			if "startup" in message:
				ans = cs += "ready for copy?"
				return ans
	if gnd in message:
		if "ready for copy" in message:
			ans = cs + ", cleared to " + dp + " local flight, runway " + rwy
			return ans
	else:
		ans = cs + " go ahead"
		return ans

	pass

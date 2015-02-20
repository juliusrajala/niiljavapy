import random

def niiloArpoo(kuinkaMonta):
	global joukkueLista
	lohko = []
	for i in range(kuinkaMonta):
		lohko.append(joukkueLista.pop(random.randrange(len(joukkueLista))))
	return lohko

def printtaa():
	print("\nKiltislohko:\n")
	for joukkue in kiltisLohko:
		print(joukkue)
	print("\nRiskilohko:\n")
	for joukkue in riskiLohko:
		print(joukkue)
	print("\nMordorlohko:\n")
	for joukkue in mordorLohko:
		print(joukkue)

def main():
	global kiltisLohko
	global riskiLohko
	global mordorLohko
	kiltisLohko = niiloArpoo(5)
	riskiLohko = niiloArpoo(5)
	mordorLohko = niiloArpoo(4)
	printtaa()


joukkueLista = ["Top Kiek", "EiUle", "MakeJake", "HIFK Kaukalopallo", "TRC.PRO", "Kiprun Rannari", "Turvattomat Karkulaiset", "Pollos Hermanos", "Abo Benisbirds", "Tinoaturpaanjoshavitaan", "HC Loylytys", "Loysat Kivet", "PaitsioRage", "Jahmeat Penikset"]
main()
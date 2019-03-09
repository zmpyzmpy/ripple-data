from ripple_data import exchange_rate
from concept_dirft.adwin import Adwin
import time

base = 'XRP'
counter = 'CNY+razqQKzJRdB4UxFPWf5NEpEG3WMkmwgcXA'
a = exchange_rate.RippleExchangeRate(base,counter)
detector = Adwin()
while True:
	
	value = float(a.exchange_rates())
	result = detector.set_input(value)
	if result:
#		send alert
		pass
	print(value)
	time.sleep(5)
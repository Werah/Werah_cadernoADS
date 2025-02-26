times = ("Fortaleza", "Botafogo", "Palmeiras", "Flamengo", "São Paulo", "Bahia", "Cruzeiro")

print(f"Os cinco primeiros times são: {times[0:5]}")
print(f"Os três ultimos times são: {times[4:7]}")
print(f"Os cinco primeiros times são: {sorted(times)}")
timeDes = times.index(times[3])
print(f"O {times[3]} está na posição: {timeDes + 1}º") 
print("Que Deus tenha piedade do Santos")
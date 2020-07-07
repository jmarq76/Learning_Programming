numeroSegundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

contaDias = numeroSegundos // 86400
restantesSegundos = numeroSegundos % 86400
contaHoras = restantesSegundos // 3600
restantesSegundos = restantesSegundos % 3600
contaMinutos = restantesSegundos // 60
restantesSegundos = restantesSegundos % 60

print(contaDias, "dias,", contaHoras, "horas,", contaMinutos, "minutos e", restantesSegundos, "segundos.")
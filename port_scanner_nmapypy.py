import nmap3
import ipaddress
import re
import socket
import argparse

def validar_destino(destino):
    try:
        ipaddress.ip_address(destino)
        if ipaddress.ip_address(destino).is_private:
            print("Advertencia: Estás escaneando una dirección IP privada.")
        return True
    except ValueError:
        if re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", destino):
            return True
        else:
            print("Error: El destino ingresado no es una IP ni un dominio válido.")
            return False

def escanear_destino(destino, puertos="top"):
    nmap = nmap3.Nmap()
    try:
        print(f"Iniciando escaneo de puertos en {destino}...")
        if puertos == "top":
            results = nmap.scan_top_ports(destino)
        else:
            results = nmap.scan_ports(destino, puertos)
        print("Escaneo finalizado.")
        return results
    except nmap3.exceptions.NmapError as e:
        print(f"Error de Nmap: {e}")
        return None
    except socket.gaierror as e:
        print(f"Error de conexión: {e}. El destino no está disponible o no existe.")
        return None

def guardar_resultados(resultados, filename="resultados.txt"):
    try:
        with open(filename, "w") as f:
            f.write(str(resultados))
        print(f"Resultados guardados en '{filename}'.")
    except Exception as e:
        print(f"Error al guardar resultados: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escanea puertos de un destino.")
    parser.add_argument("destino", help="Dirección IP o dominio a escanear")
    parser.add_argument("-p", "--puertos", help="Puertos específicos (ej: 22,80,443) o 'top' para los principales", default="top")
    parser.add_argument("-o", "--output", help="Archivo para guardar los resultados", default="resultados.txt")
    args = parser.parse_args()

    if not validar_destino(args.destino):
        exit()

    resultados = escanear_destino(args.destino, args.puertos)

    if resultados:
        guardar_resultados(resultados, args.output)
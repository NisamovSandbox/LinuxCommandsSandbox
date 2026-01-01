<!--Terminar de estructurar documento-->

# FTP Secure Channel (SSH)

Máquinas:
- Equipo1: 192.168.115.204
- Equipo2: 192.168.115.205

Instalación de dependecias:
```sh
sudo apt install ftp ufw vsftpd gpg
```
- openssh-server: permite conexiones SSH/SFTP
- vsftpd: servidor FTP
- gpg: cifrado de archivos | [ver tipos de cifrados](/secure_channel/secure_channel_ssh/theory.md)
- ufw: cortafuegos

Acceso al fichero de configuración FTP:
```sh
nano /etc/vsftpd.conf
```
Descomentar `#Port 22`
Este es el puerto por donde se establecerá la comunicación entre equipos, ha de ser cambiado según la situación de la conexión.

Reinicio de servicio SSH:
```sh
sudo service sshd restart
```
Ver claves persistentes exitentes
```sh
gpg -k
```
Generar una nueva clave GPG
```sh
gpg --gen-key
```


<i>Este fichero no está en su versión definitiva</i>
Todavía se está trabajando en este fichero

<!--Por documentar
gpg --symmetric -a ejercicio.txt	>> cifrado simétrico
gpg --symmetric ejercicio.txt	>> cifrado simétrico en binario
gpg --symmetric -o ejercicio.twofish/3des ejercicio.txt	>>pasar a 3des o twofish
gpg --full-generate-key	>>Creación completa de una key (elección de Bits)


sftp {ip}			>>Establecer conexión con el que va a recibir los archivos
put {archivo}			>>Enviar archivo

gpg -a --ouput nombre.key --export email@dominio.com >> crear una key en ascii
gpg --symmetric –a –o mensaje.twofish mensaje.txt (Cuando se encripte con twofish)
gpg -d archivo.key.asc >> Desencriptar archivo
gpg --ouput nombre.key --export email@dominio.com >> crear una key en binario
gpg --encrypt --recipient email@dominio.com archivo.extensión >> Encriptar un documento
gpg –export -a email@dominio.com > archivo.extensión >> Exportar un archivo

-->

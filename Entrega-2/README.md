Create Samba Server on the device


first connect to internet and use the "udhcpc eth0" command to obtain an ip address

then use the "opkg update" to update all libraries

then use "opkg install samba" to install samba on the device

then "mkdir /home/root/sambashare/"

then "opkg install nano" to install nano

then "nano /etc/samba/smb.conf" to edit the samba configuration file ( maybe you need to use ssh to connect to the device)

then add the following lines to the file:<br/>


    [sambashare]
        comment = Samba on Embbeded system 
        path = /home/root/sambashare
        read only = no
        browsable = yes
    


then "smbpasswd -a root" to add a password to the user root

then "systemctl enable smbd" to enable the samba service
then reboot the system or use "systemctl restart smbd" to restart the samba service


now   "sudo smbpasswd -a root" to add a password to the user root
type a password and done

to connect in windows type "\\ipaddress\sambashare" in the file explorer
and use the user root and the password you typed before





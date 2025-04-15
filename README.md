## Configure krb5 (kerberos auth) to play HackTheBox labs.

  **⚠️Kerberos is very sensitive to time and DNS configuration.**


### Recommended:
  > Use latest version of evil-winrm, impacket-* and other tools.


### /etc/hosts config:
  > DNS host order matters

    ✔️<dc_ip>  dc01.example.com exampel.com dc01
    ❌<dc_ip>  example.com dc01.exampel.com dc01

### /etc/resolv.conf:
    nameserver <dc_ip>

### Use domain name instead IP:
    ✔️evil-winrm -r dc01.example.com -i exampel.com
    ❌evil-winrm -r <dc_ip> -i exampel.com
    
### Case sensitive:
    ✔️rosa@EXAMPLE.COM
    ❌rosa@example.com

### Sync time:
    timedatectl set-ntp false
    ntpdate dc01.example.com


### 💀Common Issues:
    Server not found in Kerberos database
    evil-winrm dmalloc(): unaligned fastbin chunk detected
    evil-winrm eRR-S-PRINCIPAL-UNKNOWN
    evil-winrm error on connection to host

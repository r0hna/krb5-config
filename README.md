## Configure krb5 (kerberos auth) to play AD labs.

  **⚠️Kerberos is very sensitive to time and DNS configuration.**


 > [!NOTE]
  > Use latest version of evil-winrm, impacket-* and other tools.


### /etc/hosts config:
  > DNS host order matters

    ✔️<dc_ip>  dc01.example.com example.com dc01
    ❌<dc_ip>  example.com dc01.example.com dc01

### /etc/resolv.conf:
    nameserver <dc_ip>

### Use domain name instead IP:
    ✔️evil-winrm -r dc01.example.com -i example.com
                         OR
    ✔️evil-winrm -r example.com -i dc01.example.com
    ❌evil-winrm -r <dc_ip> -i example.com

> Error: `Server not found in the kerberos database`.

    ✔️impacket-psexec -k -no-pass forest.htb/admin@**forest**
    ❌impacket-psexec -k -no-pass forest.htb/admin@10.10.11.145
    
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
    Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information Matching credential not found

Example:
> evil-winrm -r example.htb -i dc01.example.htb

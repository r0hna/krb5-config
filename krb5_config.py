#!/usr/bin/python3

"""
This script can easily configure /etc/krb5.conf for evil-winrm, by providing a domain fqdn and domain controller name
So that evil-winrm can be used with kerberos authentication

Evil-winrm Example:

```bash
export KRB5CCNAME=Administrator.ccache
evil-winrm -i forest.htb.local -r htb.local
```

Usage: python3 configure_krb5.py <domain_fqdn> <dc_name>
"""
import os
import sys
import argparse


def get_config(domain_fqdn: str, dc_name: str):
    return f"""[libdefaults]
        default_realm = {domain_fqdn.upper()}
        dns_lookup_realm = false
        dns_lookup_kdc = false
        ticket_lifetime = 24h
        forwardable = true

[realms]
        {domain_fqdn.upper()} = {{
                kdc = {dc_name.lower()}.{domain_fqdn.lower()}
                admin_server = {dc_name.lower()}.{domain_fqdn.lower()}
                default_domain = {domain_fqdn.lower()}
        }}

[domain_realm]
        {domain_fqdn.lower()} = {domain_fqdn.upper()}
        .{domain_fqdn.lower()} = {domain_fqdn.upper()}
"""

def request_root():
    if os.geteuid() != 0:
        print("[*] This script must be run as root")
        args = ["sudo", sys.executable] + sys.argv + [os.environ]
        os.execlpe("sudo", *args)

def main():
    parser = argparse.ArgumentParser(description="Configure krb5.conf for kerberos authentication.")
    parser.add_argument("domain_fqdn", help="Domain FQDN")
    parser.add_argument("dc_name", help="Domain Controller hostname")
    args = parser.parse_args()

    request_root()

    config_data = get_config(args.domain_fqdn, args.dc_name)
    print("[*] Configuration Data:")
    print(config_data)

    confirm = input("\n[!] Above Configuration will overwrite /etc/krb5.conf, no cry afterwards? [y/N] ")
    if confirm.lower() != "y":
        print("[!] Aborting")
        sys.exit(1)

    with open("/etc/krb5.conf", "w") as f:
        f.write(config_data)

    print("[+] /etc/krb5.conf has been configured in you system.")

if __name__ == "__main__":
    main()

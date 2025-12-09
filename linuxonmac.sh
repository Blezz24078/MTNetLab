#!/bin/bash

echo "────────────────────────────────────────────"
echo "   macOS FULL HACKING TOOLKIT INSTALLER      "
echo "────────────────────────────────────────────"

# Install Homebrew if missing
if ! command -v brew &> /dev/null; then
  echo "[+] Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "[+] Updating brew..."
brew update

echo "[+] Installing core system utilities..."
brew install git python curl wget jq socat nmap openssl libffi
brew install --cask iterm2

echo "[+] Installing recon & information gathering tools..."
brew install nmap masscan amass whatweb whois dnsenum hping theharvester \
subfinder assetfinder httprobe gospider nuclei

echo "[+] Installing web application pentesting tools..."
brew install sqlmap ffuf gobuster dirsearch nikto wpscan whatweb \
wfuzz feroxbuster

echo "[+] Installing password and hash attack tools..."
brew install hashcat john hydra crunch wordlists

echo "[+] Installing exploitation frameworks..."
brew install metasploit exploitdb beef

echo "[+] Installing mitm, sniffing, spoofing tools..."
brew install wireshark mitmproxy bettercap ettercap tcpdump \
dsniff tshark sslstrip

echo "[+] Installing network analysis and recon tools..."
brew install netcat ncat nmap zmap arp-scan dnsmap traceroute \
massdns fping

echo "[+] Installing forensic & OSINT tools..."
brew install binwalk sleuthkit autopsy exiftool foremost \
pdfcrack stegseek steghide

echo "[+] Installing reverse engineering tools..."
brew install radare2 ghidra gdb apktool dex2jar jd-cli \
jadx binutils

echo "[+] Installing wireless & radio (limited on macOS)..."
brew install aircrack-ng kismet reaver blueutil

echo "[+] Installing misc hacker tools..."
brew install sqlcipher tor torsocks proxychains-ng \
hashpump hydra medusa \
zbar knock knockpy spooftooph

echo "────────────────────────────────────────────"
echo "  ALL TOOLS INSTALLED SUCCESSFULLY!"
echo "  Your macOS 'Kali-style' environment is ready."
echo "────────────────────────────────────────────"


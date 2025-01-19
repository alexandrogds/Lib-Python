import subprocess
import sys

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
        sys.exit(1)

def install_chocolatey():
    # Verifique se o Chocolatey já está instalado
    try:
        run_command("choco --version")
        print("Chocolatey já está instalado.")
    except subprocess.CalledProcessError:
        # Se o Chocolatey não estiver instalado, instale-o
        print("Instalando Chocolatey...")
        run_command('@"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin"')

def install_nodejs_and_npm():
        print("Instalando NodeJS e NPM...")
        run_command('choco install nodejs.install')

if __name__ == "__main__":
    install_chocolatey()

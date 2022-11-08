import os


class Configuration():

    @staticmethod
    def update() -> None:
        os.system('sudo apt update')
        os.system('clear')
        print('Updated Sucefully')

    @staticmethod
    def gnome() -> None:
        # Per modificare la DOC e le Finestre
        os.system("sudo apt install gnome-tweaks -y")
        os.system("sudo apt install gnome-shell-extensions -y")

    @staticmethod
    def nvim() -> None:
        os.system("sudo apt install neovim -y")

    @staticmethod
    def vscode() -> None:
        os.system("sudo apt install snapd")
        os.system("sudo snap install --classic code")

    @staticmethod
    def discord() -> None:
        os.system("sudo apt install snapd")
        os.system("sudo snap install discord")

    @staticmethod
    def chrome() -> None:
        os.system(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo apt install ./google-chrome-stable_current_amd64.deb -y")

    @staticmethod
    def spotify() -> None:
        os.system("sudo apt install snapd")
        os.system("sudo snap install spotify")

    @staticmethod
    def alacritty() -> None:
        # alacritty download
        os.system(" sudo add-apt-repository ppa:aslatter/ppa -y")
        os.system("sudo apt install alacritty -y")

    @staticmethod
    def cpp() -> None:
        os.system("sudo apt-get install c++ -y")

    @staticmethod
    def rust_lang() -> None:
        os.system("sudo apt install curl")
        os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

    @staticmethod
    def pascal() -> None:
        os.system("sudo apt install fpc -y")

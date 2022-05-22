try:
    import requests, ctypes, time, os, threading, platform
    from colorama import Fore
except ImportError:
    input("Hata Gereksinimler.txt Dosyasındaki Gereksinimlere Uyulmuyor ")

ascii_text = """
        _   _ _    _        _    
       | | (_) |  | |      | |   
       | |_ _| | _| |_ ___ | | __
       | __| | |/ / __/ _ \| |/ /
       | |_| |   <| || (_) |   < 
        \__|_|_|\_\\__\___/|_|\ _\\ - İsim Kontrol Edici -! Paradox#0001
  """


if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"

class tiktok:

    def __init__(self):
        self.lock = threading.Lock()
        self.checking = True
        self.usernames = []
        self.unavailable = 0
        self.available = 0
        self.counter = 0

    def update_title(self):
        remaining = len(self.usernames) - (self.available + self.unavailable)
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"TikTok İsim Kontrol Edici | Aktif: {self.available} | Kullanılamaz: {self.unavailable} | Kontrol Edildi: {(self.available + self.unavailable)} | Kontrol Ediliyor: {remaining} | Geliştirildi -! Paradox#0001 Tarafından"
        )
    
    def safe_print(self, arg):
        self.lock.acquire()
        print(arg)
        self.lock.release()
    
    def print_console(self, status, arg, color = Fore.RED):
        self.safe_print(f"       {Fore.WHITE}[{color}{status}{Fore.WHITE}] {arg}")
    
    def check_username(self, username):
        if username.isdigit():
            self.unavailable += 1
            self.print_console("Kullanılamaz", username)
            return
        with requests.Session() as session:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "content-type": "application/json"
            }
            r = session.head("https://www.tiktok.com/@{}".format(username), headers = headers)
            if r.status_code == 200:
                self.unavailable += 1
                self.print_console("Kullanılamaz", username)
            elif r.status_code == 404:
                self.available += 1
                self.print_console("Kullanılabilir Ya Da Banlı", username, Fore.GREEN)
                with open("Kullanılabilir.txt", "a") as f:
                        f.write(username + "\n")
            self.update_title()
 
    def load_usernames(self):
        if not os.path.exists("isimler.txt"):
            self.print_console("Asistan", "Hata isimler.txt bulunamadı")
            time.sleep(10)
            os._exit(0)
        with open("isimler.txt", "r", encoding = "UTF-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                self.usernames.append(line)
            if not len(self.usernames):
                self.print_console("Asistan", "")
                time.sleep(10)
                os._exit(0)

    
    def main(self):
        os.system(clear)
        if clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW("TikTok İsim Kontrol Edici | ! Paradox#0001 Tarafından Geliştirildi")
        print(Fore.RED + ascii_text)
        self.load_usernames()
        threads = int(input(f"       {Fore.WHITE}[{Fore.GREEN}Asistan{Fore.WHITE}] Hız Belirleyin Önerilen (5 10): "))
        print()
        if threads >= 5: #To prevent ratelimits
            threads = 5
        
        def thread_starter():
            self.check_username(self.usernames[self.counter])
        while self.checking:
            if threading.active_count() <= threads:
                try:
                    threading.Thread(target = thread_starter).start()
                    self.counter += 1
                except:
                    pass
                if len(self.usernames) <= self.counter:
                    self.checking = None

obj = tiktok()
obj.main()
input()

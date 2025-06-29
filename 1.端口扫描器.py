import socket

ip = input("请输入要扫描的ip地址（例如127.0.0.1）： ")
open_ports = []  # 用于存储开放的端口

# 扫描1到1024窗口
for port in range(1,1025):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip,port))
        if result ==0:
            print(f"端口{port}是开放的")
            open_ports.append(port)

        s.close()
    except socket.gaierror:
        print("无效的IP地址！请检查输入。")
        break
    except socket.error:
        print("无法连接目标主机")
        break


print("\n扫描完成，开放的端口有：",open_ports)
import hashlib


def calc_unlock_code(mac: str, sn: str) -> str:
    # 移除 MAC 地址中的冒号并转为大写
    mac = mac.replace(":", "").strip().upper()
    # 移除 SN 序列号的首尾空格并转为大写
    sn = sn.strip().upper()

    # 将 MAC + SN + "XIAOMI" 拼接后编码为 UTF-8 字节
    data = (mac + sn + "XIAOMI").encode("utf-8")
    # 计算 SHA-256 哈希值
    digest = hashlib.sha256(data).digest()

    # 取前 10 个字节，每个字节对 10 取模，拼接成 10 位数字解锁码
    return "".join(str(digest[i] % 10) for i in range(10))

if __name__ == "__main__":
    mac = input("请输入设备 MAC 地址 (如 AA:BB:CC:DD:EE:FF): ").strip()
    sn = input("请输入设备 SN 序列号: ").strip()
    print(f"code: {calc_unlock_code(mac, sn)}")
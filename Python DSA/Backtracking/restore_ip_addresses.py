"""
RESTORE IP ADDRESSES - Medium
Restore valid IP addresses from string
"""

def restore_ip_addresses(s):
    result = []
    def backtrack(start, parts):
        if start == len(s) and len(parts) == 4:
            result.append('.'.join(parts))
            return
        if len(parts) >= 4:
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if (segment[0] != '0' or len(segment) == 1) and int(segment) <= 255:
                backtrack(end, parts + [segment])
    backtrack(0, [])
    return result


if __name__ == "__main__":
    print("✅ Restore Ip Addresses")

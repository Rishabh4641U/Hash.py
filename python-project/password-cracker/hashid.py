import re
import hashlib
def identify_hash(hash_string):
    hash_string = hash_string.strip()
    lenght = len(hash_string)
    results = []


# ------------pattern based detection---------------------------

    patterns = {
        "bcrypt"          : r"^\$2[ayb]\$.{56}$",
        "MD5 Crypt"       : r"^\$1\$.+\$.+$",
        "SHA256 Crypt"    : r"^\$5\$.+\$.+$",
        "SHA512 Crypt"    : r"^\$6\$.+\$.+$",
        "MySQL 4.1+"      : r"^\*[A-f0-9]{40}$",
        "NTLM"            : r"^[0-9a-fA-F]{32}$",
        "LM hash"         : r"^[A-f0-9]{32}:[A-f0-9]{32}$",
        "Argon2"          : r"^\$argon2.+",
    }
    
    #-----------lenght based detection ----------------------------
    lenght_map = {
        32     : ["MD5", "NTLM", "MD4"],
        40     : ["SHA1", "RIPEMD-160"],
        56     : ["SHA224"],
        64     : ["SHA256", "SHA3-256", "BLAKE2s"],
        96     : ["SHA384"],
        128    : ["SHA512,", "SHA3-512", "BLAKE2b", "Whirlpool"],
    
    }
    
    
    if lenght in lenght_map:
        for h in lenght_map[lenght]:
            if h not in results:
                results.append(h)
    return results

def crack_hint(hash_types):
    hints = {
        "MD5"        : "hashcat -m 0",
        "SHA1"       : "hashcat -m 100",
        "SHA256"     : "hashcat -m 1400",
        "SHA512"     : "hashcat -m 1700",
        "NTLM"       : "hashcat -m 1000",
        "bcrypt"     : "hashcat -m 3200",
        "SHA512 Crypt": "hashcat -m 1800",
        "MD5 Crypt"  : "hashcat -m 500",
        "LM Hash"    : "hashcat -m 3000",
        "MySQL 4.1+" : "hashcat -m 300",
    }

    for h in hash_types:
        if h in hints:
            return hints[h]
    return "Unknoen - try: hashcat --identify <hash>"


def generate_hash(text):
    print("\n[*] Generating hashes for:", text)
    print("-" * 45)
    algos = {
        "MD5"      : hashlib.md5,
        "SHA1"     : hashlib.sha1,
        "SHA256"   : hashlib.sha256,
        "SHA512"   : hashlib.sha512,
        "SHA224"   : hashlib.sha224,
        "SHA384"   : hashlib.sha384,
    }


    for name, func in algos.items():
        h = func(text.encode()).hexdigest()
        print(f"  {name:<8}:{h}")

def main():
    print("=" * 50)
    print("       hash identifier Tool")
    print("=" * 50)

    while True:
        print("\n[1] identifier a hash")
        print("[2] Generate hashes from text")
        print("[3] Exit")

        choice = input("\n[?] Choose option: ").strip()

        #  ----------option 1 : identify------------------

        if choice == "1":
            hash_input = input("\n[? Paste Your hash: ]").strip()

            if not hash_input:
                print("[-] No hash entered!")
                continue

            print(f"\n[*] Analyzing: {hash_input[:30]}....")
            print(f"[*] Lenght : {len(hash_input)} charaters")
            print("-" * 50)

            results = identify_hash(hash_input)

            if results:
                print(f"[+] Possible hash Tupe : ")
                for i, r in enumerate(results, 1):
                    print(f"      {i}. {r}")

                hint = crack_hint(results)
                print(f"   {hint}")

            else:
                print("[-] Could not identify hash type.")
                print("[*] Try: https://hashes.com/en/tools/hash_identifier")


        #  ------------- option 2: Generate-----------------
        elif choice == "2":
            text = input("\n[?] Enter text to hash: ").strip()
            if not text:
                print("[-] Not text entered!")
                continue
            generate_hash(text)

        # --------------------option 3: exit -------------------------------
        elif choice == "3":
            print("\n[*] Exiting .......... stay ethical! with abhishek💫✨💫")
            break
        else:
            print("[-] Invaid option. choose 1, 2,3.")

if __name__ == "__main__":
    main()






    

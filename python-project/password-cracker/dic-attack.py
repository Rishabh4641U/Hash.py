import hashlib
import os
import sys

def crack_hash(target_hash, wordlist_file):
    # first we have to check wordlist file exits
    if not os.path.exists(wordlist_file):
        print(f"[-] wordlit file not found{wordlist_file}")
        return None
    
    print(f"[*]Starting dictionary attack....")
    print(f"[*] Target hash: {target_hash}")
    print(f"[*] Wordlist: {wordlist_file}")
    print("_" * 40)

    count = 0

    with open(wordlist_file, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if not word:
                continue
            # try hashing every word
            attempt = hashlib.sha256(word.encode()).hexdigest()

            if attempt == target_hash:
                print(f"[+] Password Found after {count} attemps!")
                print(f"[+] Password found: {word}")
                return word
    print(f"[-] password are not found {count} Attempts.")
    return None

def main():
    print("=" * 40)
    print(" SHA256 Dictionary Attack Tool")
    print("=" * 40)

    # enter the hash
    target = input("\n[?] Enter target SHA256 hash: ").strip()

    # if user write invaild hash
    if len(target) != 64:
        print("[-] Invaild SHA256 hash! must be 64 characters.")
        sys.exit(1)

    # wordlist path
    print("\n[?] Enter wordlist path")
    print("Path: common-password-list/rockyou.txt/rockyou_1.txt")
    wordlist = input("   path  :").strip()

    # run the aatack
    result = crack_hash(target, wordlist)

    if result is None:
        print("\n[-] Attack failed. try a different wordlist.")
    else:
        print(f"\n[+] SUCCESS! password: {result}")


if __name__ == "__main__":
    main()


import hashlib

def crack_hash(target_hash, wordlist_file):
    with open(wordlist_file, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            # try hashing every word
            attempt = hashlib.sha256(word.encode()).hexdigest()

            if attempt == target_hash:
                print(f"[+] Password found: {word}")
                return word
    print("[-] password are not found")

# here you put hash and output password
target = input("Please enter your hash : ")
crack_hash(target, "rockyou.txt")


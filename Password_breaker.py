import itertools, time, string
pw = input("Password: ").strip()
print("Sets: 1.A+0-9[36]\n 2.a+0-9[36]\n 3.A+0-9+![46]")
print("4.a+0-9+![46] \n5.0-9+![20] \n6.Aa+0-9+![72]")
print("7.A[26]\n 8.a[26]\n 9.0-9[10]\n 10.![10]")
c = input("Choice: ")
sets = {
    "1": string.ascii_uppercase + string.digits,
    "2": string.ascii_lowercase + string.digits,
    "3": string.ascii_uppercase + string.digits + "!@#$%^&*",
    "4": string.ascii_lowercase + string.digits + "!@#$%^&*",
    "5": string.digits + "!@#$%^&*",
    "6": string.ascii_letters + string.digits + "!@#$%^&*",
    "7": string.ascii_uppercase,
    "8": string.ascii_lowercase,
    "9": string.digits,
    "10": "!@#$%^&*()"
}
chars = sets.get(c, string.ascii_letters + string.digits + "!@#$%^&*")
start, attempts = time.time(), 0
timeout, last_print = 1800, start
print(f"\nTarget: {len(pw)} chars | Set: {len(chars)} chars")

for length in [len(pw)]:
    for combo in itertools.product(chars, repeat=length):
        attempts += 1
        now = time.time()
        
        if now - last_print >= 1:
            if now - start > timeout:
                print(f"\n⏰ 30min up! {attempts:,} tries")
                quit()
            print(f"Time: {int(now-start)}s | Tries: {attempts:,}", end='\r')
            last_print = now       
        if ''.join(combo) == pw:
            print(f"\n✅ Found: {pw} in {now-start:.1f}s")
            print(f"Tries: {attempts:,}")
            quit()
print(f"\n❌ Failed after {attempts:,} tries")
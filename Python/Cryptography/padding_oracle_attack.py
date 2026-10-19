# Padding oracle attack on AES CBC mode
import base64
import subprocess
from urllib.parse import unquote, quote


BLOCK_SIZE = 16

def askOracle(ciphertext) -> bool:
    # Returns True if the ciphertext has valid padding
    # In this case this is our oracle, just openssl command ran locally
    cmd = f"echo -n '{ciphertext}' | xxd -r -p -c 0 | openssl aes-256-cbc -nosalt -d -K 70617373776f7264 -iv 70616473616764617061647361676461 1>/dev/null 2>&1"
    r_process = subprocess.run(cmd, shell=True)
    return not bool(r_process.returncode)

def decrypt(ciphertext:str, blocks:list, encoding="hex") -> str:
    plain_text_block = ""
    x = iv = [0] * BLOCK_SIZE
    ciphertext = bytes.fromhex(ciphertext)
    print(f"[+] Decrypting block {blocks[1]}")
    for position in range(15, -1, -1):
        #print(f"[+] Searching at position {position}")
        pad_value = BLOCK_SIZE - position
        iv = [0] * BLOCK_SIZE
		# First: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 for finding value at position 15 that results in 01 padding in the block plaintext
		# Second: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 X^01
		# Third : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 X^02 X^02
        for i in range(1, pad_value + 1):
            iv[-i] = x[-i] ^ pad_value
        for v in range(256):
            iv[position] = v
            bytes_iv = bytearray(iv)
            copy_blocks = list(blocks)
            copy_blocks[0] = bytes_iv.hex()
            if askOracle("".join(copy_blocks)):
                #print(f"[+] Possible value found: {format(v, '#02x')}")
                if confirmFinding(copy_blocks, 0, iv, position):
                    #print(f"[+] Value found: {format(v, '#02x')}")
                    x[position] = iv[position] ^ pad_value
                    break
        else:
            print("[!] Error")
            exit()
    for v1, v2 in zip(bytes.fromhex(blocks[0]), x):
        plain_text_block += format(v1 ^ v2, "02x")
    return f"[+] Decrypted plaintext: {plain_text_block}"

def confirmFinding(blocks:list, block:int, iv:list, position:int):
	# When the position is 15, we need to confirm that the resulting padding
	# is 01. Because if the padding at position 14 is 02 we will get that
	# 02 padding at position 15 is correct. The same with 03, if the padding at
	# 13 is 03 and 14 is 03 (which is correct for 03 padding), then 03 at position
	# 15 is correct. But we are searching for the value that makes 01 padding
	# at position 15 correct
    if position != 15:
		# It is only necessary to check when the position is 15 since only
		# at position 15 we might get correct values for other paddings different
		# than 01, and at position 15 we are searching for the value that results
		# in 01 padding
        return True
    print(f"[+] Cheking if the value found is correct since we are at position 15")
    iv[position - 1] ^= 1
    bytes_iv = bytearray(iv)
    blocks[0] = bytes_iv.hex()
    return askOracle("".join(blocks))

def base64Encode(string:str):
    return base64.b64encode(string)

def paddingOracleAttack(ciphertext:str, iv:str, encoding="hex"):
	# It is easier to visualize with hex encoding rather than with base64 encoding
    if encoding == "base64":
        ciphertext_base64 = ciphertext
        ciphertext = base64.b64decode(ciphertext.encode("utf-8").decode()).hex()
    if len(ciphertext) % 2 != 0:
        raise ValueError("The length of the ciphertext is invalid for a hexadecimal value")
    if len(iv) % 2 != 0:
        raise ValueError("The length of the iv is invalid for a hexadecimal value")

    blocks = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]
    for i in range(0, len(blocks), 2):
        print(decrypt(ciphertext, blocks[i:i+2], encoding="hex"))
    print(decrypt(ciphertext, [iv, ciphertext[:32]], encoding="hex"))


def main():
    paddingOracleAttack("240e915d3b4c953373548ffccd953f4e83b4db43466c969b43de34b4a07b9805", iv="70616473616764617061647361676461", encoding="hex")

if __name__ == "__main__":
    main()

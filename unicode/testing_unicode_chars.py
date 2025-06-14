
# Test with ZERO WIDTH SPACE: https://unicode-explorer.com/c/200B
print("Testing ZERO WIDTH SPACE (U+200B): ​Prova di car​attere invisi​bile")

# Test with ZERO WIDTH NON-JOINER: https://unicode-explorer.com/c/200C
print("Testing ZERO WIDTH NON-JOINER (U+200C):‌ Prova di cara‌ttere non uni‌to")

# Test with ZERO WIDTH JOINER: https://unicode-explorer.com/c/200D
print("Testing ZERO WIDTH JOINER (U+200D):‍ ‍Prova‍ di cara‍ttere uni‍to‍")

# Test with RTL MARK: https://unicode-explorer.com/c/200F
print(u"Testing RIGHT-TO-LEFT MARK (U+200F):⁧ Prova di carattere da destra a sinistra")
# Test with LEFT-TO-RIGHT MARK: https://unicode-explorer.com/c/200E
print("Testing LEFT-TO-RIGHT MARK (U+200E):‎ Prova di car‎attere da sinistra a destra")


# Test with a network call:
import requests
url = "https://ᖯin.org/get" # Punycode convert it to -> https://xn--httpin-z84a.org/get

# Make a GET request to the URL
response = requests.get(url)
# Print the response text
print(f"Response from {url}: {response.text}")
import cv2

# -------------------- LZW COMPRESSION --------------------

def lzw_compress(uncompressed):
    """Compress a list of integers using LZW."""

    # Build the dictionary
    dict_size = 256

    dictionary = {
        bytes([i]): i for i in range(dict_size)
    }

    w = b""
    compressed = []

    for k in uncompressed:

        c = bytes([k])
        wc = w + c

        if wc in dictionary:
            w = wc

        else:
            compressed.append(dictionary[w])

            dictionary[wc] = dict_size
            dict_size += 1

            w = c

    if w:
        compressed.append(dictionary[w])

    return compressed


def lzw_decompress(compressed):
    """Decompress LZW output."""

    dict_size = 256

    dictionary = {
        i: bytes([i]) for i in range(dict_size)
    }

    w = bytes([compressed.pop(0)])

    result = bytearray(w)

    for k in compressed:

        if k in dictionary:
            entry = dictionary[k]

        elif k == dict_size:
            entry = w + w[:1]

        else:
            raise ValueError(
                "Bad compressed k: %s" % k
            )

        result += entry

        dictionary[dict_size] = w + entry[:1]

        dict_size += 1
        w = entry

    return list(result)


# -------------------- MAIN SCRIPT --------------------

# Load grayscale image
image_path = 'rapunzel1.jpg'

img = cv2.imread(
    image_path,
    cv2.IMREAD_GRAYSCALE
)

if img is None:
    raise FileNotFoundError("Image not found.")


# Flatten image to 1D
pixels = img.flatten().tolist()


# -------------------- LZW --------------------

lzw_encoded = lzw_compress(pixels)

# Estimate LZW size
lzw_size_bytes = len(lzw_encoded) * 2

# Decode to verify
lzw_decoded = lzw_decompress(
    lzw_encoded.copy()
)

assert lzw_decoded == pixels, \
    "LZW decompression failed!"


# -------------------- Compression Ratio --------------------

original_size_bytes = len(pixels)

lzw_ratio = (
    original_size_bytes / lzw_size_bytes
    if lzw_size_bytes else 0
)


print("Original Image Size (approx):",
      original_size_bytes, "bytes")

print("LZW Compressed Size (approx):",
      lzw_size_bytes, "bytes")

print(f"LZW Compression Ratio: {lzw_ratio:.2f}:1")


# -------------------- Display Image --------------------

cv2.imshow("Original Image(CS24246)", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
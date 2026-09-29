import cv2

# -------------------- RUN LENGTH ENCODING (RLE) --------------------

def rle_encode(data):
    """Run Length Encode a 1D list of values."""

    encoding = []

    prev = data[0]
    count = 1

    for pixel in data[1:]:
        if pixel == prev:
            count += 1
        else:
            encoding.append((prev, count))
            prev = pixel
            count = 1

    encoding.append((prev, count))

    return encoding


def rle_decode(encoding):
    """Run Length Decode back to original data."""

    data = []

    for value, count in encoding:
        data.extend([value] * count)

    return data


# -------------------- MAIN SCRIPT --------------------

# Load grayscale image
image_path = 'rapunzel1.jpg'

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found.")


# Flatten image to 1D for RLE
pixels = img.flatten().tolist()


# -------------------- RLE --------------------

rle_encoded = rle_encode(pixels)

# Estimate RLE size
rle_size_bytes = len(rle_encoded) * 2

# Decode to verify
rle_decoded = rle_decode(rle_encoded)

assert rle_decoded == pixels, "RLE decompression failed!"


# -------------------- Compression Ratio --------------------

original_size_bytes = len(pixels)

rle_ratio = (
    original_size_bytes / rle_size_bytes
    if rle_size_bytes else 0
)


print("Original Image Size (approx):",
      original_size_bytes, "bytes")

print("RLE Compressed Size (approx):",
      rle_size_bytes, "bytes")

print(f"RLE Compression Ratio: {rle_ratio:.2f}:1")


# -------------------- Display Image --------------------

cv2.imshow("Original Image(CS24246)", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
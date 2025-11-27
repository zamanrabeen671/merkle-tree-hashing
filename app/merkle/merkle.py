import hashlib

def sha256(data: bytes):
    return hashlib.sha256(data).hexdigest()

def build_merkle_tree(chunks):
    layer = [sha256(c) for c in chunks]

    if len(layer) == 0:
        return None

    while len(layer) > 1:
        next_layer = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i+1] if i+1 < len(layer) else left
            next_layer.append(sha256((left + right).encode()))
        layer = next_layer

    return layer[0]

#!/usr/bin/env python3

import hashlib
import os
import sys

url = sys.argv[1]
checksum = sys.argv[2]

if checksum.startswith("sha256:"):
    h = hashlib.sha256
    checksum = checksum[7:]
else:
    raise Exception("Unknown hash function")

def verify():
    with open(archive, "rb") as f:
        actual_checksum = h(f.read()).hexdigest()
    result = actual_checksum == checksum
    if result:
        print("Checksum verified")
    else:
        print("Checksum verification failed")
        print("Expected", checksum)
        print("But got:", actual_checksum)

    return result

archive = url.split("/")[-1]
archive = os.path.join("_sources", archive)

if os.path.exists(archive):
    if verify():
        sys.exit(0)
    print("Removing archive", archive)
    os.remove(archive)

# FIXME: Replace use of wget, just use python instead
if os.system(f"cd _sources && wget {url}") != 0:
    print("Failed to download")
    sys.exit(1)

if not verify():
    sys.exit(2)

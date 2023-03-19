

def encodeGeohash(lat, lng, bits):
    minLat = -90
    maxLat = 90
    minLng = -180
    maxLng = 180
    result = 0
    for i in range(bits):
        if i % 2 == 0:                # even bit: bisect longitude
            midpoint = (minLng + maxLng) / 2
            if lng < midpoint:
                result <<= 1                 # push a zero bit
                maxLng = midpoint            # shrink range downwards
            else:
                result = result << 1 | 1     # push a one bit
                minLng = midpoint            # shrink range upwards
        else:# odd bit: bisect latitude
            midpoint = (minLat + maxLat) / 2
            if lat < midpoint:
                result <<= 1                 # push a zero bit
                maxLat = midpoint            # shrink range downwards
            else:
                result = result << 1 | 1     # push a one bit
                minLat = midpoint            # shrink range upwards
    return hex(result);
one = encodeGeohash(12.02345, 45.23, 8)
two = encodeGeohash(12.04, 45.23, 8)
three = encodeGeohash(57.64911,10.40744, 8)
print(one)
print(two)
print(three)

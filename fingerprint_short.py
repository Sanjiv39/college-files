from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword():
        print('Waiting for finger...')

        while f.readImage() == False:
            pass

        print('Fingerprint detected!')

except Exception as e:
    print('Error: ' + str(e))

TRANSMIT_RT = 1/(54.0 * 10**6)   # spb
PAYLOAD = 1452 * 8 # bits
HEADER = 28 * 8  # bits
ACK = 14 * 8  # bits
RTS = 20 * 8  # bits
CTS = 14 * 8  # bits
SIFS = 16 * 10**(-6)    # s
DIFS = 34 * 10**(-6)    # s
BACKOFF = 36 * 10**(-6) # s

print("Params:")
print("TRANSMIT_RT", TRANSMIT_RT)
print("PAYLOAD", PAYLOAD)
print("HEADER", HEADER)
print("ACK", ACK)
print("RTS", RTS)
print("CTS", CTS)
print("SIFS", SIFS)
print("DIFS", DIFS)
print("BACKOFF", BACKOFF)

print("Calculating throughput for 3.1:")

bitsTransferred = PAYLOAD + HEADER + ACK
timeTaken = (bitsTransferred * TRANSMIT_RT) + DIFS + BACKOFF

throughput = bitsTransferred / timeTaken
print("Bits transferred:", bitsTransferred)
print("Time taken:", timeTaken)
print("Throughput:", throughput)

print("\nCalculating throughput for 3.2:")

bitsTransferred = RTS + CTS + PAYLOAD + HEADER + ACK
timeTaken = (bitsTransferred * TRANSMIT_RT) + (3*SIFS) + DIFS + BACKOFF
throughput = bitsTransferred / timeTaken
print("Bits transferred:", bitsTransferred)
print("Time taken:", timeTaken)
print("Throughput:", throughput)
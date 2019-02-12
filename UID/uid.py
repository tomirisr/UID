#!/usr/bin/env python3

import base2, base16, base58, base64, baseX
from base2 import convert
from datetime import datetime
import time
##############################################################################################################################################################################
#  A uid class based on time, counter, and shard id.                                                                                                                         #
#                                                                                                                                                                            #
# |                | Time Component                 | Time Component                            | Space Component                                                            |
# |----------------|--------------------------------|-------------------------------------------|----------------------------------------------------------------------------|
# | Number of Bits | 42 bits                        | 13 bits                                   | 8 bits                                                                     |
# | Description    | Milliseconds since Jan, 1970   | Counter (allows more than one UID per ms) | Shard ID (assigned explicitly to a server, process, or database)           |
# | Maximum Value  | 4,398,046,511,104 (May, 2109)  | 8,192 per ms                              | 256 unique locations                                                       |


# range is 0-255
#this shard Id is a constant because it will be the same for each computer that will be used 
SHARD_ID = 67

# sizes
MILLIS_BITS = 42
COUNTER_BITS = 13
SHARD_BITS = 8

# the masks
MILLIS_MASK = (2**MILLIS_BITS - 1) << (COUNTER_BITS + SHARD_BITS)
COUNTER_MASK = (2**COUNTER_BITS - 1) << (SHARD_BITS)
SHARD_MASK = (2**SHARD_BITS - 1)


LAST_MILLIS = 0
MAX_COUNTER = 2**COUNTER_BITS
COUNTER = 0
EPOCH = datetime(1970, 1, 1)

def pack(millis, counter, shard):
    '''Combines the three items into a single uid number'''
    bit_millis = millis << (COUNTER_BITS + SHARD_BITS)
    bit_counter = counter << SHARD_BITS
    uid = bit_millis | bit_counter | shard
    return uid


def unpack(uid):
    '''Separates the uid into its three parts'''
    millis = (uid & MILLIS_MASK) >> (COUNTER_BITS + SHARD_BITS)
    counter = (uid & COUNTER_MASK) >> SHARD_BITS
    shard = uid & SHARD_MASK
    return (millis, counter, shard)

def generate(base=10):
    '''Generates a uid with the given base'''
    global LAST_MILLIS
    global COUNTER
    # get the millisecond, waiting if needed if we've hit the max counter
    while True:
        millis= int((datetime.utcnow()- EPOCH).total_seconds()*1000)
        if COUNTER < MAX_COUNTER or LAST_MILLIS !=millis:
            break
        time.sleep(3)

    # reset the counter if we are in a new millisecond
    COUNTER+=1
    if millis != LAST_MILLIS:
        COUNTER = 0
    LAST_MILLIS = millis
    # pack it up and convert base
    uid = pack(millis, COUNTER, SHARD_ID)
    return uid

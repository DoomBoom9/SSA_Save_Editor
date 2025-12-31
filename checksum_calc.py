#!/usr/bin/env python3

#Wii Save File FNV-1a Checksum Calculator
#Checksum at offset 0x30C


#ssa's checksum algo
#Calculate FNV-1a 32-bit hash
def fnv1a_32(data):
    FNV_OFFSET_BASIS = 0x811c9dc5
    FNV_PRIME = 0x01000193
    
    hash_value = FNV_OFFSET_BASIS
    for byte in data:
        hash_value = ((hash_value ^ byte) * FNV_PRIME) & 0xFFFFFFFF
    
    return hash_value


def verify_and_fix_checksum(filename):
    with open(filename, 'rb') as f:
        save_data = bytearray(f.read())
    
    #read existing checksum
    existing_checksum = int.from_bytes(save_data[0x30C:0x310], 'big')
    print(f"File: {filename}")
    print(f"File size: {len(save_data)} bytes")
    print(f"Existing checksum at 0x30C: 0x{existing_checksum:08X}")

    if len(save_data) != 800:
        print(f"Warning: Expected 800 bytes, got {len(save_data)}")
    
    data_to_hash = save_data[0:0x30C]
    
    print(f"Hashing {len(data_to_hash)} bytes (excluding checksum at 0x30C)")
    
    #calculate correct checksum
    calculated_checksum = fnv1a_32(data_to_hash)
    print(f"Calculated checksum:        0x{calculated_checksum:08X}")

    #validity checks
    if existing_checksum == calculated_checksum:
        print("Checksum is VALID")
        return True
    else:
        print("Checksum is INVALID")
        
        #fix file prompt (probably could improve later)
        response = input("\nWrite correct checksum to file? (y/n): ")
        if response.lower() == 'y':
            save_data[0x30C:0x310] = calculated_checksum.to_bytes(4, 'big')
            
            output_filename = filename.replace('.bin', '_fixed.bin') 
            if output_filename == filename:
                output_filename = filename + '_fixed'
            
            with open(output_filename, 'wb') as f:
                f.write(save_data)
            
            print(f"Fixed checksum written to: {output_filename}")
            return False
        else:
            print("No changes made")
            return False

if __name__ == "__main__":
    import sys
    print("\n")
    print("=" * 50)
    print("Wii Save FNV-1a Checksum Tool")
    
    if len(sys.argv) > 1:
        #file as arg
        verify_and_fix_checksum(sys.argv[1])
    else:
        
        print("=" * 50)
        print("\nUsage: python3 checksum_calc.py <savefile.bin>\n")
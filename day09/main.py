

def part1(filename):
    checksum = 0
    with open(filename) as fp:
        line = fp.read().strip()

        id = 0
        rear_id = len(line) // 2
        rear_counter = 0
        position = 0

        i,j = 0, len(line)-1
        while id < rear_id:
            block_size = int(line[i])
            if i % 2 == 0: #file
                for n in range(block_size):
                    checksum += position * id
                    position += 1
                id += 1
            else: #free space
                for n in range(block_size):
                    file_size = int(line[j])
                    if rear_counter >= file_size:
                        # move to the next file
                        rear_id -= 1
                        j -= 2
                        rear_counter = 0
                    checksum += position * rear_id
                    position += 1
                    rear_counter += 1
            i += 1
        
        # still gotta check and finish moving the last file
        last_file_size = int(line[j])
        while rear_counter < last_file_size:
            if i % 2 == 0: # file, ignore
                pass
            else: #free space
                for n in range(int(line[i])):
                    if rear_counter >= last_file_size:
                        # finished with the last file
                        break
                    checksum += position * rear_id
                    position += 1
                    rear_counter += 1
            i += 1
    print(checksum)

def part2(filename):
    checksum = 0
    with open(filename) as fp:
        line = fp.read().strip()

        id = 0
        last_id = len(line) // 2
        position = 0
        fs_counter = 0

        processed_files = set()

        i = 0
        while len(processed_files) <= last_id:
            block_size = int(line[i])
            if i % 2 == 0: #file
                if id in processed_files:
                    # file has been moved
                    position += block_size
                else:
                    for n in range(block_size):
                        checksum += position * id
                        position += 1
                    processed_files.add(id)
                id += 1
            else: #free space
                fs_counter = 0
                for j in range(len(line)-1, i, -2):
                    file_id = j//2
                    file_size = int(line[j])
                    if file_size > (block_size - fs_counter):
                        continue
                    if file_id in processed_files:
                        continue

                    # file fits, move it
                    for n in range(file_size):
                        checksum += position * file_id
                        position += 1
                        fs_counter += 1
                    processed_files.add(file_id)
                    if fs_counter >= block_size:
                        # the free space has been filled
                        break
                if fs_counter < block_size:
                    position += (block_size - fs_counter)
            i += 1
    print(checksum)


if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    part1(filename)
    part2(filename)

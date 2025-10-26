class MBRPartition:
    def __init__(self, boot_indicator:str, starting_chs:dict(), partition_type:str, ending_chs:str, s_sector_LBA:int, n_sectors:int):
        self.boot_indicator = boot_indicator
        self.starting_chs = starting_chs
        self.partition_type = partition_type
        self.ending_chs = ending_chs
        self.s_sector_LBA = s_sector_LBA
        self.n_sectors = n_sectors

    def __str__(self) -> str:
        return f"""
    Boot indicator: {self.boot_indicator}
    Starting CHS: {self.starting_chs}
    Partition type: {self.partition_type}
    Ending CHS: {self.ending_chs}
    Starting sector LBA: {self.s_sector_LBA}
    Number of sectors: {self.n_sectors}\n"""

class MBRParser:
    """
    MBR primary partitions.
    This class is not able
    to recognize extended partitions.
    """
    partition_tables_offset = 446
    def __init__(self, mbr:str):
        # MBR in hexadecimal
        # MBR is 512 bytes long
        try:
            self.mbr = [hex(i).replace("0x", "").zfill(2) for i in bytes.fromhex(mbr)]
        except ValueError:
            print("MBR needs to be a hexadecimal value")

        if len(self.mbr) != 512:
            raise ValueError("Length of MBR needs to be equal to 512")

        self.first_partition = self.partitionsParser()
        self.second_partition = self.partitionsParser(offset=16)
        self.third_partition = self.partitionsParser(offset=32)
        self.fourth_partition = self.partitionsParser(offset=48)

    def __str__(self) -> str:
        return f"""
Partition 1: {self.first_partition}
Partition 2: {self.second_partition}
Partition 3: {self.third_partition}
Partition 4: {self.fourth_partition}"""

    def fromLittleEndian(self, little_endian:str) -> str:
        little_endian = little_endian.zfill(8)
        return "".join([little_endian[i:i+2] for i in range(len(little_endian) -2, -1, -2)])

    def partitionsParser(self, offset=0) -> MBRPartition:
        offset = self.partition_tables_offset + offset
        boot_indicator = f"0x{self.mbr[offset]}"
        starting_chs = {
            "s_head": int(self.mbr[1+offset], 16),
            "s_sector": int(self.mbr[2+offset], 16) & 0x3F,
            "s_cylinder": ((int(self.mbr[2+offset], 16) & 0xC0) << 2) | int(self.mbr[3+offset], 16)
        }
        partition_type = f"0x{self.mbr[4+offset]}"
        ending_chs = {
            "e_head": int(self.mbr[5+offset], 16),
            "e_sector": int(self.mbr[6+offset], 16) & 0x3F,
            "e_cylinder": ((int(self.mbr[6+offset], 16) & 0xC0) << 2) | int(self.mbr[7+offset], 16)
        }
        s_sector_LBA = int(self.fromLittleEndian("".join(self.mbr[8+offset:12+offset])), 16)
        n_sectors = int(self.fromLittleEndian("".join(self.mbr[12+offset:16+offset])), 16) if starting_chs["s_sector"] != 0 and \
                ending_chs["e_sector"] != 0 else 0
        return MBRPartition(boot_indicator, starting_chs, partition_type, ending_chs, s_sector_LBA, n_sectors)

if __name__ == "__main__":
    mbr_parser = MBRParser(input("Insert MBR: "))
    print(mbr_parser)

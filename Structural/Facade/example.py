# Complex parts
class CPU:
    def freeze(self):
        print("FREEZE")

    def jump(self, position):
        print("Jump to {}".format(position))

    def execute(self):
        print("EXECUTE")


class Memory:
    def load(self, position, data):
        print("Load {} from {}".format(data, position))


class HardDrive:
    def read(self, lba, size):
        print("Read {} {}".format(size, lba))


# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(10)
        self.cpu.execute()


# Client
if __name__ == '__main__':
    facade = Computer()
    facade.start_computer()

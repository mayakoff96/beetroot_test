CHANNELS = ['BBC', 'Discovery', 'TV1000']


class TVController:

    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.channel_list[self.current_channel_index]

    def last_channel(self):
        self.current_channel_index = len(self.channel_list) - 1
        return self.channel_list[self.current_channel_index]

    def turn_channel(self, n):
        self.current_channel_index = (self.current_channel_index + n) % len(self.channel_list)
        return self.channel_list[self.current_channel_index]

    def next_channel(self):
        return self.turn_channel(1)

    def previous_channel(self):
        return self.turn_channel(-1)

    def current_chanel(self):
        return self.channel_list[self.current_channel_index]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return "Yes" if channel in range(1, len(self.channel_list) + 1) else "No"
        else:
            return "Yes" if channel in self.channel_list else "No"


controller = TVController(CHANNELS)
var1 = controller.first_channel()
var2 = controller.last_channel()
var3 = controller.turn_channel(1)
var4 = controller.next_channel()
var5 = controller.previous_channel()
var6 = controller.current_chanel()
var7 = controller.is_exist(4)
var8 = controller.is_exist('BBC')


print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
print(var7)
print(var8)
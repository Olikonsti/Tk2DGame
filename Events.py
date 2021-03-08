event_queue = []

def clear_events():
    event_copy = event_queue.copy()
    for i in event_copy:
        event_queue.remove(i)


class QEvent():
    def __init__(self, tag, game, ticks, cmd):
        self.cmd = cmd
        self.tag = tag
        self.in_ticks = ticks
        self.game = game
        self.start_tick = game.ticks

        in_l = False
        for i in event_queue:
            if i.tag == self.tag:
                in_l = True

        if not in_l:
            event_queue.append(self)

    def update(self):
        if self.game.ticks == self.start_tick + self.in_ticks:
            self.run()

    def run(self):
        self.cmd()
        event_queue.remove(self)
        del self
# spec999.py by x0rnn, put players with 999 ping to spectator mode
# line 7 is now idented properly

import minqlx

class spec999(minqlx.Plugin):
    def __init__(self):
        self.add_command("spec999", self.cmd_spec999, 1)

    def cmd_spec999(self, player, msg, channel):
        for p in self.players():
            if p.ping >= 990:
                if p.team != "spectator":
                    p.put("spectator")
                    self.msg("spec999: Moving {} to spectators.".format(p.clean_name))

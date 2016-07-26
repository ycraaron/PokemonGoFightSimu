import utils


class Pokemon(object):

    def __init__(self, base_at, base_def, base_sta, multi):
        self.base_attack = base_at
        self.base_def = base_def
        self.base_sta = base_sta
        self.multi = multi
        self.att = self.base_attack * self.multi
        self.defense = self.base_def * self.multi
        self.hp = self.basesta * self.multi

    def dec_hp(self, damage):
        self.hp -= damage
        return self.is_dead()

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False
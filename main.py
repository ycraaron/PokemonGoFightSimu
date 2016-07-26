from __future__ import division

import Pokemon
import utils
import time


class Main(object):

    def __init__(self):
        self.name = "battle"

    def core(self):
        cp_mul = utils.list_cp_multi
        print cp_mul[39]
        poke_1_att = 186*cp_mul[39]
        poke_1_def = 152*cp_mul[39]
        poke_1_sta = 110*cp_mul[39]

        poke_2_att = 186*cp_mul[39]
        poke_2_def = 168*cp_mul[39]
        poke_2_sta = 260*cp_mul[39]

        poke_1 = Pokemon.Pokemon(poke_1_att, poke_1_def, poke_1_sta, cp_mul[39])
        poke_2 = Pokemon.Pokemon(poke_2_att, poke_2_def, poke_2_sta, cp_mul[39])

        time_elapsed = 0

        att_count_1=0
        att_count_2=0

        poke1_cd = 0.5
        poke2_cd = 0.57

        start_poke1 = start_poke2= time.clock()

        damage_12 = self.cal_damage(40, poke_1_att, poke_2_def, 15*1.25)

        damage_21 = self.cal_damage(40, poke_2_att, poke_1_def, 10*1.25)
        print "a -> va", damage_12, " va -> a", damage_21
        print "a die after times:", poke_1.get_hp()/damage_21
        print "va die after times:", poke_2.get_hp()/damage_12
        # while True:
        #     end_poke =
        #     if poke_1.is_dead() or poke_2.is_dead():
        #         print "Battle end"
        #         if poke_1.is_dead():
        #             print "poke1 win"
        #         else:
        #             print "poke2 win"
        #         break
        #     else:
        #         if

    def cal_damage(self, level, attack, defense, move_power):
        #damage = 0
        damage = (2 * level + 4) / 100 * (attack / defense) * move_power + 0.25
        #print level, attack, defense, move_power
        #print ((2 * level + 4) / 100) * (attack / defense) * move_power
        #print damage
        #Base Damage = (2 * Level + 4) / 100 * (Attacker's_Attack / Defender's_Defense) *Move_Power + 0.25
        return damage;

run = Main()
run.core()


import pygame as pg
import os.path as op
import json
from data import *
import data as da
import objects as ob
import random as ra


def importLevel(path):
	level = json.load(open(op.join("data/json/", path)))
	for o in level:
		# get pos
		def pos(call):
			if len(o["pos"]["pos"]) == 2:
				if o["pos"]["grid"]:
					call(vec(o["pos"]["pos"][0], o["pos"]["pos"][1]) * 48)
				else:
					call(vec(o["pos"]["pos"]))
			elif len(o["pos"]["pos"]) == 4:
				for x in range(o["pos"]["pos"][0], o["pos"]["pos"][2]+1):
					for y in range(o["pos"]["pos"][1], o["pos"]["pos"][3]+1):
						if o["pos"]["grid"]:
							call(vec(x, y) * 48)
						else:
							call(vec(x, y))
			else:
				call(vec(0))
					
		# player
		if o["type"] == "player":
			pos(lambda pos : ob.Player(pos))
			if o["main"]: da.currentPlayer = groups["all"].sprites()[-1]

		# jelly
		elif o["type"] == "jelly":
			pos(lambda pos : ob.Jelly(pos))

		# ground
		elif o["type"] == "ground":
			def create(pos):
				if o["sprite"] == "random":
					ob.NoLogic(pos, groups["all", "ground"], animations["ground-"+str(ra.randint(1, 6))])
				elif 1 <= int(o["sprite"]) <= 5:
					ob.NoLogic(pos, groups["all", "ground"], animations["ground-"+int(o["sprite"])])
				else:
					ob.NoLogic(pos, groups["all", "ground"], animations["ground-1"])
					
			pos(create)
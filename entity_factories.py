#!/usr/bin/env python3

from entity import Entity;

player = Entity(char="@", color=(255, 0, 255), name="Player", blocks_movement=True);

rabbit = Entity(char="b", color=(255, 20, 20), name="Rabbit Marauder", blocks_movement=True);
dog = Entity(char="d", color=(255, 150, 255), name="Dog", blocks_movement=True);

from typing import Set, Iterable, Any;

from tcod.context import Context;
from tcod.console import Console;
from tcod.map import compute_fov;

from actions import EscapeAction, MovementAction;
from entity import Entity;
from game_map import GameMap;
from input_handlers import EventHandler;

import random;

class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.event_handler = event_handler;
        self.game_map = game_map;
        self.player = player;
        self.update_fov();

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            if self.game_map.visible[entity.x, entity.y]:
                if random.random() > 0.5:
                    print('\033[96m' + f"[E] The {entity.name} does not move. It seems to be annoyed by your presence.");
                else:
                    print('\033[96m' + f"[E] The {entity.name} stares into the dark expanse of the Dungeon. It takes no notice of you.");

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event);

            if action is None:
                continue;

            action.perform(self, self.player);
            self.handle_enemy_turns();
            self.update_fov();

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console);
        context.present(console);

        console.clear();

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov (
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        self.game_map.explored |= self.game_map.visible;

from __future__ import annotations;

from typing import TYPE_CHECKING;

if TYPE_CHECKING:
    from engine import Engine;
    from entity import Entity;

class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError;

class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit();

class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__();

        self.dx = dx;
        self.dy = dy;

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError;

class MeleeAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx;
        dest_y = entity.y + self.dy;
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y);
        if not target:
            return;

        print('\033[92m' + f"[P] You bump into the {target.name}. It seems displeased, but it does not retaliate.");

class BumpAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx;
        dest_y = entity.y + self.dy;

        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine, entity);
        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity);

class MovementAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx;
        dest_y = entity.y + self.dy;

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return;
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return;
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return;

        entity.move(self.dx, self.dy);

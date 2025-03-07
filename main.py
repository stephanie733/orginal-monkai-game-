@namespace
class SpriteKind:
    banana = SpriteKind.create()

def on_a_pressed():
    if the_monkai.vy == 0:
        the_monkai.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    animation.run_image_animation(the_monkai,
        [img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        f f . c d b e e d d c d d d d c 
                        f e f . c f e e d d d c c c c c 
                        f e f . . f f e e d d d d d f . 
                        f e f . f e e e e f f f f f . . 
                        f e f f e e e e e e e f . . . . 
                        . f f e e e e f e f f e f . . . 
                        . . f e e e e f e f f e f . . . 
                        . . . f e f f b d f b d f . . . 
                        . . . f d b b d d c d d f . . . 
                        . . . f f f f f f f f f . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . . f e e d f d d f d c . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        f f . c d b e e e d d c c c c c 
                        f e f . c f f e e e d d d d f . 
                        f e f . f e e e e f f f f f f . 
                        f e f f e e e e e e e f f f f . 
                        . f f e e e e f e f d d f d d f 
                        . . f e e e e f e f b d f b d f 
                        . . f e f f f f f f f f f f f f 
                        . . f d d c f . . . . . . . . . 
                        . . f f f f . . . . . . . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . f f e e e d d d d f . . 
                        . . . f d d e e d d d d d d c . 
                        . . . c d b e e d f d d f d c . 
                        f f . c d b e e d f d d f d d c 
                        f e f . c f e e d d d d e e d c 
                        f e f . . f e e e d c d d d d c 
                        f e f . . f f e e e d c c c f . 
                        f e f . f e e e e f f f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f e e e e f e e f e f f . . 
                        . . f e e e f f f e e f f e f . 
                        . f b f f f f f f c d d b d d f 
                        . f d d c f . . f d d d c d d f 
                        . . f f f . . . f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . f f f e e e e e f . . . 
                        . . . f d d e e e e d d d f . . 
                        . . . c d b e e e d d d d d c . 
                        . . . c d b e e d d d d d d c . 
                        . f f . c f e e d f d d f d d c 
                        f e f . . f e e d f d d f d d c 
                        f e f . . f e e d d d d e e d c 
                        f e f . . f f e e d c d d d f . 
                        f e f . f e e e e e d f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f f b e e e e e f f . . . . 
                        . . f f d d c e e f f e f . . . 
                        . . . . f f f c d d b d d f . . 
                        . . . . . f f d d d c d d f . . 
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . . c f e e e d d c c c c c 
                        . . . . . f f e e e d d d d f . 
                        . . . . f e e e e f f f f f . . 
                        f f . f e e e e e e f f . . . . 
                        f e . f e e f e e f e e f . . . 
                        f e . f e e e f e e f e e f . . 
                        f e f f e f b b f b d f d b f . 
                        f f f f e b d d f d d f d d f . 
                        . f f f f f f f f f f f f f . .
            """)],
        100,
        False)
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_left_pressed():
    animation.run_image_animation(the_monkai,
        [img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . f f 
                        c c c c c d d d e e f c . f e f 
                        . f d d d d d e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f e f 
                        . . . f e f f e f e e e e f f . 
                        . . . f e f f e f e e e e f . . 
                        . . . f d b f d b f f e f . . . 
                        . . . f d d c d d b b d f . . . 
                        . . . . f f f f f f f f f . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        c d e e d d d d e e d d f . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e b d c . f f 
                        . f d d d d e e e f f c . f e f 
                        . f f f f f f e e e e f . f e f 
                        . f f f f e e e e e e e f f e f 
                        f d d f d d f e f e e e e f f . 
                        f d b f d b f e f e e e e f . . 
                        f f f f f f f f f f f f e f . . 
                        . . . . . . . . . f c d d f . . 
                        . . . . . . . . . . f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f f . . . . 
                        . c d d d d d d e e d d f . . . 
                        . c d f d d f d e e b d c . . . 
                        c d d f d d f d e e b d c . f f 
                        c d e e d d d d e e f c . f e f 
                        c d d d d c d e e e f . . f e f 
                        . f c c c d e e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . f f e f e e f e e e e f . . 
                        . f e f f e e f f f e e e f . . 
                        f d d b d d c f f f f f f b f . 
                        f d d c d d d f . . f c d d f . 
                        . f f f f f f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f f f . . . . 
                        . . f d d d e e e e d d f . . . 
                        . c d d d d d e e e b d c . . . 
                        . c d d d d d d e e b d c . . . 
                        c d d f d d f d e e f c . f f . 
                        c d d f d d f d e e f . . f e f 
                        c d e e d d d d e e f . . f e f 
                        . f d d d c d e e f f . . f e f 
                        . . f f f d e e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . . . f f e e e e e b f f . . 
                        . . . f e f f e e c d d f f . . 
                        . . f d d b d d c f f f . . . . 
                        . . f d d c d d d f f . . . . . 
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e f c . . . . 
                        . f d d d d e e e f f . . . . . 
                        . . f f f f f e e e e f . . . . 
                        . . . . f f e e e e e e f . f f 
                        . . . f e e f e e f e e f . e f 
                        . . f e e f e e f e e e f . e f 
                        . f b d f d b f b b f e f f e f 
                        . f d d f d d f d d b e f f f f 
                        . . f f f f f f f f f f f f f .
            """)],
        100,
        False)
    the_monkai.vy = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite2, location2):
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles4,
    on_overlap_tile2)

def on_right_pressed():
    animation.run_image_animation(the_monkai,
        [img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        f f . c d b e e d d c d d d d c 
                        f e f . c f e e d d d c c c c c 
                        f e f . . f f e e d d d d d f . 
                        f e f . f e e e e f f f f f . . 
                        f e f f e e e e e e e f . . . . 
                        . f f e e e e f e f f e f . . . 
                        . . f e e e e f e f f e f . . . 
                        . . . f e f f b d f b d f . . . 
                        . . . f d b b d d c d d f . . . 
                        . . . f f f f f f f f f . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . . f e e d f d d f d c . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        f f . c d b e e e d d c c c c c 
                        f e f . c f f e e e d d d d f . 
                        f e f . f e e e e f f f f f f . 
                        f e f f e e e e e e e f f f f . 
                        . f f e e e e f e f d d f d d f 
                        . . f e e e e f e f b d f b d f 
                        . . f e f f f f f f f f f f f f 
                        . . f d d c f . . . . . . . . . 
                        . . f f f f . . . . . . . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . f f e e e d d d d f . . 
                        . . . f d d e e d d d d d d c . 
                        . . . c d b e e d f d d f d c . 
                        f f . c d b e e d f d d f d d c 
                        f e f . c f e e d d d d e e d c 
                        f e f . . f e e e d c d d d d c 
                        f e f . . f f e e e d c c c f . 
                        f e f . f e e e e f f f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f e e e e f e e f e f f . . 
                        . . f e e e f f f e e f f e f . 
                        . f b f f f f f f c d d b d d f 
                        . f d d c f . . f d d d c d d f 
                        . . f f f . . . f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . f f f e e e e e f . . . 
                        . . . f d d e e e e d d d f . . 
                        . . . c d b e e e d d d d d c . 
                        . . . c d b e e d d d d d d c . 
                        . f f . c f e e d f d d f d d c 
                        f e f . . f e e d f d d f d d c 
                        f e f . . f e e d d d d e e d c 
                        f e f . . f f e e d c d d d f . 
                        f e f . f e e e e e d f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f f b e e e e e f f . . . . 
                        . . f f d d c e e f f e f . . . 
                        . . . . f f f c d d b d d f . . 
                        . . . . . f f d d d c d d f . . 
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . . c f e e e d d c c c c c 
                        . . . . . f f e e e d d d d f . 
                        . . . . f e e e e f f f f f . . 
                        f f . f e e e e e e f f . . . . 
                        f e . f e e f e e f e e f . . . 
                        f e . f e e e f e e f e e f . . 
                        f e f f e f b b f b d f d b f . 
                        f f f f e b d d f d d f d d f . 
                        . f f f f f f f f f f f f f . .
            """)],
        100,
        False)
    the_monkai.vy = 0
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_left_repeated():
    animation.run_image_animation(the_monkai,
        [img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . f f 
                        c c c c c d d d e e f c . f e f 
                        . f d d d d d e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f e f 
                        . . . f e f f e f e e e e f f . 
                        . . . f e f f e f e e e e f . . 
                        . . . f d b f d b f f e f . . . 
                        . . . f d d c d d b b d f . . . 
                        . . . . f f f f f f f f f . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        c d e e d d d d e e d d f . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e b d c . f f 
                        . f d d d d e e e f f c . f e f 
                        . f f f f f f e e e e f . f e f 
                        . f f f f e e e e e e e f f e f 
                        f d d f d d f e f e e e e f f . 
                        f d b f d b f e f e e e e f . . 
                        f f f f f f f f f f f f e f . . 
                        . . . . . . . . . f c d d f . . 
                        . . . . . . . . . . f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f f . . . . 
                        . c d d d d d d e e d d f . . . 
                        . c d f d d f d e e b d c . . . 
                        c d d f d d f d e e b d c . f f 
                        c d e e d d d d e e f c . f e f 
                        c d d d d c d e e e f . . f e f 
                        . f c c c d e e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . f f e f e e f e e e e f . . 
                        . f e f f e e f f f e e e f . . 
                        f d d b d d c f f f f f f b f . 
                        f d d c d d d f . . f c d d f . 
                        . f f f f f f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f f f . . . . 
                        . . f d d d e e e e d d f . . . 
                        . c d d d d d e e e b d c . . . 
                        . c d d d d d d e e b d c . . . 
                        c d d f d d f d e e f c . f f . 
                        c d d f d d f d e e f . . f e f 
                        c d e e d d d d e e f . . f e f 
                        . f d d d c d e e f f . . f e f 
                        . . f f f d e e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . . . f f e e e e e b f f . . 
                        . . . f e f f e e c d d f f . . 
                        . . f d d b d d c f f f . . . . 
                        . . f d d c d d d f f . . . . . 
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e f c . . . . 
                        . f d d d d e e e f f . . . . . 
                        . . f f f f f e e e e f . . . . 
                        . . . . f f e e e e e e f . f f 
                        . . . f e e f e e f e e f . e f 
                        . . f e e f e e f e e e f . e f 
                        . f b d f d b f b b f e f f e f 
                        . f d d f d d f d d b e f f f f 
                        . . f f f f f f f f f f f f f .
            """)],
        100,
        False)
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

banana12: Sprite = None
the_monkai: Sprite = None
the_monkai = sprites.create(img("""
        . . . . . . . f f f f f . . . . 
            . . . . . . f e e e e e f . . . 
            . . . . . f e e e d d d d f . . 
            . . . . f f e e d f d d f d c . 
            . . . f d d e e d f d d f d c . 
            . . . c d b e e d d d d e e d c 
            f f . c d b e e d d c d d d d c 
            f e f . c f e e d d d c c c c c 
            f e f . . f f e e d d d d d f . 
            f e f . f e e e e f f f f f . . 
            f e f f e e e e e e e f . . . . 
            . f f e e e e f e f f e f . . . 
            . . f e e e e f e f f e f . . . 
            . . . f e f f b d f b d f . . . 
            . . . f d b b d d c d d f . . . 
            . . . f f f f f f f f f . . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
scene.set_background_image(img("""
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7776677777777767777777777777777777777777777667777777776777777777777777777777777777766777777777677777777777777777777777777776677777777767777777777777777777777777
        7666777777777667777777777777777777777767766677777777766777777777777777777777776776667777777776677777777777777777777777677666777777777667777777777777777777777767
        7767766777667766777766777777777777777766776776677766776677776677777777777777776677677667776677667777667777777777777777667767766777667766777766777777777777777766
        6666667767766766776766777777777777776676666666776776676677676677777777777777667666666677677667667767667777777777777766766666667767766766776766777777777777776676
        6666677766766666766667777777777777666677666667776676666676666777777777777766667766666777667666667666677777777777776666776666677766766666766667777777777777666677
        6666676666666676666677767777776667776667666667666666667666667776777777666777666766666766666666766666777677777766677766676666676666666676666677767777776667776667
        6666666666666776677666667766677766777666666666666666677667766666776667776677766666666666666667766776666677666777667776666666666666666776677666667766677766777666
        6666666666666766667766677677667766666666666666666666676666776667767766776666666666666666666667666677666776776677666666666666666666666766667766677677667766666666
        66b666666666666666666667667776676666666666b666666666666666666667667776676666666666b666666666666666666667667776676666666666b6666666666666666666676677766766666666
        66b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b67766666666666
        66b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb6766666666666
        66b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb666666666666
        66b66666699dbb666666dd9666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb666666666666
        6bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb666666666666
        6bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb66666666666
        6bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb66666666666
        bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666
        bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666
        bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666
        bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966
        bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996
        bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999
        bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999
        bb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999b
        bb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999b
        bb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999b
        b9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99b
        b9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99b
        b9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bb
        b9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbb
        dd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbb
        9d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb9
        9d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb99
        9d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb999
        9dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd99
        99dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd99
        99ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd9
        9999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d9
        9999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d9
        999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd
        d9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999d
        dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999
        dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
        9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
        ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999
        dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
        dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999
        d99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999d
        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
        d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
        999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
        999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9
        9999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd9
        d999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbdddddddd
        ddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbddddddd
        dddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddd
        ddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbddddddd
        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
        ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
        dddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
        ddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbddddd
        dddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddd
        ddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777dddd
        dddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dd
        ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
scene.camera_follow_sprite(the_monkai)
the_monkai.set_velocity(10, 100)
the_monkai.ay = 500
controller.move_sprite(the_monkai, 100, 0)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile0
""")):
    banana12 = sprites.create(assets.image("""
        myImage
    """), SpriteKind.food)
    tiles.place_on_tile(banana12, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
game.set_dialog_frame(img("""
    8888.....88....888....888...8888.
        867788..8768..86768..8678.887768.
        8767768.877788676768877788677678.
        87767768676778776778776786776778.
        .877876667767877677876778678778..
        .867786686766867676866766687768..
        ..8666868867688686886768686668...
        .88866688888888888888888866688...
        8777768866666666666666668886688..
        86767768666666666666666688677778.
        .8776678666666666666666686776768.
        ..87766866666666666666668766778..
        ..8888886666666666666666866778...
        .86776886666666666666666888888...
        8677776866666666666666668867768..
        87666688666666666666666686777768.
        86777768666666666666666688666678.
        .8677688666666666666666686777768.
        ..88888866666666666666668867768..
        ..8776686666666666666666888888...
        .87766786666666666666666866778...
        8676776866666666666666668766778..
        87777688666666666666666686776768.
        .8866888666666666666666688677778.
        ..88666888888888888888888666888..
        ..8666868676886868867688686668...
        .867786667668676768667686687768..
        .877876877678776778767766678778..
        87767768767787767787767686776778.
        876776887778867676887778.8677678.
        867788.8768..86768..8678..887768.
        8888...888....888....88.....8888.
        .................................
"""))
game.show_long_text("This is george", DialogLayout.BOTTOM)
game.show_long_text("Help him get all the bananas", DialogLayout.BOTTOM)
info.set_score(0)
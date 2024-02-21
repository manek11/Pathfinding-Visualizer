from domain.enums.box_type import BoxType

SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720
ROWS = 32
COLS = 18
BOX_HEIGHT = SCREEN_HEIGHT // ROWS 
BOX_WIDTH = SCREEN_WIDTH // COLS

BOX_TYPE_TO_COLOR = {
    BoxType.UNSET : "steelblue1",
    BoxType.SOURCE : "saddlebrown",
    BoxType.DESTINATION : "red",
    BoxType.WALL : "seashell4", 
    BoxType.VISITED : "yellow",
}
size = 400 # Board size
gridLen = 4 # No. of rows x colomn
gridPadding = 10 # space between cells

backgroundColorGame = "#92877d" # Board Background Color
BackgroundColorCell = "#9e948a" # Cell color if in case 0 is present to denote empty

# Cell background color otherwise
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e",
4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179", 32768: "#f59563", 65536: "#f67c5f", }

# Text color
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2",
4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65", 32768: "#776e65", 65536: "#f9f6f2", }

FONT=("Verdana", 40, "bold")
KEY_UP = "'u'"
KEY_DOWN = "'d'"
KEY_LEFT = "'l'"
KEY_RIGHT = "'r'"
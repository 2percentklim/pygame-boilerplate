# Scene Layout

Scenes render to a fixed 640 x 360 logical canvas. The optional `--grid` overlay
divides it into 32 x 32 pixel cells, labeled like a chessboard: columns `A` through
`T` run left to right and rows `1` through `11` run top to bottom.

The canvas includes a 4-pixel margin above and below the grid. Cell `A1` begins at
`(0, 4)`. A cell's center is 16 pixels from its left edge and 16 pixels from its top
edge. For a zero-based column and row, calculate the center as:

```python
cell_center_x = column * GRID_SIZE + GRID_SIZE // 2
cell_center_y = 4 + row * GRID_SIZE + GRID_SIZE // 2
```

For example, `I6` begins at `(256, 164)` and its center is `(272, 180)`.

## Centering Objects

Set a `pygame.Rect` or rendered surface's `center` to the center of one cell, or to
the midpoint of the cell group it should occupy. When an object spans an even number
of cells, its center lies on the shared gridline between the two middle cells.

```python
# A 100 x 25 button centered across I6 through L6.
new_game_button = pygame.Rect((0, 0), (100, 25))
new_game_button.center = (320, 180)

# A button centered on the J/K gridline in row 8.
settings_button = pygame.Rect((0, 0), (100, 25))
settings_button.center = (320, 244)
```

The start menu uses these placements:

| Object     | Grid alignment                        | Logical center |
| ---------- | ------------------------------------- | -------------- |
| Game title | Horizontally centered; row 4          | `(320, 116)`   |
| New Game   | Centered across I6-L6                 | `(320, 180)`   |
| Load Game  | Centered across I7-L7                 | `(320, 212)`   |
| Settings   | Centered on the J/K gridline in row 8 | `(320, 244)`   |

## Tiles and Scene Objects

Tiles should use the standard `32 x 32` size and be placed at their cell's upper-left
corner. Convert a zero-based map column and row to pixels with:

```python
tile_x = column * GRID_SIZE
tile_y = 4 + row * GRID_SIZE
canvas.blit(tile_surface, (tile_x, tile_y))
```

For objects larger than one tile, define their size as a multiple of `GRID_SIZE` and
place their `topleft` on gridlines. Use `rect.center` for buttons, labels, sprites,
or other objects intended to balance around a cell or a group of cells.

Run `py main.py --grid` while creating layouts to verify placement. The grid is a
debug overlay and is not shown in a normal run.

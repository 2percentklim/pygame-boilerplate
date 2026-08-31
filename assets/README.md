# Artwork Assets

The game renders scenes at a fixed logical canvas of 640 x 360 pixels (16:9).
The default window is 1280 x 720. It scales the canvas to the largest size that
preserves its aspect ratio, using nearest-neighbor filtering. This avoids stretching
and leaves black bars only when the active window or fullscreen display is not 16:9.
Create pixel art at its intended logical size. Whole-number display scales produce
the most even pixel sizes; other scales remain sharp but can vary individual pixel
widths slightly.

## File Types

| Asset | Recommended format | Notes |
| --- | --- | --- |
| Game art, UI, sprites, tiles | PNG | Use RGBA PNGs whenever transparency is needed. |
| Large opaque backgrounds | JPG or PNG | Use JPG for photographic or painted backgrounds without transparency; use PNG for sharp edges or alpha. |
| Window and installer icon | ICO and PNG | Use `Boilerplate-Icon-256.ico` for Windows packaging and `Boilerplate-Icon-256.png` for the Pygame window. |
| Fonts | TTF or OTF | Put font files in `fonts/`. |
| Audio | OGG or WAV | Prefer OGG for longer music and WAV for short sound effects. |

Do not use GIF for gameplay animation. Export animation as numbered PNG frames or
a PNG sprite sheet instead. WebP is suitable for opaque static artwork when file
size matters, but PNG is the default because it is predictable across Pygame tools.

## Recommended Dimensions

| Asset | Design size | Notes |
| --- | --- | --- |
| Application icon | 32 x 32 PNG; multi-resolution ICO | Include 16, 32, 48, and 256px images in the ICO. |
| Toolbar or action icon | 24 x 24 or 32 x 32 | Use 32px when it needs to read clearly at a distance. |
| Menu button icon | 48 x 48 or 64 x 64 | Leave transparent padding around the artwork. |
| Small item or status icon | 32 x 32 or 48 x 48 | Keep a consistent visual box across the set. |
| Character sprite | 32 x 32 or 32 x 48 per frame | Default player and NPC scale. Keep every animation frame on the same grid. |
| NPC, enemy, or prop sprite | 32 x 32 per frame | Standard world-object size; use 32 x 48 or 32 x 64 for taller subjects. |
| Large character, vehicle, or boss | 64 x 64 per frame | Use when the subject needs additional silhouette or animation detail. |
| Sprite sheet | Frame size times columns and rows | Example: eight 32 x 32 frames in four columns is 128 x 64. |
| Terrain tile | 32 x 32 | Standard world grid. Make square, seamlessly tileable PNGs; do not mix tile sizes in one map. |
| UI panel or dialog art | Build from 9-slice pieces | Use corners and repeatable edges rather than one large fixed-size panel. |
| Background layer | 640 x 360 | Match the logical canvas for a full-screen, non-scrolling background. |
| Scrolling/parallax layer | At least 640px wide | Make it wider than the logical viewport when it must scroll horizontally. |
| Splash or title artwork | 640 x 360 or 640 x 160 | Keep important details away from the outer 5% of the image. |

Use 32px as the default world grid. A 64 x 64 sprite can sit over that grid for
large subjects, while 16 x 16 is appropriate for small item or status icons.
"32-bit" describes color depth; describe asset dimensions as 32 x 32 or 64 x 64
pixels. Keep outlines, animation frames, and tiles aligned to the selected grid.
For painted or high-resolution art, retain a separate source file outside the
shipped asset folder.

## Organization

Add asset groups as the game grows:

```text
assets/
  backgrounds/
  fonts/
  icons/
  sprites/
    characters/
    enemies/
    props/
  tiles/
  ui/
  audio/
```

Use lowercase, descriptive filenames with hyphens, such as
`player-idle.png`, `forest-grass-01.png`, and `icon-settings-32.png`. For animation
frames, use zero-padded numbers: `player-run-00.png`, `player-run-01.png`.

## Export Checklist

- Export transparent artwork as 8-bit RGBA PNG.
- Remove unused transparent borders unless the padding is intentional for alignment.
- Keep every frame in a sprite animation the same dimensions and anchor position.
- Check tile edges at 100% zoom before adding them to a map.
- Test scenes at 1280 x 720 and fullscreen; non-16:9 screens can show small black bars to preserve pixel proportions.
- Keep original layered source files separate from runtime-ready artwork.

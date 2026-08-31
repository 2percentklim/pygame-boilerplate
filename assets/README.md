# Artwork Assets

The game is designed at 1200 x 675 pixels (16:9). Create artwork at its intended
design size; scenes scale it to the active window size. Keep pixel art at integer
multiples of its base resolution and avoid scaling it with smoothing.

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
| Character sprite | 64 x 64 or 96 x 96 per frame | Use a larger frame only when the character occupies a substantial screen area. |
| NPC, enemy, or prop sprite | 48 x 48, 64 x 64, or 96 x 96 per frame | Choose one grid size per asset family. |
| Sprite sheet | Frame size times columns and rows | Example: eight 64 x 64 frames in four columns is 256 x 128. |
| Terrain tile | 32 x 32, 48 x 48, or 64 x 64 | Use square, seamlessly tileable PNGs. Do not mix tile sizes in one map. |
| UI panel or dialog art | Build from 9-slice pieces | Use corners and repeatable edges rather than one large fixed-size panel. |
| Background layer | 1200 x 675 | Match the design canvas for a full-screen, non-scrolling background. |
| Scrolling/parallax layer | At least 1200px wide | Make it wider than the viewport when it must scroll horizontally. |
| Splash or title artwork | 1200 x 675 or 1200 x 300 | Keep important details away from the outer 5% of the image. |

For pixel art, select a base unit such as 16px or 32px and keep outlines,
animation frames, and tiles aligned to that grid. For painted or high-resolution
art, use the dimensions above as display targets and retain a separate source file
outside the shipped asset folder.

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
- Keep original layered source files separate from runtime-ready artwork.

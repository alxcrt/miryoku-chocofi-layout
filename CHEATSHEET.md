# Corne cheat sheet

42 keys, Colemak-DH. The Corne layout requires the new firmware; Mac Raycast assignments are saved. Physical Hyper and quick-terminal activation still need testing.

**Select host:** hold **Escape + Q** for Mac or **Escape + W** for Omarchy. Mac is the startup mode; reboot resets the mode.

## Outer keys

| Position | Mac left | Mac right | Omarchy left | Omarchy right |
| --- | --- | --- | --- | --- |
| Top | Quick terminal | Capture menu; hold Clicks | Scratchpad | Capture menu; hold Clicks |
| Middle | Caps Word | Clipboard history | Caps Word | Clipboard manager |
| Bottom | Tap Raycast; hold Hyper | Tap one-shot Hyper; hold Hyper | Tap menu; hold Super | Tap one-shot Super; hold Super |

Mac quick terminal: **Command + backtick (`)**. Linux scratchpad: **Super + backtick**; put a terminal there first with **Super + Shift + backtick**.

Left bottom taps the launcher and holds Hyper/Super. Right bottom taps one-shot Hyper/Super: release it, then press the shortcut within 1.5 seconds. It releases after that target key press, or times out unused; it does not lock. Hold it for an ordinary modifier chord. Left bottom has a 180 ms hold-preferred term; capture/Clicks has the default 200 ms layer-tap.

## Caps Word

Tap the left-middle outer key for uppercase words and identifiers such as `MY_VARIABLE`. Letters, digits, underscores, Backspace and Delete continue it. A space or another separator ends it; tap Caps Word again to turn it off. This is word-by-word capitalization, not a persistent Caps Lock. Browser access remains on Hyper+B (Mac) or System + L.

## Thumb layers

| Tap key; hold for | Layer |
| --- | --- |
| Escape | System |
| Space | Navigate |
| Tab | Mouse |
| Enter | Symbols |
| Backspace | Numbers |
| Delete | F-keys |
| Outer top-right | Clicks |

## Hyper - Mac

**Hyper = left Control + Option/Alt + Shift + Command.** Both bottom outer keys provide it. Z and / type normally. Extra Hyper modifier keys inside utility layers have been removed; their old positions are disabled.

| Hyper + | Opens |
| --- | --- |
| A | ChatGPT |
| C | Claude |
| E | VS Code |
| L | Linear |
| T | Ghostty |
| W | cmux workspaces |
| B | Helium browser |
| V | Clipboard history |
| P | Bitwarden |
| M | IINA |
| O | Omarchy menu |
| K | Shortcut guide |

## System - hold Escape

| Base letter | Mac | Omarchy |
| --- | --- | --- |
| Q / W | Mac / Omarchy | Mac / Omarchy |
| F | Omarchy menu | Omarchy menu |
| P | Fullscreen capture | Record / stop |
| B | Capture menu | Screenshot OCR |
| J | Ghostty | Terminal |
| L | Helium | Browser |
| U | Shortcut guide | Keybindings |
| Y | Area capture | Screenshot |

Hold **Space + Q** for Mission Control on Mac. Hold **Space + W / F** for previous / next Desktop on Mac or workspace on Linux.

## Base typing positions

Read each layer grid using these same positions. Outer utility keys are omitted.

```text
     Q            W            F            P            B        |       J            L            U            Y            '
     A            R            S            T            G        |       M            N            E            I            O
     Z            X            C            D            V        |       K            H            ,            .            /
```

Home-row holds: **A/R/S/T = Cmd/Alt/Ctrl/Shift**; **N/E/I/O = Shift/Ctrl/Alt/Cmd**. On Linux, Cmd means Super.

Ordinary home-row modifiers retain 280 ms tapping term, 175 ms quick-tap and 150 ms prior-idle protection.

## Navigate - Hold Space

```text
  Mission     Prev desk    Next desk        -            -        |      Redo        Paste         Copy         Cut          Undo
    Cmd          Alt          Ctrl        Shift          -        |     Escape        Left         Down          Up         Right
     -            -            -            -            -        |     Insert        Home      Page down     Page up        End
```

Right thumbs: Enter / Backspace / Delete. Linux: W/F = previous/next workspace; Q inactive.

## Mouse - Hold Tab

```text
     -            -            -            -            -        |      Redo        Paste         Copy         Cut          Undo
    Cmd          Alt          Ctrl        Shift          -        |       -        Move left    Move down     Move up     Move right
     -            -            -            -            -        |       -       Scroll left  Scroll down   Scroll up   Scroll right
```

Right thumbs: Right click / Left click / Middle click.

## Numbers - Hold Backspace

```text
     [            7            8            9            ]        |       -            -            -            -            -
     ;            4            5            6            =        |       -          Shift         Ctrl         Alt          Cmd
     `            1            2            3            \        |       -            -            -            -            -
```

Left thumbs: . / 0 / -

## Symbols - Hold Enter

```text
     {            &            *            (            }        |       -            -            -            -            -
     :            $            %            ^            +        |       -          Shift         Ctrl         Alt          Cmd
     ~            !            @            #            |        |       -            -            -            -            -
```

Left thumbs: ( / ) / _

## F-keys - Hold Delete

```text
    F12           F7           F8           F9         SysRq      |       -            -            -            -            -
    F11           F4           F5           F6      Scroll lock   |       -          Shift         Ctrl         Alt          Cmd
    F10           F1           F2           F3         Pause      |       -            -            -            -            -
```

Left thumbs: Context menu / Space / Tab.

Navigate/Mouse clipboard row, right side: **J redo, L paste, U copy, Y cut, apostrophe undo**. Mac uses Command; Omarchy uses its universal Super copy/paste/cut and Control undo/redo.

**Navigate M = Escape; H = Home.** Home now sends the normal keyboard Home key. Outer utility keys pass through on every layer. Empty inner positions are disabled, so they do not fall back to typing letters.

## Clicks - hold outer top-right

- Left thumbs: middle / left / right mouse button.
- Right thumbs: right / left / middle mouse button.
- Left top/bottom rows: Q/W/F/P/B or Z/X/C/D/V = undo/cut/copy/paste/redo.
- Right top/bottom rows: J/L/U/Y/apostrophe or K/H/comma/dot/slash = redo/paste/copy/cut/undo.

## System media and connections - hold Escape

| Base key | Action |
| --- | --- |
| N / O | Previous / next track |
| E / I | Volume down / up |
| Enter / Backspace / Delete thumbs | Play-pause / next track / mute |
| M | Toggle external peripheral power (hardware dependent) |
| K | Toggle USB / Bluetooth output |
| H / comma / dot | Bluetooth profiles 1 / 2 / 3 |
| Slash | Clear the selected Bluetooth profile pairing |

Use the Bluetooth host controls in standalone mode. In dongle mode, the Prospector normally outputs through USB. Clearing a host profile removes that saved host pairing.

## Optional next features (not enabled)

- [Key Repeat](https://zmk.dev/docs/keymaps/behaviors/key-repeat): send the last key again.
- [Sticky layers](https://zmk.dev/docs/keymaps/behaviors/sticky-layer): tap once for one symbol or number, then return to typing.

## Source and refresh

Reference: `config/corne.keymap` and the Mac Raycast assignments documented in `README.md`. Native Omarchy shortcuts require its standard bindings. The Numbers/Symbols/F-keys grids share the same placement on both hosts.

PDF: [Printable cheat sheet](output/pdf/corne-cheatsheet.pdf). Rebuild with `python3 tools/generate_cheatsheet.py` in an environment with ReportLab installed.

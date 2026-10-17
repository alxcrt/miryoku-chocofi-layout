# Corne cheat sheet

42 keys, Colemak-DH. The Corne layout requires the new firmware; Mac Raycast assignments are saved. Physical Hyper and quick-terminal activation still need testing.

**Select host:** hold **Escape + Q** for Mac or **Escape + W** for Omarchy. Mac is the startup mode; reboot resets the mode.

## Outer keys

| Position | Mac left | Mac right | Omarchy left | Omarchy right |
| --- | --- | --- | --- | --- |
| Top | Tap Raycast; hold Hyper | Tap one-shot Hyper; hold Hyper | Tap menu; hold Super | Tap one-shot Super; hold Super |
| Middle | Clipboard history | Helium browser | Clipboard manager | Browser |
| Bottom | Quick terminal | Capture menu; hold Clicks | Scratchpad | Capture menu; hold Clicks |

Mac quick terminal: **Command + backtick (`)**. Linux scratchpad: **Super + backtick**; put a terminal there first with **Super + Shift + backtick**.

Left top taps the launcher and holds Hyper/Super. Right top taps one-shot Hyper/Super: release it, then press the shortcut within 1.5 seconds. It releases after that target key press, or times out unused; it does not lock. Hold it for an ordinary modifier chord. Left top has a 180 ms hold-preferred term; capture/Clicks has the default 200 ms layer-tap.

## Thumb layers

| Tap key; hold for | Layer |
| --- | --- |
| Escape | System |
| Space | Navigate |
| Tab | Mouse |
| Enter | Symbols |
| Backspace | Numbers |
| Delete | F-keys |
| Outer bottom-right | Clicks |

## Hyper - Mac

**Hyper = left Control + Option/Alt + Shift + Command.** Both outer top keys provide it. Z and / type normally.

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
    Cmd          Alt          Ctrl        Shift          -        |     Caps*         Left         Down          Up         Right    
   Hyper          -            -            -            -        |     Insert    Browser home  Page down     Page up        End     
```

Right thumbs: Enter / Backspace / Delete. Linux: W/F = previous/next workspace; Q inactive.

## Mouse - Hold Tab

```text
     -            -            -            -            -        |      Redo        Paste         Copy         Cut          Undo    
    Cmd          Alt          Ctrl        Shift          -        |       -        Move left    Move down     Move up     Move right 
   Hyper          -            -            -            -        |       -       Scroll left  Scroll down   Scroll up   Scroll right
```

Right thumbs: Right click / Left click / Middle click.

## Numbers - Hold Backspace

```text
     [            7            8            9            ]        |       -            -            -            -            -      
     ;            4            5            6            =        |       -          Shift         Ctrl         Alt          Cmd     
     `            1            2            3            \        |       -            -            -            -          Hyper    
```

Left thumbs: . / 0 / -

## Symbols - Hold Enter

```text
     {            &            *            (            }        |       -            -            -            -            -      
     :            $            %            ^            +        |       -          Shift         Ctrl         Alt          Cmd     
     ~            !            @            #            |        |       -            -            -            -          Hyper    
```

Left thumbs: ( / ) / _

## F-keys - Hold Delete

```text
    F12           F7           F8           F9         SysRq      |       -            -            -            -            -      
    F11           F4           F5           F6      Scroll lock   |       -          Shift         Ctrl         Alt          Cmd     
    F10           F1           F2           F3         Pause      |       -            -            -            -          Hyper    
```

Left thumbs: Context menu / Space / Tab.

Navigate/Mouse clipboard row, right side: **J redo, L paste, U copy, Y cut, apostrophe undo**. Mac uses Command; Omarchy uses its universal Super copy/paste/cut and Control undo/redo.

**Caps (asterisk)** sends Caps Lock; your Mac remaps it to Escape. **Browser home** sends the consumer Browser Home action, not a document Home key.

## Clicks - hold outer bottom-right

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

- [Caps Word](https://zmk.dev/docs/keymaps/behaviors/caps-word): uppercase words and identifiers, then leave on a separator.
- [Key Repeat](https://zmk.dev/docs/keymaps/behaviors/key-repeat): send the last key again.
- [Sticky layers](https://zmk.dev/docs/keymaps/behaviors/sticky-layer): tap once for one symbol or number, then return to typing.

## Source and refresh

Reference: `config/corne.keymap` and the Mac Raycast assignments documented in `README.md`. Native Omarchy shortcuts require its standard bindings. The Numbers/Symbols/F-keys grids share the same placement on both hosts.

PDF: [Printable cheat sheet](output/pdf/corne-cheatsheet.pdf). Rebuild with `python3 tools/generate_cheatsheet.py` in an environment with ReportLab installed.

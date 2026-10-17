# Miryoku for 42-key Corne

Colemak-DH, Miryoku-inspired ZMK configuration for Alex's **42-key Corne** with
a 36-key typing core, six outer utility keys, **nice!nano nRF52840 controllers**
and optional nice!view displays. The `dongle`
branch supports a **Prospector USB dongle (XIAO BLE)** and standalone use with
only the two keyboard halves.

![Miryoku Chocofi base layout](assets/layout.png)

[Cheat sheet](CHEATSHEET.md) · [Printable two-page PDF](output/pdf/corne-cheatsheet.pdf)

## Firmware and flashing

Download the `firmware` artifact from a successful GitHub Actions run on `dongle`.
Builds run after a push or through **Actions → Run workflow**.

| Mode | Prospector | Left half | Right half |
| --- | --- | --- | --- |
| Dongle | `corne_dongle prospector_adapter-xiao_ble__zmk-zmk.uf2` | `corne_left_dongle.uf2` | `corne_right.uf2` |
| Standalone, USB or BLE host | Not used | `corne_left_standalone.uf2` | `corne_right.uf2` |

Both halves are BLE peripherals in dongle mode. In standalone mode, the left
half is central and sends input to the host over USB or BLE. The right half
cannot connect directly to a computer.

When **changing modes**, flash the board's `settings_reset` image to every
participating controller, then its appropriate normal firmware. This erases
pairings and output preferences; forget old host pairings and pair again when
using BLE. Pair the left half to a fresh Prospector before the right so its
battery widgets appear in the expected order.

A keymap-only update with the same device roles normally needs no settings reset.
For the Hyper fix, update the **Prospector in dongle mode** or the **left half in
standalone mode**. For the ZMK/configuration upgrade, update all participating
controllers from the same successful build.

See ZMK's [dongle guide](https://zmk.dev/docs/hardware-integration/dongle) and
[pairing reset procedure](https://zmk.dev/docs/troubleshooting/connection-issues#reset-split-keyboard-procedure).

## Mac and Omarchy in one firmware

The same firmware supports **macOS (including the local Omarchy Mac setup)**
and **Omarchy Linux / Hyprland**. Typing, thumb positions, home-row timing,
radio settings and hardware builds are shared. Host mode changes desktop,
screenshot and editing shortcuts.

**Hold the Escape thumb, then tap `Q` for Mac or `W` for Omarchy.** Release
Escape afterward. Mac is the startup mode; the selection lasts until restart.
Host mode is independent of Bluetooth profile/output selection. USB/BLE does
not automatically choose the operating system.

The default display shows **Mac** or **Omarchy**. While a layer is held it shows
its simple action name automatically. In the Keymap Editor, the additional
`Omarchy Navigate/Mouse/Clicks/System` layers activate automatically for that
host; they are not extra layers to remember or activate by hand.

| Layer | Access | Purpose |
| --- | --- | --- |
| Navigate | Hold Space | Arrows, editing and clipboard |
| Mouse | Hold Tab | Pointer, scroll and mouse buttons |
| Clicks | Hold bottom right outer key | Mouse buttons and clipboard on both hands |
| System | Hold Escape | Host mode, capture tools, media, output and Bluetooth |
| Numbers | Hold Backspace | Numpad and numeric punctuation |
| Symbols | Hold Enter | Programming symbols |
| F-keys | Hold Delete | F1–F12 and system keys |

### Six outer keys

| Outer row | Left, Mac | Right, Mac | Left, Omarchy | Right, Omarchy |
| --- | --- | --- | --- | --- |
| Top | Tap: Raycast (`⌘Space`); hold: Hyper | Tap: one-shot Hyper; hold: Hyper | Tap: Omarchy menu (`Super+Space`); hold: Super | Tap: one-shot Super; hold: Super |
| Middle | Clipboard History (`Hyper+V`) | Helium browser (`Hyper+B`) | Clipboard manager (`Super+Ctrl+V`) | Browser (`Super+Shift+Enter`) |
| Bottom | Quick terminal (`⌘` + backtick) | Capture menu (`⌘⇧5`); hold: Clicks | Scratchpad (`Super` + backtick) | Capture menu (`Super+Ctrl+C`); hold: Clicks |

All outer keys remain available on the other layers. The left top key uses a
180 ms hold-preferred behavior: another key press selects Hyper/Super
immediately; a tap opens the launcher on release. It has no home-row prior-idle
or opposite-hand restriction. The right top key also uses a 180 ms hold-preferred behavior: tap it and
release, then press a shortcut letter within 1.5 seconds for one-shot
Hyper/Super; hold it with another key for an ordinary modifier chord. The
one-shot is lazy (no host modifier before the target key), releases on the
target key press, and keeps `ignore-modifiers` enabled for the combined Hyper
modifier. It does not lock on. Direct layer Hyper keys remain ordinary held
modifiers. The bottom right key uses the default 200 ms layer-tap.
The image above illustrates the typing core; this table describes its six
additional utility keys.

`Z` and `/` are ordinary keys. Both outer Hyper keys and the direct layer
Hyper bindings send **left Ctrl + Alt/Option + Shift + GUI/Command**:
`LS(LA(LC(LGUI)))`. The active local Omarchy Mac `hidutil` mapping changes
right Command to left Option (`~/omarchy-mac/local/bin/mac-keyremap`), which
can remove Command from an all-right Hyper chord. Left Command avoids it.

The ordinary home-row modifiers retain their existing 280 ms tapping term,
175 ms quick-tap, 150 ms prior-idle guard, balanced flavor, opposite-hand
triggers and `hold-while-undecided`.

The Mac integration is in
[`omarchy-mac`](https://github.com/alxcrt/omarchy-mac/blob/main/config/raycast/SETUP.md).
Raycast's launcher is `⌘Space`; its app-owned hotkeys were configured and
verified in Settings on 18 October 2026:

| Hyper + | Action | Hyper + | Action |
| --- | --- | --- | --- |
| V | Clipboard History | B | Helium |
| T | Ghostty | W | cmux workspaces |
| A | ChatGPT | C | Claude |
| E | VS Code | L | Linear (existing) |
| P | Bitwarden | M | IINA |
| O | Omarchy menu | K | Shortcut guide |

Ghostty already configures `global:cmd+grave_accent=toggle_quick_terminal`.
It requires Ghostty running with its global shortcut registered; live show/hide
still needs testing on the Mac. This computer-use environment blocks Ghostty.
Omarchy's matching key toggles the **scratchpad**, which shows whatever window
you put there; send a terminal there with `Super+Shift+backtick` first. It does
not create a terminal automatically.

### Editing and System shortcuts

Navigate, Mouse and Clicks use explicit macOS `Command` shortcuts in Mac mode.
In Omarchy mode, copy/paste/cut use its current universal `Super+C/V/X`
bindings; Omarchy handles terminal copy/paste as `Ctrl+Shift+C/V`. Undo/redo
use `Ctrl+Z` / `Ctrl+Shift+Z` in Omarchy and `Command+Z` / `Command+Shift+Z`
on the Mac. The appropriate editing overlay follows the selected mode and
held layer automatically.

The System layer adds these shortcuts, using the letters printed by Base:

| Hold Escape + | Mac | Omarchy |
| --- | --- | --- |
| Q / W | Select Mac / Omarchy mode | Select Mac / Omarchy mode |
| F | Omarchy menu (`Hyper+O`) | Omarchy menu |
| P | CleanShot fullscreen | Screen recording menu / stop recording |
| B | CleanShot All-In-One | Screenshot text recognition (OCR) |
| J / L | Ghostty / Helium | Terminal / browser |
| U | Shortcut guide (`Hyper+K`) | Keybindings (`Super+K`) |
| Y | Area screenshot (`⌘⇧4`) | Screenshot (`Print`) |

Hold **Space + Q** for Mission Control on Mac; **Space + W / F** switches
previous / next Desktop on Mac or workspace on Omarchy.

CleanShot bindings were read from the local app's saved settings: area
`⌘⇧4`, fullscreen `⌘⇧3`, All-In-One `⌘⇧5`. The Linux bindings were verified
against upstream Omarchy
[`4a9c83d`](https://github.com/omacom/omarchy/tree/4a9c83deceb5bda84f706794c2ddc61084914fe0/default/hypr/bindings):
`utilities.lua`, `tiling.lua`, `clipboard.lua` and `applications.lua`.
They follow current stock Omarchy; local Linux overrides may require adjustments.

Edit `config/corne.keymap`, or select `dongle` in the
[Keymap Editor](https://nickcoutsos.github.io/keymap-editor/).
All 42 Corne positions are used. Runtime mode/layer changes need no reflashing.

## Power, signal and latency

Shared settings are in `config/corne.conf`; device roles are in `build.yaml`.
Debounce properties live on each half's scanner in its `corne_left.overlay` /
`corne_right.overlay`; the keyless dongle has no GPIO debounce configuration.

| Setting | Value | Effect / tradeoff |
| --- | --- | --- |
| Radio transmit power | +8 dBm on all parts | Already at the nRF52840 maximum; improves link margin |
| Press / release debounce | 1 / 5 ms | Low press latency with brief-noise filtering; restore 5 ms press if chatter appears |
| Idle timeout | 30 seconds | Idle keeps BLE connected; nice!view intentionally retains its image |
| Deep sleep | 15 minutes on battery | Saves power; reconnection after wake may take a few seconds |
| Split interval | ZMK default 6 × 1.25 ms = 7.5 ms | Already the minimum normal BLE connection interval |
| Split peripheral latency | ZMK default 30 | Allows skipped idle connection events; avoid forcing zero for an assumed typing speed gain |
| USB HID polling | ZMK default 1 ms | Used by the Prospector or standalone left half |

USB power prevents deep sleep. Peripheral halves disable USB HID while retaining
USB power detection. The unused SSD1306 OLED driver is disabled; nice!view and
Prospector remain supported. The empty combo node was removed; no combos or
macros are currently configured. Layer `display-name` properties allow the
Prospector to display names rather than numeric indices.

Dongle mode moves the central role to USB power, reducing the left half's battery
load. Further battery savings can come from omitting the halves' nice!view
shields if their displays are unnecessary, or shortening the sleep timeout at
the cost of more reconnects. Measure runtime before changing radio or scan
parameters. For unreliable links, improve antenna placement and move the
receiver away from metal and nearby USB 3 equipment.

References: [debounce](https://zmk.dev/docs/features/debouncing),
[low-power states](https://zmk.dev/docs/features/low-power-states),
[radio power](https://zmk.dev/docs/troubleshooting/connection-issues#unreliableweak-connection),
[split defaults](https://github.com/zmkfirmware/zmk/blob/4dd95d7840eb3d5a3f59bb29fbf1ab054715ef85/app/src/split/bluetooth/Kconfig),
[hold-tap behavior](https://zmk.dev/docs/keymaps/behaviors/hold-tap).

## Upstream versions

Checked on **18 October 2026**:

- ZMK and its reusable build workflow are pinned to latest `main` commit
  [`4dd95d7`](https://github.com/zmkfirmware/zmk/commit/4dd95d7840eb3d5a3f59bb29fbf1ab054715ef85),
  from 9 October 2026. The previous successful build used `9ebbeff`.
- Prospector is pinned to latest `feat/new-status-screens` commit
  [`ed98221`](https://github.com/carrefinho/prospector-zmk-module/commit/ed98221f3b52b7066dbb10ba3af8a29150b93a5a).
  It was already current. This branch provides the newer status-screen layouts
  and requires the Zephyr 4.1 ZMK line.
- The latest tagged ZMK release remains `v0.3.0`. This configuration uses current
  `main` for the board targets and Prospector module.

Update `config/west.yml` and the workflow reference together when upgrading.
ZMK's imported manifest supplies Zephyr and other module versions; imported
branch refs and the build container are not a complete dependency lock.

## Remaining hardware checks and layout decisions

- Test the same Raycast shortcut with both outer Hyper keys and direct
  layer Hyper keys. Modifier sides match; recognition on the Mac needs testing.
- Test ordinary `z` and `/`, home-row rolls, Hyper chords, host switching,
  automatic editing layers, one-shot Hyper timeout and fast letter rolls,
  capture-menu tap versus Clicks hold, wake/reconnect,
  battery readings and both dongle and standalone modes.
  CleanShot must be running. Test launcher taps versus Hyper holds and quick-terminal show/hide. Desktop switching needs existing Desktops; add them
  manually in Mission Control if needed. Linux commands need Omarchy running.
- `config/boards/shields/corn/` is an older unused definition. Current builds use
  `config/boards/shields/corne/`; editing `corn/` has no effect.
- BLE host profiles are 0–4, but Media exposes only 0–2 plus clear-current-profile.
  Add next/previous profile bindings if more are needed.
- Battery runtime, RSSI and end-to-end latency have not been measured by this
  source review. Compilation alone cannot establish those results.

## Credits and license

[Chocofi](https://github.com/pashutk/chocofi),
[Miryoku](https://github.com/manna-harbour/miryoku),
[ZMK](https://github.com/zmkfirmware/zmk),
[Keymap Editor](https://github.com/nickcoutsos/keymap-editor),
[Prospector](https://github.com/carrefinho/prospector-zmk-module).

MIT; see [LICENSE](LICENSE).

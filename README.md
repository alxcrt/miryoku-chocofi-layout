# Miryoku for 42-key Corne

Colemak-DH, Miryoku-inspired ZMK configuration for Alex's **42-key Corne** with
a 36-key typing core, six outer utility keys, **nice!nano nRF52840 controllers**
and optional nice!view displays. The `dongle`
branch supports a **Prospector USB dongle (XIAO BLE)** and standalone use with
only the two keyboard halves.

![Miryoku Chocofi base layout](assets/layout.png)

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

## Layout and Hyper

Edit `config/corne.keymap`, or use the
[Keymap Editor](https://nickcoutsos.github.io/keymap-editor/) with the `dongle` branch.
All 42 Corne positions are active. The 36-key typing core keeps its existing
layout; the outer columns add these shortcuts based on the local Omarchy Mac
setup and saved CleanShot preferences:

| Outer row | Left half | Right half |
| --- | --- | --- |
| Top | Previous Desktop (`⌃←`) | CleanShot area capture (`⌘⇧4`) |
| Middle | Mission Control (`⌃↑`) | CleanShot fullscreen (`⌘⇧3`) |
| Bottom | Next Desktop (`⌃→`) | Tap: CleanShot All-In-One (`⌘⇧5`); hold: Button layer |

These six keys fall through to Base on every other layer. Holding the bottom
right outer key opens Button without taking either Hyper key away. Its layer-tap
uses ZMK's default 200 ms tapping term. The layout image above illustrates the
typing core; this table describes the additional outer keys.

| Index | Layer | Base-layer access |
| --- | --- | --- |
| 0 | Base | Default |
| 1 | Nav | Hold Space |
| 2 | Mouse | Hold Tab |
| 3 | Button | Hold bottom right outer key |
| 4 | Media | Hold Escape |
| 5 | Num | Hold Backspace |
| 6 | Sym | Hold Enter |
| 7 | Fun | Hold Delete |

Both Hyper keys send **left Ctrl + left Alt/Option + left Shift + left GUI/Command**:
`LS(LA(LC(LGUI)))`. Left Hyper taps `Z`; right Hyper taps `/`. The direct Hyper
bindings on Nav, Mouse, Media, Num, Sym and Fun send the same modifier combination.
The right key retains `&hmr` for its timing and opposite-hand triggers.

The active Omarchy Mac `hidutil` mapping changes right Command to left Option
(`~/omarchy-mac/local/bin/mac-keyremap`). That mapping can remove Command from
the former all-right Hyper chord. Left Command avoids it; no Mac remaps or app
preferences need changing for these firmware bindings.

Existing hold-tap tuning is preserved: 280 ms tapping term, 175 ms quick-tap,
150 ms prior-idle guard, balanced flavor, opposite-hand triggers and
`hold-while-undecided`. A base Hyper press within 150 ms of another non-modifier
press resolves as its tap action even if held. Fast same-hand chords can also
resolve as taps. Test after pausing, or use a direct layer Hyper binding to
separate timing from host recognition. Change these typing safeguards only
after testing ordinary typing and shortcuts.

## Power, signal and latency

Shared settings are in `config/corne.conf`; device roles are in `build.yaml`.

| Setting | Value | Effect / tradeoff |
| --- | --- | --- |
| Radio transmit power | +8 dBm on all parts | Already at the nRF52840 maximum; improves link margin |
| Press / release debounce | 1 / 5 ms | Low press latency with brief-noise filtering; restore 5 ms press if chatter appears |
| Display idle | 30 seconds | Keeps BLE connected while displays idle |
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

- Test the same Raycast shortcut with both base Hyper keys and direct layer Hyper
  keys. Modifier sides now match; recognition on the Mac still needs testing.
- Test ordinary `z` and `/`, double-tap repeats, fast rolls, Hyper chords,
  wake/reconnect, battery readings, all six outer keys and both operating modes.
  CleanShot must be running. Desktop switching needs existing Desktops; add them
  manually in Mission Control if needed.
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

#!/usr/bin/env python3
"""Render the Corne reference. Requires reportlab; no device changes."""
from pathlib import Path
import re
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/corne-cheatsheet.pdf'
MD = ROOT / 'CHEATSHEET.md'
SOURCE = (ROOT / 'config/corne.keymap').read_text()
BASE = [['Q','W','F','P','B','J','L','U','Y',"'"],
        ['A','R','S','T','G','M','N','E','I','O'],
        ['Z','X','C','D','V','K','H',',','.','/']]
HYPER = [('A','ChatGPT'),('C','Claude'),('E','VS Code'),('L','Linear'),
         ('T','Ghostty'),('W','cmux workspaces'),('B','Helium browser'),
         ('V','Clipboard history'),('P','Bitwarden'),('M','IINA'),
         ('O','Omarchy menu'),('K','Shortcut guide')]
LAYERS = [
 ('Navigate', 'Hold Space', [
   ['Mission','Prev desk','Next desk','-','-','Redo','Paste','Copy','Cut','Undo'],
   ['Cmd','Alt','Ctrl','Shift','-','Caps*','Left','Down','Up','Right'],
   ['Hyper','-','-','-','-','Insert','Browser home','Page down','Page up','End']],
   'Right thumbs: Enter / Backspace / Delete. Linux: W/F = previous/next workspace; Q inactive.'),
 ('Mouse', 'Hold Tab', [
   ['-','-','-','-','-','Redo','Paste','Copy','Cut','Undo'],
   ['Cmd','Alt','Ctrl','Shift','-','-','Move left','Move down','Move up','Move right'],
   ['Hyper','-','-','-','-','-','Scroll left','Scroll down','Scroll up','Scroll right']],
   'Right thumbs: Right click / Left click / Middle click.'),
 ('Numbers', 'Hold Backspace', [
   ['[','7','8','9',']','-','-','-','-','-'],
   [';','4','5','6','=','-','Shift','Ctrl','Alt','Cmd'],
   ['`','1','2','3','\\','-','-','-','-','Hyper']],
   'Left thumbs: . / 0 / -'),
 ('Symbols', 'Hold Enter', [
   ['{','&','*','(','}','-','-','-','-','-'],
   [':','$','%','^','+','-','Shift','Ctrl','Alt','Cmd'],
   ['~','!','@','#','|','-','-','-','-','Hyper']],
   'Left thumbs: ( / ) / _'),
 ('F-keys', 'Hold Delete', [
   ['F12','F7','F8','F9','SysRq','-','-','-','-','-'],
   ['F11','F4','F5','F6','Scroll lock','-','Shift','Ctrl','Alt','Cmd'],
   ['F10','F1','F2','F3','Pause','-','-','-','-','Hyper']],
   'Left thumbs: Context menu / Space / Tab.'),
]
THUMBS = [('Escape','System'),('Space','Navigate'),('Tab','Mouse'),
          ('Enter','Symbols'),('Backspace','Numbers'),('Delete','F-keys')]
SYSTEM = [('Q / W','Mac / Omarchy','Mac / Omarchy'),
          ('F','Omarchy menu','Omarchy menu'),('P','Fullscreen capture','Record / stop'),
          ('B','Capture menu','Screenshot OCR'),('J','Ghostty','Terminal'),
          ('L','Helium','Browser'),('U','Shortcut guide','Keybindings'),('Y','Area capture','Screenshot')]
OUTER = [('Top','Quick terminal','Capture menu; hold Clicks', 'Scratchpad','Capture menu; hold Clicks'),
         ('Middle','Caps Word','Clipboard history','Caps Word','Clipboard manager'),
         ('Bottom','Tap Raycast; hold Hyper','Tap one-shot Hyper; hold Hyper','Tap menu; hold Super','Tap one-shot Super; hold Super')]

# Guard against silently rendering a reference for a different-sized layout.
parsed = {}
for m in re.finditer(r'(\w+)_layer\s*\{\s*(?://[^\n]*\n\s*)?bindings\s*=\s*<([\s\S]*?)>;', SOURCE):
    parsed[m[1]] = [' '.join(x.split()) for x in re.findall(r'&\w+(?:\s+[^&]+)?',m[2])]
assert len(parsed) == 13 and all(len(v) == 42 for v in parsed.values())
assert parsed['mac'][0] == '&kp LG(GRAVE)' and parsed['omarchy'][0] == '&kp LG(GRAVE)'
assert parsed['mac'][24] == '&launcher LS(LA(LC(LGUI))) LG(SPACE)'
assert parsed['omarchy'][24] == '&launcher LGUI LG(SPACE)'
assert parsed['mac'][11] == '&lt 4 LG(LS(N5))'
assert parsed['omarchy'][11] == '&lt 4 LG(LC(C))'
assert parsed['mac'][35] == '&hyper LS(LA(LC(LGUI))) LS(LA(LC(LGUI)))'
assert parsed['omarchy'][35] == '&hyper LGUI LGUI'
assert parsed['system'][9] == '&kp LG(LS(N4))' and parsed['omarchy_system'][9] == '&kp PSCRN'
assert parsed['mac'][25] == '&kp Z' and parsed['mac'][34] == '&kp SLASH'
assert parsed['mac'][12] == parsed['omarchy'][12] == '&caps_word'
assert parsed['mac'][23] == '&kp LS(LA(LC(LG(V))))'
assert parsed['omarchy'][23] == '&kp LG(LC(V))'

# Read each layer's printable actions from its real bindings. Base labels are
# only location hints; the grid must follow source edits, not a copied diagram.
KEY_LABELS = {
    'LC(UP)':'Mission', 'LC(LEFT)':'Prev desk', 'LC(RIGHT)':'Next desk',
    'LG(LS(Z))':'Redo', 'LG(V)':'Paste', 'LG(C)':'Copy', 'LG(X)':'Cut', 'LG(Z)':'Undo',
    'LGUI':'Cmd', 'LEFT_ALT':'Alt', 'LCTRL':'Ctrl', 'LEFT_SHIFT':'Shift',
    'RIGHT_SHIFT':'Shift', 'RCTRL':'Ctrl', 'RIGHT_ALT':'Alt',
    'LS(LA(LC(LGUI)))':'Hyper', 'CAPSLOCK':'Caps*', 'LEFT':'Left', 'DOWN':'Down',
    'UP':'Up', 'RIGHT':'Right', 'INSERT':'Insert', 'C_AC_HOME':'Browser home',
    'PAGE_DOWN':'Page down', 'PAGE_UP':'Page up', 'END':'End',
    'LBKT':'[', 'RIGHT_BRACKET':']', 'SEMI':';', 'EQUAL':'=', 'GRAVE':'`',
    'BACKSLASH':'\\', 'LEFT_BRACE':'{', 'AMPERSAND':'&', 'KP_MULTIPLY':'*',
    'LEFT_PARENTHESIS':'(', 'RIGHT_BRACE':'}', 'COLON':':', 'DOLLAR':'$',
    'PERCENT':'%', 'CARET':'^', 'PLUS':'+', 'TILDE':'~', 'EXCLAMATION':'!',
    'AT_SIGN':'@', 'HASH':'#', 'PIPE':'|', 'SYSREQ':'SysRq',
    'SCROLLLOCK':'Scroll lock', 'PAUSE_BREAK':'Pause',
}
def action_label(binding):
    if binding == '&none': return '-'
    if binding.startswith('&kp '):
        code=binding[4:]
        if code in KEY_LABELS: return KEY_LABELS[code]
        if re.fullmatch(r'N[0-9]',code): return code[1:]
        if re.fullmatch(r'F[0-9]+',code): return code
    for prefix, label in [('&mmv MOVE_', 'Move'), ('&msc SCRL_', 'Scroll')]:
        if binding.startswith(prefix): return label+' '+binding[len(prefix):].lower()
    raise ValueError('Add a printable label for '+binding)
core=[[1,2,3,4,5,6,7,8,9,10], [13,14,15,16,17,18,19,20,21,22],
      [25,26,27,28,29,30,31,32,33,34]]
LAYERS=[(name,hold,[[action_label(parsed[{'F-keys':'fkeys'}.get(name,name.lower())][i])
                      for i in row] for row in core],note)
        for name,hold,_old_rows,note in LAYERS]
OUT.parent.mkdir(parents=True,exist_ok=True)

fontdir = Path('/System/Library/Fonts/Supplemental')
for family, filename in [('Body','Arial.ttf'),('Bold','Arial Bold.ttf')]:
    if (fontdir/filename).exists(): pdfmetrics.registerFont(TTFont(family,str(fontdir/filename)))
    else: pdfmetrics.registerFont(pdfmetrics.Font(family,'Helvetica-Bold' if family=='Bold' else 'Helvetica','WinAnsiEncoding'))

W,H=A4
INK=colors.HexColor('#172D3B'); TEAL=colors.HexColor('#087E83')
MUTED=colors.HexColor('#526572'); LINE=colors.HexColor('#D8E2E6')
PALE=colors.HexColor('#F1F6F7'); PAPER=colors.HexColor('#FCFDFC')
C=canvas.Canvas(str(OUT), pagesize=A4, invariant=1)
C.setTitle('Corne - Mac and Omarchy cheat sheet')
C.setAuthor('Alex')

def text(x,y,s,size=9,bold=False,color=INK):
    C.setFillColor(color); C.setFont('Bold' if bold else 'Body',size); C.drawString(x,y,s)

def fit(x,y,s,width,size=9,bold=False,color=INK):
    font='Bold' if bold else 'Body'
    while pdfmetrics.stringWidth(s,font,size)>width and size>5.5: size-=.2
    assert pdfmetrics.stringWidth(s,font,size)<=width+1, s
    text(x,y,s,size,bold,color)

def box(x,y,w,h,fill=PALE):
    C.setFillColor(fill); C.setStrokeColor(LINE); C.setLineWidth(.5)
    C.roundRect(x,y,w,h,5,fill=1,stroke=1)

def heading(x,y,s,small=''):
    text(x,y,s,11,True)
    if small: text(x,y-14,small,8,color=MUTED)

def header(page,title,subtitle):
    C.setFillColor(PAPER); C.rect(0,0,W,H,fill=1,stroke=0)
    text(40,H-39,'CORNE / 42 KEYS',9,True,TEAL)
    text(40,H-70,title,24,True)
    text(40,H-88,subtitle,9,color=MUTED)
    C.setStrokeColor(LINE); C.line(40,H-100,W-40,H-100)
    text(40,24,'MAC + OMARCHY  /  Colemak-DH  /  dongle branch',7,color=MUTED)
    text(W-73,24,f'{page} / 2',8,True,TEAL)

def table(x,y,width,headers,rows,ratios=None,rh=19,size=8):
    ratios=ratios or [1/len(headers)]*len(headers)
    widths=[width*r for r in ratios]
    C.setFillColor(INK); C.roundRect(x,y-rh,width,rh,4,fill=1,stroke=0)
    pos=x
    for h,w in zip(headers,widths): fit(pos+7,y-rh+6,h,w-14,size,True,colors.white);pos+=w
    y-=rh
    for n,row in enumerate(rows):
        if n%2==0:
            C.setFillColor(PALE);C.rect(x,y-rh,width,rh,fill=1,stroke=0)
        pos=x
        for v,w in zip(row,widths):fit(pos+7,y-rh+6,str(v),w-14,size);pos+=w
        y-=rh
    return y

def key(x,y,w,h,label,sub='',accent=False):
    box(x,y,w,h,colors.HexColor('#E1F0EE') if accent else colors.white)
    font='Bold'; size=12 if len(label)<3 else 7.5
    while pdfmetrics.stringWidth(label,font,size)>w-5: size-=.2
    C.setFillColor(TEAL if accent else INK);C.setFont(font,size)
    C.drawCentredString(x+w/2,y+(h-8)/2+(4 if sub else 0),label)
    if sub:
        size=6.2
        while pdfmetrics.stringWidth(sub,'Body',size)>w-4:size-=.2
        C.setFont('Body',size);C.setFillColor(MUTED);C.drawCentredString(x+w/2,y+4,sub)

header(1,'Your everyday keys','Caps Word for UPPER_CASE. Hyper for shortcuts. Hold a thumb for a layer.')
box(40,701,W-80,30)
text(50,713,'HOST MODE',8,True,TEAL)
text(120,713,'Hold Escape + Q = Mac     |     Hold Escape + W = Omarchy',9,True)
text(40,684,'BASE / MAC UTILITIES',10,True)
kw,gap,split=35,4,32
start=(W-(12*kw+10*gap+split))/2
leftouter=[('Quick term','Cmd + `'),('Caps Word','UPPER_CASE'),('Raycast','H: Hyper')]
rightouter=[('Capture','H: Clicks'),('Clipboard',''),('Hyper','Tap: 1-shot')]
mods={'A':'H: Cmd','R':'H: Alt','S':'H: Ctrl','T':'H: Shift','N':'H: Shift','E':'H: Ctrl','I':'H: Alt','O':'H: Cmd'}
for row,letters in enumerate(BASE):
    y=646-row*35
    key(start,y,kw,30,*leftouter[row],accent=True)
    for j,l in enumerate(letters[:5]):key(start+(j+1)*(kw+gap),y,kw,30,l,mods.get(l,''))
    rx=start+6*kw+5*gap+split
    for j,l in enumerate(letters[5:]):key(rx+j*(kw+gap),y,kw,30,l,mods.get(l,''))
    key(rx+5*(kw+gap),y,kw,30,*rightouter[row],accent=True)
for j,(name,layer) in enumerate(THUMBS[:3]):key(start+(j+3)*(kw+gap),539,kw,29,name,'H: '+layer)
for j,(name,layer) in enumerate(THUMBS[3:]):key(rx+j*(kw+gap),539,kw,29,name,'H: '+layer)
text(40,525,'H = hold. Right bottom: tap, then a shortcut within 1.5 sec; or hold for normal Hyper.',8,color=MUTED)

heading(40,503,'Six outer keys - same purpose on both hosts')
table(40,491,W-80,['Position','Mac: left / right','Omarchy: left / right'],[
 ('Top','Quick terminal  |  Capture/Clicks','Scratchpad  |  Capture/Clicks'),
 ('Middle','Caps Word  |  Clipboard','Caps Word  |  Clipboard'),
 ('Bottom','Raycast/Hyper  |  Sticky Hyper','Menu/Super  |  Sticky Super')], [.13,.435,.435],rh=23,size=8)

heading(40,378,'Hyper shortcuts - Mac')
text(40,363,'Hyper = left Ctrl + Alt + Shift + Cmd',8,color=TEAL)
table(40,350,236,['Hyper +','Opens'],HYPER,[.25,.75],rh=18,size=8.5)
heading(298,378,'Hold a thumb')
table(298,365,W-338,['Thumb','Layer'],THUMBS,[.47,.53],rh=18,size=8.5)
heading(298,217,'Hold Escape + letter')
table(298,204,W-338,['Key','Mac','Omarchy'],SYSTEM,[.19,.43,.38],rh=15,size=7.5)

text(40,91,'QUICK TERMINAL',8,True,TEAL)
text(40,77,'Mac: Cmd + backtick (`).',8.5)
text(40,63,'Linux: Super + ` toggles the scratchpad.',8,color=MUTED)
text(40,50,'Put a terminal there first: Super + Shift + `.',7.5,color=MUTED)
text(40,37,'Flash the updated firmware first. Physical activation still needs testing.',7.1,color=MUTED)
C.showPage()

header(2,'The layers','Small labels show the Base key. Big labels show what it does while the thumb is held.')
y=H-124
for title,hold,rows,note in LAYERS:
    text(40,y,title.upper(),10,True,TEAL)
    text(144,y,hold,9,True)
    if title in ('Navigate','Mouse'):text(330,y,'Mac shown; Linux editing follows host mode',7,color=MUTED)
    top=y-30
    innerw=(W-80-24-8*4)/10
    for row,actions in enumerate(rows):
        for j,action in enumerate(actions):
            x=40+j*(innerw+4)+(20 if j>=5 else 0)
            yy=top-row*26
            box(x,yy-11,innerw,24,colors.white if action!='-' else PALE)
            text(x+4,yy+5,BASE[row][j],6.3,color=MUTED)
            fit(x+4,yy-6,action,innerw-8,8.2,True,TEAL if action!='-' else LINE)
    text(40,top-80,note,7.1,color=MUTED)
    y-=127

# Layer detail that is useful, without turning the sheet into a firmware manual.
text(40,76,'CLICKS',8,True,TEAL)
text(102,76,'Hold outer top-right. Left thumbs: Middle / Left / Right click.',7.5)
text(102,64,'Right thumbs: Right / Left / Middle click. Clipboard shortcuts on both hands.',7.5)
text(40,48,'* Mac hidutil maps Caps Lock to Escape. Navigate H sends Browser Home, not a document Home key.',7,color=MUTED)
text(40,37,'System: N/E/I = previous track / volume down / volume up; H/,/. = Bluetooth profiles 1/2/3; / clears current pairing.',6.8,color=MUTED)
C.save()

# Markdown keeps the essential reference readable in GitHub and text editors.
md=['# Corne cheat sheet','',
    '42 keys, Colemak-DH. The Corne layout requires the new firmware; Mac Raycast assignments are saved. Physical Hyper and quick-terminal activation still need testing.','',
    '**Select host:** hold **Escape + Q** for Mac or **Escape + W** for Omarchy. Mac is the startup mode; reboot resets the mode.','',
    '## Outer keys','',
    '| Position | Mac left | Mac right | Omarchy left | Omarchy right |',
    '| --- | --- | --- | --- | --- |']
md += ['| '+' | '.join(r)+' |' for r in OUTER]
md += ['', 'Mac quick terminal: **Command + backtick (`)**. Linux scratchpad: **Super + backtick**; put a terminal there first with **Super + Shift + backtick**.',
       '', 'Left bottom taps the launcher and holds Hyper/Super. Right bottom taps one-shot Hyper/Super: release it, then press the shortcut within 1.5 seconds. It releases after that target key press, or times out unused; it does not lock. Hold it for an ordinary modifier chord. Left bottom has a 180 ms hold-preferred term; capture/Clicks has the default 200 ms layer-tap.',
       '', '## Caps Word', '', 'Tap the left-middle outer key for uppercase words and identifiers such as `MY_VARIABLE`. Letters, digits, underscores, Backspace and Delete continue it. A space or another separator ends it; tap Caps Word again to turn it off. This is word-by-word capitalization, not a persistent Caps Lock. Browser access remains on Hyper+B (Mac) or System + L.', '', '## Thumb layers','', '| Tap key; hold for | Layer |','| --- | --- |']
md += [f'| {a} | {b} |' for a,b in THUMBS]
md += ['| Outer top-right | Clicks |','', '## Hyper - Mac','',
       '**Hyper = left Control + Option/Alt + Shift + Command.** Both bottom outer keys provide it. Z and / type normally.','', '| Hyper + | Opens |','| --- | --- |']
md += [f'| {a} | {b} |' for a,b in HYPER]
md += ['', '## System - hold Escape','', '| Base letter | Mac | Omarchy |','| --- | --- | --- |']
md += ['| '+' | '.join(r)+' |' for r in SYSTEM]
md += ['', 'Hold **Space + Q** for Mission Control on Mac. Hold **Space + W / F** for previous / next Desktop on Mac or workspace on Linux.',
       '', '## Base typing positions','', 'Read each layer grid using these same positions. Outer utility keys are omitted.','', '```text']
md += [' '.join(f'{k:^12}' for k in row[:5])+'  |  '+' '.join(f'{k:^12}' for k in row[5:]) for row in BASE]
md += ['```','', 'Home-row holds: **A/R/S/T = Cmd/Alt/Ctrl/Shift**; **N/E/I/O = Shift/Ctrl/Alt/Cmd**. On Linux, Cmd means Super.',
       '', 'Ordinary home-row modifiers retain 280 ms tapping term, 175 ms quick-tap and 150 ms prior-idle protection.']
for title,hold,rows,note in LAYERS:
    md += ['',f'## {title} - {hold}','', '```text']
    md += [' '.join(f'{k:^12}' for k in row[:5])+'  |  '+' '.join(f'{k:^12}' for k in row[5:]) for row in rows]
    md += ['```', '',note]
md += ['', 'Navigate/Mouse clipboard row, right side: **J redo, L paste, U copy, Y cut, apostrophe undo**. Mac uses Command; Omarchy uses its universal Super copy/paste/cut and Control undo/redo.',
       '', '**Caps (asterisk)** sends Caps Lock; your Mac remaps it to Escape. **Browser home** sends the consumer Browser Home action, not a document Home key.',
       '', '## Clicks - hold outer top-right','',
       '- Left thumbs: middle / left / right mouse button.',
       '- Right thumbs: right / left / middle mouse button.',
       '- Left top/bottom rows: Q/W/F/P/B or Z/X/C/D/V = undo/cut/copy/paste/redo.',
       '- Right top/bottom rows: J/L/U/Y/apostrophe or K/H/comma/dot/slash = redo/paste/copy/cut/undo.',
       '', '## System media and connections - hold Escape','',
       '| Base key | Action |','| --- | --- |',
       '| N / O | Previous / next track |','| E / I | Volume down / up |',
       '| Enter / Backspace / Delete thumbs | Play-pause / next track / mute |',
       '| M | Toggle external peripheral power (hardware dependent) |',
       '| K | Toggle USB / Bluetooth output |','| H / comma / dot | Bluetooth profiles 1 / 2 / 3 |',
       '| Slash | Clear the selected Bluetooth profile pairing |',
       '', 'Use the Bluetooth host controls in standalone mode. In dongle mode, the Prospector normally outputs through USB. Clearing a host profile removes that saved host pairing.',
       '', '## Optional next features (not enabled)', '', '- [Key Repeat](https://zmk.dev/docs/keymaps/behaviors/key-repeat): send the last key again.', '- [Sticky layers](https://zmk.dev/docs/keymaps/behaviors/sticky-layer): tap once for one symbol or number, then return to typing.', '', '## Source and refresh','',
       'Reference: `config/corne.keymap` and the Mac Raycast assignments documented in `README.md`. Native Omarchy shortcuts require its standard bindings. The Numbers/Symbols/F-keys grids share the same placement on both hosts.',
       '', 'PDF: [Printable cheat sheet](output/pdf/corne-cheatsheet.pdf). Rebuild with `python3 tools/generate_cheatsheet.py` in an environment with ReportLab installed.']
MD.write_text('\n'.join(md)+'\n')
print(OUT)
print(MD)

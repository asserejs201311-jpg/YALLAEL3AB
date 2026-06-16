# -*- coding: utf-8 -*-
import re, urllib.parse
s=open("yallael3ab.html",encoding="utf-8").read()

# strip variation selectors so we can map base codepoints
s=s.replace("️","")

# ---------- icon path library (24x24) ----------
# line icons use stroke=currentColor; solid use fill=currentColor; status icons hardcode color
def L(inner):   # line/stroke icon
    return ("<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' "
            "stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>"+inner+"</svg>")
def F(inner,fill="currentColor"):  # solid fill icon
    return "<svg viewBox='0 0 24 24' fill='"+fill+"'>"+inner+"</svg>"
def Lc(inner,color):  # colored stroke
    return ("<svg viewBox='0 0 24 24' fill='none' stroke='"+color+"' "
            "stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>"+inner+"</svg>")

ICONS={
 "ball":L("<circle cx='12' cy='12' r='9'/><path d='M12 7l4 3-1.5 5h-5L8 10z'/>"),
 "building":L("<rect x='5' y='3' width='14' height='18' rx='1'/><path d='M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2'/>"),
 "user":L("<circle cx='12' cy='8' r='4'/><path d='M5 21c0-4 3.5-6 7-6s7 2 7 6'/>"),
 "envelope":L("<rect x='3' y='5' width='18' height='14' rx='2'/><path d='M4 7l8 6 8-6'/>"),
 "lock":L("<rect x='5' y='11' width='14' height='9' rx='2'/><path d='M8 11V8a4 4 0 0 1 8 0v3'/>"),
 "store":L("<path d='M4 9h16M4 9l1-5h14l1 5M5 9v11h14V9M9 20v-5h6v5'/>"),
 "stadium":L("<ellipse cx='12' cy='12' rx='9' ry='6'/><path d='M7 12a5 3 0 0 1 10 0'/>"),
 "pin":L("<path d='M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z'/><circle cx='12' cy='10' r='2.5'/>"),
 "money":L("<rect x='3' y='6' width='18' height='12' rx='2'/><circle cx='12' cy='12' r='2.5'/>"),
 "ruler":L("<path d='M4 16L16 4l4 4L8 20z'/><path d='M9 9l2 2M12 6l2 2M6 12l2 2'/>"),
 "warn":Lc("<path d='M12 3l9 16H3z'/><path d='M12 9v5M12 17h.01'/>","#fbbf24"),
 "check":L("<path d='M5 12l5 5 9-11'/>"),
 "bell":L("<path d='M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6z'/><path d='M10 20a2 2 0 0 0 4 0'/>"),
 "search":L("<circle cx='11' cy='11' r='6'/><path d='M20 20l-4-4'/>"),
 "gear":L("<circle cx='12' cy='12' r='3'/><path d='M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2'/>"),
 "map":L("<path d='M9 4L3 6v14l6-2 6 2 6-2V4l-6 2-6-2z'/><path d='M9 4v14M15 6v14'/>"),
 "calendar":L("<rect x='4' y='5' width='16' height='16' rx='2'/><path d='M4 9h16M8 3v4M16 3v4'/>"),
 "compass":L("<circle cx='12' cy='12' r='9'/><path d='M15 9l-2 6-4 0 2-6z'/>"),
 "home":L("<path d='M4 11l8-7 8 7'/><path d='M6 10v10h12V10'/>"),
 "trophy":L("<path d='M8 4h8v5a4 4 0 0 1-8 0z'/><path d='M8 6H5a3 3 0 0 0 3 3M16 6h3a3 3 0 0 1-3 3M10 14h4M9 20h6M12 14v6'/>"),
 "grid":L("<rect x='3' y='3' width='7' height='7' rx='1'/><rect x='14' y='3' width='7' height='7' rx='1'/><rect x='3' y='14' width='7' height='7' rx='1'/><rect x='14' y='14' width='7' height='7' rx='1'/>"),
 "barchart":L("<path d='M3 21h18'/><rect x='5' y='11' width='3' height='8'/><rect x='11' y='6' width='3' height='13'/><rect x='17' y='13' width='3' height='6'/>"),
 "plus":L("<path d='M12 5v14M5 12h14'/>"),
 "crown":F("<path d='M3 8l4.5 4L12 4l4.5 8L21 8l-2 11H5z'/>"),
 "card":L("<rect x='3' y='5' width='18' height='14' rx='2'/><path d='M3 10h18'/>"),
 "robot":L("<rect x='5' y='8' width='14' height='11' rx='2'/><path d='M9 13h.01M15 13h.01M9 16h6M12 5v3'/><circle cx='12' cy='4' r='1'/>"),
 "send":F("<path d='M3 11l18-8-8 18-2-7z'/>"),
 "heartfill":F("<path d='M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z'/>"),
 "heartline":L("<path d='M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z'/>"),
 "brokenheart":L("<path d='M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z'/><path d='M12 7l-1.5 3 3 2-1.5 3'/>"),
 "clock":L("<circle cx='12' cy='12' r='9'/><path d='M12 7v5l3 2'/>"),
 "trash":L("<path d='M4 7h16M9 7V5h6v2M6 7l1 13h10l1-13'/>"),
 "checkc":Lc("<circle cx='12' cy='12' r='9'/><path d='M8 12l3 3 5-6'/>","#22c55e"),
 "belloff":L("<path d='M6 9a6 6 0 0 1 9.5-4.8M18 13c0 2 2 6 2 6H6M10 20a2 2 0 0 0 4 0'/><path d='M3 3l18 18'/>"),
 "bank":L("<path d='M4 10l8-5 8 5M5 10v8M19 10v8M9 10v8M15 10v8M3 21h18'/>"),
 "chartup":L("<path d='M3 17l6-6 4 4 7-8'/><path d='M17 7h4v4'/>"),
 "pencil":L("<path d='M4 20l1-4 11-11 3 3-11 11z'/>"),
 "x":L("<path d='M6 6l12 12M18 6L6 18'/>"),
 "mailbox":L("<path d='M3 12a4 4 0 0 1 8 0v7H3z'/><path d='M11 12h7a3 3 0 0 1 3 3v4'/><path d='M7 12V9'/>"),
 "chat":L("<path d='M4 5h16v11H9l-5 4z'/>"),
 "door":L("<path d='M14 3H5v18h9M14 12h6M17 9l3 3-3 3'/>"),
 "refresh":L("<path d='M20 11A8 8 0 0 0 6 6L4 8M4 13a8 8 0 0 0 14 5l2-2'/><path d='M4 4v4h4M20 20v-4h-4'/>"),
 "ban":Lc("<circle cx='12' cy='12' r='9'/><path d='M6 6l12 12'/>","#ef4444"),
 "clipboard":L("<rect x='6' y='4' width='12' height='17' rx='2'/><path d='M9 4h6v3H9z'/>"),
 "tools":L("<path d='M15 7l3-3 2 2-3 3-2-2zM13 9L4 18l2 2 9-9M9 13l-3 3'/>"),
 "telescope":L("<path d='M3 16l13-7 2 4-13 7zM10 13l3 5M7 19l2-3'/>"),
 "shield":L("<path d='M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z'/>"),
 "bolt":F("<path d='M13 2L4 14h6l-1 8 9-12h-6z'/>"),
 "mobile":L("<rect x='7' y='3' width='10' height='18' rx='2'/><path d='M11 18h2'/>"),
 "star":F("<path d='M12 3l2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-2.9-5.3 2.9 1.1-6L3.4 9.4l6-.8z'/>","#fbbf24"),
}

def span(key):
    return "<span class='ico'>"+ICONS[key]+"</span>"

# ---------- 1) decorative CSS backgrounds ----------
def datauri(svg):
    return "url(\"data:image/svg+xml,"+urllib.parse.quote(svg)+"\") center/contain no-repeat"
ball_w="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='1.4'><circle cx='12' cy='12' r='9'/><path d='M12 7l4 3-1.5 5h-5L8 10z'/></svg>"
coin_w="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='1.4'><ellipse cx='12' cy='6' rx='8' ry='3'/><path d='M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6'/><path d='M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6'/></svg>"
star_w="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'><path d='M12 3l2.6 5.6 6 .8-4.4 4.2 1.1 6L12 17.9 6.7 20.8l1.1-6L3.4 9.4l6-.8z'/></svg>"

s=s.replace(
 '.homeHero::after{content:"⚽";position:absolute;right:-22px;bottom:-28px;font-size:7.5rem;opacity:.12;transform:rotate(-15deg)}',
 '.homeHero::after{content:"";position:absolute;right:-22px;bottom:-30px;width:150px;height:150px;opacity:.16;transform:rotate(-15deg);background:'+datauri(ball_w)+'}')
s=s.replace(
 '.earnhero::after{content:"💰";position:absolute;right:-12px;bottom:-18px;font-size:5.5rem;opacity:.15}',
 '.earnhero::after{content:"";position:absolute;right:6px;bottom:6px;width:96px;height:96px;opacity:.2;background:'+datauri(coin_w)+'}')
s=s.replace(
 '.subcard::after{content:"⭐";position:absolute;right:-10px;top:-14px;font-size:5rem;opacity:.08}',
 '.subcard::after{content:"";position:absolute;right:8px;top:8px;width:80px;height:80px;opacity:.1;background:'+datauri(star_w)+'}')

# ---------- 2) neutralize emoji in textContent / escaped strings ----------
neut=[
 ("Yalla! 👋 I'm your Pitch Finder AI.","Yalla! I'm your Pitch Finder AI."),
 ("nothing matches that 🤔 Try","nothing matches that. Try"),
 ('"📍 Based on your location, here"','"Based on your location, here"'),
 ("${i+1}. ⚽ ${f.name}","${i+1}. ${f.name}"),
 ("\\nTap to book instantly ⚡","\\nTap to book instantly"),
 ("textContent=`📍 ${selField.area}","textContent=`${selField.area}"),
 ("Welcome to YallaEl3ab! 🎉","Welcome to YallaEl3ab!"),
 ("Booking requested 📩","Booking requested"),
 ("Booking confirmed ✅","Booking confirmed"),
 ("Subscription renewed 👑","Subscription renewed"),
 ("Booking accepted ✓","Booking accepted"),
]
for a,b in neut:
    assert a in s, "MISSING neutralize: "+repr(a)
    s=s.replace(a,b)

# ---------- 3) convert toast/icon string args to ICON refs ----------
# default param
s=s.replace('function toast(msg,ic="✅")','function toast(msg,ic=ICON.checkc)')
arg_map={
 "✅":"checkc","⚽":"ball","🎉":"party","👋":"ball","🚫":"ban","⚠":"warn",
 "🏟":"stadium","🔄":"refresh","❤":"heartfill","💔":"brokenheart","🗑":"trash",
 "👑":"crown","📋":"clipboard","💳":"card","🛠":"tools","💬":"chat","📈":"chartup",
}
# party not in ICONS -> use confetti-ish: map to star
ICONS_extra={"party":ICONS["star"]}
def arg_repl(m):
    e=m.group(2)
    key=arg_map.get(e)
    return ","+("ICON."+key)+")" if key else m.group(0)
s=re.sub(r",(['\"])(✅|⚽|🎉|👋|🚫|⚠|🏟|🔄|❤|💔|🗑|👑|📋|💳|🛠|💬|📈)\1\)",arg_repl,s)

# ---------- 4) global emoji -> inline span in remaining (HTML/template) ----------
emoji_to_key={
 "⚽":"ball","🏢":"building","👤":"user","✉":"envelope","🔒":"lock","🏪":"store",
 "🏟":"stadium","📍":"pin","💵":"money","📐":"ruler","⚠":"warn","✓":"check",
 "🔔":"bell","🔍":"search","⚙":"gear","🗺":"map","📅":"calendar","🧭":"compass",
 "🏠":"home","🏆":"trophy","▦":"grid","📊":"barchart","➕":"plus","👑":"crown",
 "💳":"card","🤖":"robot","➤":"send","❤":"heartfill","🤍":"heartline","💔":"brokenheart",
 "🕒":"clock","🗑":"trash","✅":"checkc","🔕":"belloff","🏦":"bank","📈":"chartup",
 "✏":"pencil","✕":"x","📭":"mailbox","💬":"chat","🚪":"door","🔄":"refresh",
 "⛔":"ban","🚫":"ban","📋":"clipboard","🛠":"tools","🔭":"telescope","🛡":"shield",
 "⚡":"bolt","📱":"mobile","⭐":"star","💸":"money","💰":"money","🎉":"star","👋":"ball","🤔":"search",
}
# order longest first not needed (all single codepoint emoji)
for e,key in emoji_to_key.items():
    s=s.replace(e, span(key))

# ---------- 5) inject ICON js object + .ico css ----------
icon_js="const ICON={"+",".join("%s:`%s`"%(k,(ICONS_extra.get(k) or ICONS.get(k))) for k in set(list(arg_map.values())+["checkc","party"])) + "};\n"
# build ICON map with span wrappers for toast usage
icon_js="const ICON={"+",".join("%s:`%s`"%(k,span(k) if k in ICONS else "<span class='ico'>"+ICONS_extra[k]+"</span>") for k in sorted(set(list(arg_map.values())+["checkc","party"]))) + "};\n"
s=s.replace("const $=s=>document.querySelector(s);","const $=s=>document.querySelector(s);\n"+icon_js,1)

# .ico css after .pm .pmlogo svg rule
css_add=("\n.ico{display:inline-flex;align-items:center;justify-content:center;width:1em;height:1em;line-height:0;vertical-align:-.14em;flex-shrink:0}"
         "\n.ico svg{width:100%;height:100%;display:block}")
s=s.replace(".pmlogo .pay-svg{height:24px;width:auto;display:block;overflow:visible}",
            ".pmlogo .pay-svg{height:24px;width:auto;display:block;overflow:visible}"+css_add,1)

open("yallael3ab.html","w",encoding="utf-8").write(s)
print("done; bytes",len(s))

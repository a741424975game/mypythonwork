# -*- coding: UTF-8 -*-

import re, random

ss = """
 <div class="emoji-panel ctrl-panel dp-none" style="display: none;">
                <!--repeat11330623127:start--><a>(⌒▽⌒)</a><!--repeat11330623127--><a>（￣▽￣）</a><!--repeat11330623127--><a>(=・ω・=)</a><!--repeat11330623127--><a>(｀・ω・´)</a><!--repeat11330623127--><a>(〜￣△￣)〜</a><!--repeat11330623127--><a>(･∀･)</a><!--repeat11330623127--><a>(°∀°)ﾉ</a><!--repeat11330623127--><a>(￣3￣)</a><!--repeat11330623127--><a>╮(￣▽￣)╭</a><!--repeat11330623127--><a>_(:3」∠)_</a><!--repeat11330623127--><a>( ´_ゝ｀)</a><!--repeat11330623127--><a>←_←</a><!--repeat11330623127--><a>→_→</a><!--repeat11330623127--><a>(*_*)</a><!--repeat11330623127--><a>(>_>)</a><!--repeat11330623127--><a>(;¬_¬)</a><!--repeat11330623127--><a>("▔□▔)/</a><!--repeat11330623127--><a>(ﾟДﾟ≡ﾟдﾟ)!?</a><!--repeat11330623127--><a>Σ(ﾟдﾟ;)</a><!--repeat11330623127--><a>Σ( ￣□￣||)</a><!--repeat11330623127--><a>(´；ω；`)</a><!--repeat11330623127--><a>（/TДT)/</a><!--repeat11330623127--><a>(^・ω・^ )</a><!--repeat11330623127--><a>(｡･ω･｡)</a><!--repeat11330623127--><a>(●￣(ｴ)￣●)</a><!--repeat11330623127--><a>ε=ε=(ノ≧∇≦)ノ</a><!--repeat11330623127--><a>(´･_･`)</a><!--repeat11330623127--><a>(-_-#)</a><!--repeat11330623127--><a>（￣へ￣）</a><!--repeat11330623127--><a>(￣ε(#￣) Σ</a><!--repeat11330623127--><a>ヽ(`Д´)ﾉ</a><!--repeat11330623127--><a>（#-_-)┯━┯</a><!--repeat11330623127--><a>(╯°口°)╯(┴—┴</a><!--repeat11330623127--><a>←◡←</a><!--repeat11330623127--><a>( ♥д♥)</a><!--repeat11330623127--><a>Σ>―(〃°ω°〃)♡→</a><!--repeat11330623127--><a>⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄</a><!--repeat11330623127--><a>(╬ﾟдﾟ)▄︻┻┳═一</a><!--repeat11330623127--><a>･*･:≡(　ε:)</a><!--repeat11330623127--><a>(汗)</a><!--repeat11330623127--><a>(苦笑)</a><!--repeat11330623127--><!--repeat11330623127:end-->
            </div>
            
"""
 
allemoji = []
for emoji in re.findall('<a>.*?</a>', ss):
    emoji = emoji.replace('<a>','').replace('</a>','')
    allemoji.append(emoji)


def randEmoji():
    try:
        return (allemoji[ random.randint(0, len(allemoji)-1)])
    except Exception as e:
        print (e)
        return '-_-'
            
            
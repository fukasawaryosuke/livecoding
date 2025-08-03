# 1. pluck（プラック：弦っぽい音）
p1 >> pluck([0, 2, 4, 7], dur=0.5, amp=0.6)

# 2. bass（ベース音）
p2 >> bass([0, -1, -3, -5], dur=1, amp=0.8)

# 3. pads（パッド音）
p3 >> pads([0, 2, 4, 7], dur=4, sus=3, amp=0.4)

# 4. lead（リード音）
p4 >> lead([0, 3, 5, 7], dur=0.25, amp=0.7)

# 5. sinepad（サイン波のパッド）
p5 >> sinepad([0, 2, 5, 9], dur=2, amp=0.5)

# 6. play（ドラムパターン）
d1 >> play("x-o-")          # キック(x), スネア(o), ハイハット(-)

# 7. snappy（パーカッション系）
d2 >> snappy(P[0, 2, 4, 6], dur=0.25, amp=0.6)

# 8. noise（ノイズ系）
p6 >> noise([0, 3, 5], dur=1, amp=0.3)

# 9. blip（デジタル風音）
p7 >> blip([0, 4, 7], dur=0.5, amp=0.5)

# 10. コンビネーション例
p1 >> pluck([0, 2, 4, 7])
p2 >> bass([0, -2, -3, -5])
d1 >> play("x-o-")

# 11. 音色パラメータ調整例
p1 >> pluck([0, 2, 4, 7], cutoff=4000, slide=0.1)
p2 >> bass([0, -2, -3, -5], oct=3, amp=0.7)

# 12. パターン応用（スライドやランダム）
p1 >> pluck([0, 2, 4, 5] + PWhite(0, 2), dur=0.5, slide=0.05)

# 13. ドラムパターン拡張
d1 >> play("x-o-")
d2 >> play("  *  o ", sample=2, amp=0.5)

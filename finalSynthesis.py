Scale.default = 'harmonicMajor'
Clock.bpm = 100
Root.default = "D"

p1 >> space([0,2,4,8,3,5], delay=[0, 0, 0.5])

p2 >> prophet([3,2,5], delay=[0, 0, 0.5], amp=[0.3, 0.7, 0.5])

p2.dur=PSum(8,4)

p2.amp=0.5

p1.rate= PRand(4,10)

c1 >> soprano([0,2,5,3,0], dur=1/2, amp=0.5)

c1.dur = 1

p1.pan= [-1,0,1]

p1.dur = 1/2

b1 >> arpy([0,2,3,4], dur=1/2, amp=0.3)
p3 >> blip(dur=1/2).follow(b1) + (0, 2, 4)

p1.dur=1

p2.stop()

p3.pan= [-1,1]

p3.amp=0.5

b1.stop()

p3.rate= PRand(4,10)

d1 >> play("yh#*s~lcG++w[&&&&&&&&&]", amp=0.3, sus=0.2)

p3.stop()

p1.amp = 0.3

d2 >> play(P["x-o-o--"].bubble().stretch(15), amp=0.3)

d1.every(4, "shuffle")

c1.stop()

p4 >> marimba([2,5,7,3], dur=1/2, amp=1)

p_all.hpf = 500

p1.stop()

d3 >> glass([2,4,7,11], dur=1/4, amp=1.5)

d1.amp=1

c2 >> klank([0,1,3,5], dur=1/4, amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1])

c2.reverse()

d4.every(2, "shuffle")

c3 >> viola([3,2,0,2,3], dur=1/2, sus=1/4, amp=[0.8, 0.6, 0.5], pan=[-1,1])

d4 >> bell([2,0,4,2], dur=1/4, amp=0.2)

p4.stop()

d3.amp=0.1

d4.stop()

c2.stop()

d3.rate=(.8,1)

d4.amp=[0.5,0.3,0.2,0]

d3.stop()

c3.stop()

d1.amp=0.2

d2.stop()

d1.stop()


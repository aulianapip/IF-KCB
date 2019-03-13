from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars

ukuran = Relation()
warna = Relation()
gelap = Relation()

facts(ukuran, ("beruang", "besar"),
              ("gajah", "besar"),
              ("kucing", "kecil"))

facts(warna,  ("beruang", "cokelat"),
              ("kucing", "hitam"),
              ("gajah", "kelabu"))

fact(gelap, "hitam")
fact(gelap, "cokelat")

z = var()
ukuran_h = "kecil"
kecil =  run(0, z, ukuran(z, ukuran_h))
print("hewan berukuran "+ukuran_h+": ", kecil)

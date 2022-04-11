(define (problem lysak5x5)
        (:domain agent)
        (:objects p1 p2 p3 p4 p5
                  p6 p7 p8 p9 p10
                  p11 p12 p13 p14 p15
                  p16 p17 p18 p19 p20
                  p21 p22 p23 p24 p25
                  a1 a2 a3 a4 a5
                  a6 a7 a8 a9 a10
                  a11 a12 a13 a14 a15
                  a16 a17 a18 a19 a20
                  a21 a22 a23 a24)
        (:init
            (next-to p1 p2)
            (next-to p1 p6)
            
            (next-to p2 p1)
            (next-to p2 p3)
            (next-to p2 p7)
            
            (next-to p3 p2)
            (next-to p3 p4)
            (next-to p3 p8)
            
            (next-to p4 p3)
            (next-to p4 p5)
            (next-to p4 p9)
            
            (next-to p5 p4)
            (next-to p5 p10)
            
            (next-to p6 p1)
            (next-to p6 p7)
            (next-to p6 p11)
            
            (next-to p7 p6)
            (next-to p7 p2)
            (next-to p7 p8)
            (next-to p7 p12)
            
            (next-to p8 p7)
            (next-to p8 p3)
            (next-to p8 p9)
            (next-to p8 p13)
            
            (next-to p9 p8)
            (next-to p9 p4)
            (next-to p9 p10)
            (next-to p9 p14)
            
            (next-to p10 p9)
            (next-to p10 p5)
            (next-to p10 p15)
            
            
            (next-to p11 p6)
            (next-to p11 p12)
            (next-to p11 p16)
            
            (next-to p12 p11)
            (next-to p12 p13)
            (next-to p12 p7)
            (next-to p12 p17)
            
            (next-to p13 p12)
            (next-to p13 p14)
            (next-to p13 p8)
            (next-to p13 p18)
            
            (next-to p14 p13)
            (next-to p14 p15)
            (next-to p14 p9)
            (next-to p14 p19)
            
            (next-to p15 p14)
            (next-to p15 p10)
            (next-to p15 p20)
            
            
            (next-to p16 p17)
            (next-to p16 p11)
            (next-to p16 p21)
            
            (next-to p17 p16)
            (next-to p17 p18)
            (next-to p17 p12)
            (next-to p17 p22)
            
            (next-to p18 p17)
            (next-to p18 p19)
            (next-to p18 p13)
            (next-to p18 p23)
            
            (next-to p19 p18)
            (next-to p19 p20)
            (next-to p19 p14)
            (next-to p19 p24)
            
            (next-to p20 p19)
            (next-to p20 p15)
            (next-to p20 p25)
            
            
            (next-to p21 p16)
            (next-to p21 p22)
            
            (next-to p22 p21)
            (next-to p22 p23)
            (next-to p22 p17)
            
            (next-to p23 p22)
            (next-to p23 p24)
            (next-to p23 p18)
            
            (next-to p24 p23)
            (next-to p24 p25)
            (next-to p24 p19)
            
            (next-to p25 p24)
            (next-to p25 p20)
            
            (on a1 p25)
            (on a2 p4)
            (on a3 p2)
            (on a4 p23)
            (on a5 p8)
            (on a6 p12)
            (on a7 p3)
            (on a8 p17)
            (on a9 p9)
            (on a10 p22)
            (on a11 p10)
            (on a12 p24)
            (on a13 p5)
            (on a14 p19)
            (on a15 p14)
            (on a16 p6)
            (on a17 p21)
            (on a18 p7)
            (on a19 p15)
            (on a20 p13)
            (on a21 p11)
            (on a22 p18)
            (on a23 p20)
            (on a24 p1)
            (empty p16)
        )
        (:goal(and
            (on a1 p1)
            (on a2 p2)
            (on a3 p3)
            (on a4 p4)
            (on a5 p5)
            (on a6 p6)
            (on a7 p7)
            (on a8 p8)
            (on a9 p9)
            (on a10 p10)
            (on a11 p11)
            (on a12 p12)
            (on a13 p13)
            (on a14 p14)
            (on a15 p15)
            (on a16 p16)
            (on a17 p17)
            (on a18 p18)
            (on a19 p19)
            (on a20 p20)
            (on a21 p21)
            (on a22 p22)
            (on a23 p23)
            (on a24 p24)
            (empty p25)
        ))
)

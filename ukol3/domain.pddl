(define (domain agent)
    (:predicates
        (next-to ?x ?y)
        (on ?x ?y)
        (empty ?x)
        )
    (:action move
        :parameters(?from ?to ?what)
        :precondition (and
            (empty ?to)
            (on ?what ?from)
            (next-to ?from ?to)
        )
        :effect(and
            (on ?what ?to)
            (empty ?from)
            (not (empty ?to))
            (not (on ?what ?from))
        )
    )
)

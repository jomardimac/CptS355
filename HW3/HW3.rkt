(define (deepCount L)
  (cond ; start with a conditions:
    ((null? L) 0) ;if L is empty or not a list, return 0
    ((pair? (car L)) (+(deepCount(car L)) (deepCount (cdr L)))) ;if the element is a list, go through the list and run the function recursively
    (else ( + 1 (deepCount(cdr L)))) ;otherwise: add 1 to the count for one element: cdr
    )
  )

(define (nthElement n L) 
  (cond ;make a condition with base cases:
    ((null? L) "nothing" ) ; check to see when the list is empty
    ((= n 0 ) (car L)) ;if n = 0, take the first item in the list
    (else (nthElement (- n 1) (cdr L))) ; else decrement n and take all of L's items besides the first one
    )
  )

(define (repL n v L)
  (cond ;create conditions with base cases: 
    ((null? L) '()) ;no list, can't compile
    ((= n 0) (cons v (cdr L))) ;when going through n, when n is 0, found the index and cons the value to the cdr of L
    (else (cons(car L) (repL (- n 1) v (cdr L)))) ;recursion phase: add the car of L and recall repL n - 1 , same value, and cdr of L.
    )
  )

(define (range min step max)
  (cond ;create conditions with base cases:
    ((and (<= min max) (< step 0)) '()) ;if min <= max and step < 0, done
    ((and (> min max) (>= step 0)) '()) ;if min > max and step >= , done
    (else (cons min (range(+ min step) step max))) ;else: create a list with the min and recursively call range and update range's min to min+ step.
    )
  )

(define (merge2 L1 L2)
  (cond ;Set up base cases and recursions:
    ((null? L1) L2) ;whenever L1 is empty, check if L2 is and return it 
    ((null? L2) L1) ;whenever L2 is empty, check if L1 is and return it
    ((<= (car L1) (car L2)) (cons (car L1) (merge2 (cdr L1) L2))) ;compare the first items in both list. If L1's item is bigger, add item in front and recursively call merge again
    ((> (car L1) (car L2)) (cons (car L2) (merge2 L1 (cdr L2)))) ;compare the first item in both list. If L2's item is bigger, add that item in front of the list and recusively call merge again.        
    )
  )

;HelperFunction Fold:
(define (Fold func base L)
  (cond ;base cases, higher order function
    ((null? L) base) ;return the base if nothing on list
    (#t (func (car L) (fold func base (cdr L))) ) ;call the function to each item in L from left to right
    )
  )

(define (foldl fcombine basecase L)
  (cond
    ((null? L) basecase)
    (#t (foldl fcombine (fcombine (car L) basecase) (cdr L)))
    )
  )

;Helper Function Filter:
(define (filter pred L)
  (cond ;base cases, higher order function
    ((null? L) '()) ;return nothing when empty
    ((pred (car L)) (cons (car L) (filter pred (cdr L)))) ;Use the predicate / condition to each items in the list and return that true item in a list
    (else (filter pred (cdr L))) ;if false on the predicate, cut that item and call filter on the rest of the items
    )
  )


(define (mergeN Ln) (Fold ( (merge2 (car Ln) (car (cdr Ln)) ) '() Ln)) )
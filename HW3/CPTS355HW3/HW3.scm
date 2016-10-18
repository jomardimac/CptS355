;Name: Jomar Dimaculangan"
;CptS 355 - Scheme Lisp HW #3"
;WSU ID: 11422439"
;OS: Windows 10"

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
    ((and (>= min max) (>= step 0)) '()) ;if min > max and step >= , done
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
    (#t (func (car L) (Fold func base (cdr L)))) ;call the function to each item in L from left to right
    )
  )

;helpermerge is literally the same as merge2 but will be used in mergeN function
(define (helpermerge L1 L2)
  (cond
    ((null? L1) L2)
    ((null? L2) L1)
    ((<= (car L1) (car L2)) (cons (car L1) (helpermerge (cdr L1) L2)))
    ((> (car L1) (car L2)) (cons (car L2) (helpermerge L1 (cdr L2))))
    )
  )

;mergeN will take a list and merge two lists inside the list in order. 
(define (mergeN Ln) (Fold helpermerge '() Ln)) 

;matrix map will be another higher order function
(define (matrixMap f M)
  (cond ;create conditions, not going to be recursion but will exit out of the function when Matrix is emtpy
    ((null? M) '()) ;matrix is empty, exit
    ;will be similar to mymap functions. the matrixmap will require two lists inside a list so use cons.
    ((pair? M) (cons (map f (car M)) ;first list will need to return the first list from the matrix that has a function used on the list. if map is used, that will return the specified list
              (matrixMap f (cdr M)) ;second list will return the second list from the matrix that has the specified function used. again, use the higher order map function to the second list aka ((cdr matrix)))
              )
          )
    )
  )

;create a helper function that checks if the value is odd:
(define (isOdd x)
  (cond
    ((= 1( modulo x 2)) #t)
    (else #f)
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

;helper creating list of odd values:
(define (oddL L) (filter isOdd L))

;helper adding list:
(define (sum L) (fold (lambda (x y) (+ x y)) 0 L))

(define (avgOdd L)
  (oddL L) ;creates a list of odd values in an accepted list:
  (/ (sum (oddL L)) (deepCount (oddL L)));adds up the list, divides that sum to the length of list
  )



; TEST CASES:
(define (testDeepCount)
  (cond
  ((= (deepCount '(1 (2 3 4) (5) 6 7 (8 9) "10" 11)) 11)
  (= (deepCount '(1 ((2 3)) (4 5 6))) 6)
  (= (deepCount '(1 (2 3) 4 5 6 7)) 7) #t "deepCount passed")
  (else #f "deepCount failed")
  )
  )

(define (testnthEl)
  (cond
   ( (= (nthElement 3 '(1 2 3 4 (5) "6")) 4) 
   (equal? (nthElement 4 '(1 2 3 4 (5) "6")) '(5)) 
   (equal? (nthElement 5 '(1 2 3 4 (5) "6")) "6") #t "nthElement Passed")
   
   (else #f)
   )
  )
  

(define (testRepL)
  (cond
    ((equal? (repL 3 40 '(1 2 3 4 (5) "6")) '(1 2 3 40 (5) "6"))
    (equal? (repL 4 5 '(1 2 3 4 (5) "6")) '(1 2 3 4 5 "6"))
    (equal? (repL 2 "30" '(1 2 3 4 (5) "6")) '(1 2 "30" 4 (5) "6")) #t "repL passed")
    (else #f)
    )
  )

(define (testRange)
  (cond
    ((equal? (range 0 5 30) '(0 5 10 15 20 25))
     (equal? (range 5 -1 0) '(5 4 3 2 1))
     (equal? (range 3 3 27) '(3 6 9 12 15 18 21 24))
     (equal? (range 40 -5 0) '(40 35 30 25 20 15 10 5))#t "Range passed")
    (else #f)
    )
  )

(define (testMerge2)
  (cond
    ((equal? (merge2 '(4 6 7) '(3 5 7)) '(3 4 5 6 7 7))
     (equal? (merge2 '(1 7) '(2 5 7)) '(1 2 5 7 7))
     (equal? (merge2 '() '(3 5 7)) '(3 5 7))
     (equal? (merge2 '(4 5) '(1 2 8)) '(1 2 4 5 8))#t "Merge2 Passed")
    (else #f)
    )
  )

(define (testMergeN)
  (cond
    ((equal? (mergeN '()) '())
    (equal? (mergeN '((2 4 6) (1 4 5 6))) '(1 2 4 4 5 6 6))
    (equal? (mergeN '((2 4 6 10) (1 3 6) (8 9))) '(1 2 3 4 6 6 8 9 10))
    (equal? (mergeN '((1 2 3 10 30) (7 8 9 10 14 29))) '(1 2 3 7 8 9 10 10 14 29 30))
    #t "MergeN Passed")
    (else #f)
    )
  )


(define (testMatrixMap)
  (cond
    ((equal? (matrixMap (lambda (x) (* x x))  '((1 2) (3 4)) ) '((1 4) (9 16)))
    (equal? (matrixMap (lambda (x) (+ 1 x))  '((0 1 2) (3 4 5)) ) '((1 2 3) (4 5 6)))
    (equal? (matrixMap (lambda (x) (+ x x)) '((2 4 7) (10 20 30) (40 50 70))) '((4 8 14) (20 40 60) (80 100 140)))
    (equal? (matrixMap (lambda (x) (/ x x)) '((200 300 400) (12 13 14))) '((1 1 1) (1 1 1)) )
    #t "MatrixMap Passed")
    (else #f)
    )
  )

(define (testAvgOdd)
  (cond
    ((equal? (avgOdd '(1 2 3 4 5)) 3)
     (equal? (avgOdd '(1 2 4 6 8 10 12)) 1)
     (equal? (avgOdd '(1 3 6 8 10 11)) 5)
     #t "AvgOdd passed")
    (else #f)
    )
  )

;test a function
(define (testFunction f)
  (cond
    (f "Function passed") ;if the test function passes, prints function passed
    (else "Function Failed") ;else, function fails
    )
  )

;testAll:
"Name: Jomar Dimaculangan"
"CptS 355 - Scheme Lisp HW #3"
"WSU ID: 11422439"
"OS: Windows 10"
(testDeepCount)
(testnthEl)
(testRepL)
(testRange)
(testMerge2)
(testMergeN)
(testMatrixMap)
(testAvgOdd)
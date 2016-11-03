(* use "HW4.sml"; *);

(* revAppend, reverse, aux_filter and filter will be #1 question of HW4 *);

(* if the list appending is empty, return the list and recursion is done *);
(* if the function hasn't gone through the whole list, append the cdr of L, this wil go left to right*);
fun revAppend ([],L) = L 
| revAppend(x::rest,L) = revAppend(rest,x::L); 

(*reverse a list using the revAppend function: *);
fun reverse L = revAppend(L,[]); 


(* How tail recusion would work for filter. *)
(*fun aux_filter pred acc [] = acc
  | aux_filter pred acc (x::rest) = if pred x then x::(aux_filter pred acc rest)
	else (aux_filter pred acc rest);
*)
fun filter pred L =
let
	fun aux_filter pred acc [] = acc 
  	  | aux_filter pred acc (x::rest) = if pred x then x::(aux_filter pred acc rest)
	else (aux_filter pred acc rest)
(* In order for the function to work, there needs to be a function appending each elements to a list*)
 in
	reverse(reverse(aux_filter pred [] L))
end;

(*exist: *);

fun exists (L,[]) = false (*if the second list is done, the element doesn't exists*)
	| exists (x,y::resty) = if x = y then true  (* compare the first elements of the list, if they match, it does exist*)
						else exists (x,resty); (*go through the list recursively*)
						
(*listUnion*)

fun union (L1, []) = L1 (*base case: return the list when theres no more in the first list *)
	| union (L1,L2::rest) = if exists (L2,L1) = false then L2::union (L1,rest)  (*takes an element with a list, 
					if element isnt the same as car list, add the car to the list and recursively call it to go through the list*)
	else union (L1, rest); (*if the element is the same, go through the second list and skip the compared element*)

	
(*list difference*)
fun remove x [] = []
	| remove x (y::rest) = if x = y then remove (x rest)
	else y::(remove (x rest));

fun listDiff [] y = y
	| listDiff x [] = x
	| listDiff (x::r1) (y::r2) = if (exists (x, (y::r2))) then (listDiff r1 r2)
	else x::(listDiff r1 (remove y (y::r2)));


(*pairNright and helper functions*)
fun length [] = 0
	| length (x::rest) = length (rest) + 1;
	
fun pairAuxR N [] acc = [acc]
	| pairAuxR N (x::rest) acc = if (N > length (x::rest)) then 
	
	
(*merge sort helper unit lists*)
(*creates a list with each elements being in its own list*)
fun unitList [] = []
	| unitList (x::rest) = (x::[])::(unitList rest);
	
(*Merge two lists into one, not in order but compares the two cars in a lists. will be used for mergesort: *)
(*Will exactly be the same thing as Merge2 from the scheme homework*)
fun mergeLists (L1,[]) = L1
	| mergeLists ([],L2) = L2
	| mergeLists (L1::r1,L2::r2) = if L1 < L2 then L1::mergeLists (r1,L2::r2)
	else L2::mergeLists (L1::r1,r2);
	
fun merge [] = []
	| merge [x] = x
	| merge (x::y::rest) =  merge(mergeLists (x,y)::rest);

fun mergeSort [] = []
	| mergeSort (x) = merge (unitList (x));
	
fun mergeSort2 [] =[]
	| mergeSort2 (x) = if exists(x,y) then mergeSort2 (y::rest)
	else merge(unitList (x));

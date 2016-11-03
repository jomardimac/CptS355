(*Name: Jomar Dimaculangan*)
(*HW4*)

(*use "C:\\Users\\Jomar\\Documents\\CptS 355\\CptS355\\HW4\\HW4.sml";*)

(* revAppend, reverse, aux_filter and filter will be #1 question of HW4 *);

(* if the list appending is empty, return the list and recursion is done *);
(* if the function hasn't gone through the whole list, append the cdr of L, this wil go left to right*);
fun revAppend ([],L) = L 
| revAppend(x::rest,L) = revAppend(rest,x::L); 

(*reverse a list using the revAppend function: *);
fun reverse L = revAppend(L,[]); 

(*Need to see the length of list to compare with the int*)
fun length [] = 0
	| length (x::rest) = length (rest) + 1;
	
(*can use remove in many functions such as removing duplicates and list differences*)
fun myRemove x [] = []
	| myRemove x (y::rest) = if x = y then rest (*if the 'a value type is car of the list, return cdr*)
	else y::(myRemove x rest); (*if its not what it wants to remove, add that car in a list and go through rest of remove*)
	
fun map f [] = []
	| map f (x::rest) = (f x ):: (map f rest);
	
	
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
(*The type of exist is (''a * ''a list )->bool and not ('a * 'a list)-> bool because *)
fun exists (L,[]) = false (*if the second list is done, the element doesn't exists*)
	| exists (x,y::resty) = if x = y then true  (* compare the first elements of the list, if they match, it does exist*)
						else exists (x,resty); (*go through the list recursively*)
						
(*listUnion*)

fun listUnion (L1, []) = L1 (*base case: return the list when theres no more in the first list *)
	| listUnion (L1,L2::rest) = if exists (L2,L1) = false then L2::listUnion (L1,rest)  (*takes an element with a list, 
					if element isnt the same as car list, add the car to the list and recursively call it to go through the list*)
	else listUnion (L1, rest); (*if the element is the same, go through the second list and skip the compared element*)

	
(*list difference*)
fun listDiff [] y = y (*When there is nothing the first list, return second list*)
	| listDiff x [] = x (*When there is nothing in the second list, return first list*)
	(*if car of first list is already the second list, skip that car and call the rest of each list*)
	| listDiff (x::r1) (y::r2) = if (exists (x, (y::r2))) then (listDiff r1 r2)
	(*it is unique, then append that car from first list and recall the cdr and remove that item from the list (bag scheme)*)
	else x::(listDiff r1 (myRemove y (y::r2)));

(*Subsets*) 
(*from sakire's video*)
(*[1,2,3,4]
  add 1 to each sublist in subset[2,3,4] -> all subset of L
  add 2 to each sublist in subsets[3,4] -> all of subsets from [234]
  subset (x::rest) =  listunion (x added to subset of rest, subset of rest)*)

fun subsets [] = [[]]
	| subsets (x::rest) = 
	(*need to figure out how to add previous x's so lets make a function that adds it to a list*)
		let 
		(*append that item to the list*)
			fun putin(L1,[]) = []
			|	putin(L1,L2::r2) = listUnion([L1],L2)::putin(L1,r2)
			
		in 
			listUnion ( putin(x, subsets rest) , subsets rest)
		end;
(*pairNright and helper functions*)

(*Will be the auxilary function, be adding elements of the list backwards due to the acc::pair*)
fun pairAux N acc [] = [acc] (*if there is nothing left in the list, append list in that list*)
	(*if the length of acc is smaller than N, add the car to the the accumulator because it needs to be populated*)
	| pairAux N acc (x::rest) = if (length acc) < N then pairAux N (x::acc) rest 
	(*if it gets equal to the lenght of the accumulator, append the list of accumulator and recusively call pairaux with EMPTY accumulator*)
	else acc::(pairAux N [] (x::rest));

(*pairNLeft. Will need to reverse the auxilary function and the list passing in the auxilary function*)
fun pairNleft N [] = []
	| pairNleft N (x::rest) = reverse(pairAux N [] (reverse(x::rest)));
	
(*similar to pairNleft except that this one, you just have to reverse the separate lists in the list*)
fun pairNright N [] = []
	| pairNright N (x::rest) = 
		let 
			(*EXACTLY the same as the auxilary pair made for Left except it reverses the elements in the list inside the list*)
			fun pairAux N acc [] = [acc]
			| pairAux N acc (x::rest) = if (length acc) < N then pairAux N (x::acc) rest 
			(*this is the change, reverse the accumilator*)
			else reverse acc::(pairAux N [] (x::rest));
		in
			pairAux N [] (x::rest)
			
		end;
	
(*merge sort helper unit lists*)
(*creates a list with each elements being in its own list*)
fun unitList [] = []
	| unitList (x::rest) = ([x])::(unitList rest);
	
(*Merge two lists into one, not in order but compares the two cars in a lists. will be used for mergesort: *)
(*Will exactly be the same thing as Merge2 from the scheme homework*)
fun mergeLists (L1,[]) = L1
	| mergeLists ([],L2) = L2
	| mergeLists (L1::r1,L2::r2) = if L1 < L2 then L1::mergeLists (r1,L2::r2)
	else L2::mergeLists (L1::r1,r2);
	
(* Helped from Sakire's video. If list is empty, return empty
	if the item is in a list inside a list, return the list only. 
	if there are two lists in the tuple, merge them together. mergelists will then sort them*)
fun merge [] = []
	| merge [x] = x
	| merge (x::y::rest) =  merge(mergeLists (x,y)::rest);

(*will do the same thing as merge except it isn't in list*list aka tuple *)
fun mergeSort [] = []
	| mergeSort (x) = merge (unitList (x));

(*accepts a list type and creates the same list without duplicates *)
fun notEq x y = if x = y then false else true;
fun noDup [] = []
	| noDup (x::rest) = x::(noDup(filter (fn y => x <> y)rest)); (*appends car in the list. recursively
						calls filter to check if car DOESNT equal to as the next element of list and moves on to the rest of the list*)
	
(*calls mergesort with the duplicate items of the list and creates a non-duplicate one by  calling noDup*)
fun mergeSort2 [] =[]
	| mergeSort2 (x) = noDup(merge(unitList (x)));
	
	
	

	

	
(* TEST FUNCTIONS *)

fun myTest_filter(pred,L,R) = if (myfilter pred L) = R then true else false;
fun myTest_subset(L, R) = if (subsets L) = R then true else false;
fun myTest_pairNleft(n,L,R) = if (pairNleft n L) = R then true else false;
fun myTest_pairNright (n,L,R) = if (pairNright n L) = R then true else false;
fun myTest_exists(n,L,R) = if (exists(n,L) = R) then true else false;
fun myTest_listUnion(L,L2,R) = if (listUnion(L,L2) = R) then true else false;
fun myTest_listDiff(L,L2,R) = if (listDiff L L2 = R) then true else false;
fun myTest_mergeSort(L,L2,R) = if (mergeSort L L2 = R) then true else false;
fun myTest_mergeSort2(L,L2,R) = if (mergeSort2 L L2 = R) then true else false;	



	

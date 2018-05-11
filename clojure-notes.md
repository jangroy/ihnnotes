## Clojure Notes 

[Clojure Official Docs](https://clojure.org/reference/data_structures#Data%20Structures-Numbers.)

# Syntax
- Lisp like syntax
- Form refers to <i>valid code</i>
- <i>expressions</i> refer to Clojure forms

These literal representations are all valid forms:
```clj
1
"a string"
["a" "vector" "of" "strings"]
```
- Clojure uses whitespace to separate operands
```clj
(+ 1 2 3)
; => 6

(str "It was the panda " "in the library " "with a dust buster")
; => "It was the panda in the library with a dust buster"
```

- needs to have closing paranthesis to be a valid form

# Control Flow

- `if`, `do`, `when`

## `if`
general structure for an `if` expression:
```clj
(if boolean-form
  then-form
  optional-else-form)
```
```clj
(if true
  "By Zeus's hammer!"
  "By Aquaman's trident!")
; => "By Zeus's hammer!"

(if false
  "By Zeus's hammer!"
  "By Aquaman's trident!")
; => "By Aquaman's trident!"
```
You can also omit the `else` branch. If you do that and the Boolean expression is false, Clojure returns `nil`, like this:

```clj
(if false
  "By Odin's Elbow!")
; => nil
```

## `do`
lets you wrap up multiple forms in parentheses and run each of them
```clj
(if true
; do 
  (do (println "Success!")
      "By Zeus's hammer!")
  (do (println "Failure!")
      "By Aquaman's trident!"))
; => Success!
; => "By Zeus's hammer!"
```
## `when`
is like a combination of `if` and `do`, but with no `else` branch. Here’s an example:
```clj
(when true
  (println "Success!")
  "abra cadabra")
; => Success!
; => "abra cadabra"
```

## `nil`, `true`, `false`, `Truthiness`, `Equality`, and `Boolean` Expressions
Clojure has true and false values. `nil` is used to indicate no value in Clojure. You can check if a value is `nil` with the appropriately named `nil?` function:
```clj
(nil? 1)
; => false

(nil? nil)
; => true
```
- `nil and false` both represent logical falsiness

Clojure’s equality operator is `=`:
```clj
(= 1 1)
; => true

(= nil nil)
; => true

(= 1 2)
; => false
```
>`or` and `and`
```clj
(or false nil :large_I_mean_venti :why_cant_I_just_say_large)
; => :large_I_mean_venti

(or (= 0 1) (= "yes" "no"))
; => false

(or nil)
; => nil
```
- `or` returns `first truthy` or `last value`
- `and` returns `first falsey` or, if not values are falsey, `last truthy value`

## Naming Values with `def`
to bind a name to a value
```clj
(def failed-protagonist-names
  ["Larry Potter" "Doreen the Explorer" "The Incredible Bulk"])

failed-protagonist-names
; => ["Larry Potter" "Doreen the Explorer" "The Incredible Bulk"]
```
`binding a value` in CLJ = `assigning a value` in JS

- in the meantime, you should treat `def` as if it’s defining constants

# Data Structures

- All of Clojure’s data structures are `immutable`

## Numbers
- `int`, `float`, `ratio`
```clj
93
1.2
1/5
```

## Strings

- clojure doesn't have `string interpolation`
- It only allows concatenation via the `str` function:
```clj
(def name "Chewbacca")
(str "\"Uggllglglglglglglglll\" - " name)
; => "Uggllglglglglglglglll" - Chewbacca
```

## Maps

- similar to `dictionaries` or `hashes`
> empty map 
```clj
{}
```
>`:first-name` and `:last-name` are keywords
```clj
{:first-name "Charlie"
 :last-name "McFishwich"}
```

>`hash-map` function, to create a `map`
```clj
(hash-map :a 1 :b 2)
; => {:a 1 :b 2}
```

>`get`, looks up values in `maps`
```clj
(get {:a 0 :b 1} :b)
; => 1

(get {:a 0 :b {:c "ho hum"}} :b)
; => {:c "ho hum"}
```

>`get-in`, looks up values in nested `maps`
```clj
(get-in {:a 0 :b {:c "ho hum"}} [:b :c])
; => "ho hum"
```

Another way to look up a value in a `map` is to treat the `map` like a function with the key as its argument:
```clj
({:name "The Human Coffeepot"} :name)
; => "The Human Coffeepot"
```

## Keywords

- primarily used as `keys` in `maps`
```clj
(:a {:a 1 :b 2 :c 3})
; => 1
```

equivalent to
```clj
(get {:a 1 :b 2 :c 3} :a)
; => 1
```

default value with `get`
```clj
(:d {:a 1 :b 2 :c 3} "No gnome knows homes like Noah knows")
; => "No gnome knows homes like Noah knows"
```

## Vector
- `[]` Brackets
- end of vector
- array = vector
- 0-indexed collection
```clj
[3 2 1]
```
return 0th element of vector
```clj
(get [3 2 1] 0)
; => 3
```

Create vectors with `vector` function
```clj
(vector "creepy" "full" "moon")
; => ["creepy" "full" "moon"]
```

`conj` function, to add element to `end` of a vector
```clj
(conj [1 2 3] 4)
; => [1 2 3 4]
```

## Lists
- `()` Parentheses
- can't retrieve list elements with `get`
```clj
'(1 2 3 4)
; ' is a token symbol
; ` is another token that can cancel
; => (1 2 3 4)
```

`nth`, to retrieve element from a list
- it is slower than `get` to grab vector elements
- has to traverse all _n_ elements

```clj
(nth '(:a :b :c) 0)
; => :a

(nth '(:a :b :c) 2)
; => :c
```
create lists using `list` function
```clj
(list 1 "two" {3 4})
; => (1 "two" {3 4})
```
- lists are added to the BEGINNING of a list
```clj
(conj '(1 2 3) 4)
; => (4 1 2 3)
```
-  use a list if you need to easily add items to the beginning of a sequence or if you’re writing a macro.
- Otherwise use a vector.

## Sets
- collection of unique values`(no duplicates)`
  - hash sets, used more often
  - sorted sets
```clj
#{"kurt vonnegut" 20 :icicle}
```

`hash-set` function to create a set
```clj
(hash-set 1 1 2 2)
; => #{1 2}
```

`set` function
```clj
(set [3 3 3 4 4])
; => #{3 4}
```

`contains?` check for set membership, by using `get` or keyword as a function with set as its argument.

## Simplicity

```
It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures.
—Alan Perlis
```

# Functions

Lisp functions by explaining the following:

- Calling functions
- How functions differ from macros and special forms
- Defining functions
- Anonymous functions
- Returning functions

## Calling Functions

- syntax: 

`opening parenthesis`, `operator`, `operands`, `closing parenthesis`. 
> `(+ 1 2 3 4)`

- numbers and strings aren't functions
```clj
(1 2 3 4)
("test" 1 2 3)
```

`map`
- not to be confused with `map data structure {}`
- creates a new list, not vector
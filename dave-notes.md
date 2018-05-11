> data > functions > macro

```clj
(->> [1 2 3] 
     (map inc))
=> (2 3 4)
(->> [1 2 3] 
     (map inc))
=> (2 3 4)
(->> [1 2 3]
     (map inc))
=> (2 3 4)
(doseq [x [1 2 3]]
  (println "x:" x))
x: 1
x: 2
x: 3
=> nil
(doseq [x '(1 2 3)]
  (println "x:" x))
x: 1
x: 2
x: 3
=> nil
(conj [1 3 5] :a)
=> [1 3 5 :a]
(conj '(1 2 3) :a)
=> (:a 1 2 3)
(->> [1 2 3]
     (mapv inc))
=> [2 3 4]
(->> [1 2 3]
     (map inc))
=> (2 3 4)
(->> [1 2 3]
     (map inc))
=> (2 3 4)
(->> [1 2 3]
     (map inc))
=> (2 3 4)
(->> [1 2 3]
     (map inc))
=> (2 3 4)
(->> [1 2 3]
     (map inc)
     (into []))
=> [2 3 4]
(defn my-fun [x]
  (inc x))
=> #'clojure-noob.core/my-fun
(my-fun 5)
=> 6
(defn my-fun [x y]
  (+ x y))
=> #'clojure-noob.core/my-fun
(my-fun 5 6)
=> 11
(1 5 6)
ClassCastException java.lang.Long cannot be cast to clojure.lang.IFn  clojure-noob.core/eval1464 (form-init351963221801696558.clj:1)
'(1 5 6)
=> (1 5 6)
(let [x 10
      l '(1 2 3 x)]
  l)
=> (1 2 3 x)
(let [x 10
      l `(1 2 3 x)]
  l)
=> (1 2 3 clojure-noob.core/x)
(let [x 10
      l `(1 2 3 ~x)]
  l)
=> (1 2 3 10)
(let [name "my name"]
  `(:create-user {:name ~name}))
=> (:create-user {:name "my name"})
(identity :a)
=> :a
(->> [1 2] (map identity))
=> (1 2)
(->> {:a "aval"
      :b "bval"}
     (map identity))
=> ([:a "aval"] [:b "bval"])
(->> [[:a "val"]
      [:b "bval"]]
     (into {}))
=> {:a "val", :b "bval"}
(into {} [[:a "val"]
          [:b "bval"]])
=> {:a "val", :b "bval"}
(->> {:a "aval" :b "bval"}
     (map identity))
=> ([:a "aval"] [:b "bval"])
(->> [1 2 3]
     (map (fn [x] (inc x))))
=> (2 3 4)
(->> {:a "aval"}
     (map (fn [[k v]] [k v])))
=> ([:a "aval"])
(->> {:a "aval"}
     (map (fn [[k v]] [k v]))
     (into {}))
=> {:a "aval"}
(->> {:a "aval"}
     (map (fn [[k v]] [k (str "modified-" v)]))
     (into {}))
=> {:a "modified-aval"}
```
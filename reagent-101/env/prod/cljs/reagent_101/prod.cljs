(ns reagent-101.prod
  (:require [reagent-101.core :as core]))

;;ignore println statements in prod
(set! *print-fn* (fn [& _]))

(core/init!)

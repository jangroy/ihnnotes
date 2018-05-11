(ns ^:figwheel-no-load reagent-101.dev
  (:require
    [reagent-101.core :as core]
    [devtools.core :as devtools]))

(devtools/install!)

(enable-console-print!)

(core/init!)

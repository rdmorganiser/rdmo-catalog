# Über den JKI-BLE Fragenkatalog
# Ziel und Zweck

Der JKI-BLE Fragenkatalog wurde vom Team FDM am Julius Kühn-Institut (JKI) entworfen. Feedbacks und Anregungen vom Team Forschungsdaten-Services TU-Darmstadt und von der Hochschule Geisenheim wurden bei der Entwicklung berücksichtigt. Der Fragenkatalog soll das manuell auszufüllende Word-Template des Fördergebers BLE (Bundesanstalt für Landwirtschaft und Ernährung) ersetzten. Der zu dem Fragenkatalog gehörende View orientiert sich beim Layout an dem Word-Template der BLE.
Inhaltlich zeichnet sich der Katalog durch wenig Freitext und viele Auswahloptionen aus. Er ist so gestaltet, dass er sich von Forschenden, die keine tiefgreifende FDM-Kenntnisse haben, ausfüllen lässt. Bei Fragen, die sich mit dem Einsatz von Auswahlmenüs beantworten lassen, sind diese in mehreren Fällen auf die Bedarfe des JKI ausgelegt. Der Katalog ist auf Deutsch und Englisch verfügbar.



## Einrichtung des Fragenkatalogs

Als Voraussetzung müssen die vom RDMO-Projekt bereitgestellten Standard-Attribute und -Optionen in die eigene RDMO-Instanz importiert worden sein. Diese können unter https://github.com/rdmorganiser/rdmo-catalog/tree/master/rdmorganiser heruntergeladen werden.

Der JKI-BLE Fragenkatalog benötigt darüber hinaus zusätzliche Attribute, Optionen und Bedingungen, die sich in den Dateien ble_domain.xml, ble_options.xml und ble_conditions.xml befinden. Zudem sollte Autosave auf Ihrer RDMO-Instanz aktiviert sein, damit aufgrund von Bedingungen (nicht) relevante Fragen direkt ein- /ausgeblendet werden können. Ansonsten geschieht dies erst nachdem auf den „Sichern“-Button geklickt wurde. Ein Beispiel ist im Abschnitt Publikation unter -> Verfügbarmachung zu sehen. Wenn die Frage „Sollen die Daten aus dieser Datenkategorie publiziert werden?“ mit einer der Nein-Antworten beantwortet wird, dann sind die darunter folgenden Fragen überflüssig. Sie werden erst ausgeblendet, wenn auf „Sichern“ geklickt wird. 

**rdmo/core/Settings.py PROJECT_QUESTIONS_AUTOSAVE = True**

Folgende Dateien müssen vor dem Import des eigentlichen JKI-BLE-Fragenkatalogs (jki_questions.xml) in der folgenden Reihenfolge in die eigene RDMO-Instanz importiert werden:

1.	ble_domain.xml
2.	ble_options.xml
3.	ble_conditions.xml

Erst im Anschluss kann der Fragenkatalog (ble_questions.xml) korrekt importiert werden. Wird dieser versehentlich zuerst importiert, werden die Optionen und Bedingungen nicht verknüpft und der Katalog funktioniert nicht richtig. In diesem Fall hilft es, den JKI-BLE-Fragenkatalog zu löschen und, nach dem Import der oben genannten Dateien, neu zu importieren.

## Einrichtung der Views

Zuerst müssen die Dateien „ble_view_de“ und „ble_view_en.xml“ importiert werden. Damit das Layout ordnungsgemäß nach MS Word exportiert werden kann, empfiehlt sich der Export als HTML. Nachdem sich im Browser der View geöffnet hat, Rechtsklick und „Seite speichern unter …“ wählen. Die gespeicherte Datei in Word zur Durchsicht bzw. Nachbearbeitung öffnen. Final das Dokument aus Word heraus als docx oder pdf abspeichern.
Wenn Änderungen im Fragenkatalog, in Optionen oder Bedingungen vorgenommen werden, dann müssen ggf. die Views angepasst werden. 

## Rechtliches und Kontakt

Der Katalog steht unter der Lizenz CC0 zur freien Verfügung. Bei Fragen und Anmerkungen wenden Sie sich bitte an fdm@julius-kuehn.de .
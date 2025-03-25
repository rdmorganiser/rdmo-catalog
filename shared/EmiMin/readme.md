# Über das Projekt EmiMin (Emissionsminderung in der Nutztierhaltung)

## Thema und Zielsetzung

Im Rahmen des Verbundvorhabens „Emissionsminderung Nutztierhaltung ‐ Einzelmaßnahmen“ (EmiMin)
werden ausgewählte, auf dem Markt verfügbare verfahrensintegrierte, baulich‐technische Maßnahmen
zur Emissionsminderung in Ställen der Nutztierhaltung hinsichtlich ihrer Wirksamkeit unter deutschen
Produktionsbedingungen untersucht und Emissionsminderungsgrade bzw. Emissionsfaktoren für Ammoniak,
Geruch und Methan abgeleitet. Die Untersuchungen erfolgen auf Grundlage des international abgestimmten
VERA‐Testprotokolls und umfassen Maßnahmen und Maßnahmenkombinationen sowie deren
Optimierung in zwangsgelüfteten Ställen der Zucht‐ und Mastschweinehaltung, bei frei gelüfteten Ställen
mit Auslauf für die Mastschweinehaltung sowie in frei gelüfteten Milchviehställen. Für die Untersuchung
der Emissionsminderung bei Ausläufen von Ställen wird die Messmethodik mit künstlichem Tracergas entwickelt
und validiert.

Die Ergebnisse des Verbundvorhabens und die Forschungsdaten selbst werden frei zugänglich im Rahmen
einer Forschungsdatenbank dokumentiert und der Fachöffentlichkeit für weitere Forschungszwecke zur
Verfügung gestellt. Die Datenaufbereitung und Veröffentlichung wird projektbegleitend mit einem Datenmanagementplan
unterstützt.

## Ziele des Projektes

Das Vorhaben ergänzt das von der Landwirtschaftlichen Rentenbank geförderte EmiDaT‐Projekt („Ermittlung
von Emissionsdaten für die Beurteilung der Umweltwirkungen der Nutztierhaltung – Verbundprojekt
Emissionen“, Laufzeit 2014‐2018), bei dem Emissionsdaten von Nutztierställen ohne den Einsatz von Emissionsminderungsmaßnahmen
ermittelt werden, die als Referenzwerte zur Beurteilung der Nutztierhaltung
herangezogen werden können.

Folgende Maßnahmen zur Minderung der Emissionen werden untersucht:

### 1. Schweinehaltung

‐ Einsatz von Ureaseinhibitoren zur Oberflächenbehandlung in der Mastschweinehaltung
‐ Einsatz von Systemen zur Güllekühlung und Verkleinerung der Oberfläche von Güllekanälen jeweils
als Einzelmaßnahme und in Kombination bzw. optimierte Maßnahme
‐ Einsatz einer Kot‐Harn‐Trennung mit Unterflurschieber bei der besonders tiergerechten Auslaufhaltung
von Schweinen (perforierter Mistbereich) als Einzelmaßnahme und in Kombination mit einer
Oberflächenbehandlung (Ureaseinhibitor) sowie Einsatz von Ureaseinhibitoren zur Oberflächenbehandlung
bei planbefestigten Ausläufen; hierzu wird eine spezielle Messmethodik entwickelt
und validiert.

### 2. Milchviehhaltung

‐ Einsatz modifizierter, emissionsarmer planbefestigter Böden im Laufbereich
‐ Einsatz modifizierter, emissionsarmer perforierter Böden im Laufbereich
Grundlage zur Verifizierung der Minderungsleistungen ist wie bei EmiDaT das international abgestimmte
VERA‐Testprotokoll für Haltungs‐ und Managementsysteme, um zu gewährleisten, dass die Ergebnisse
international vergleichbar sind und anerkannt werden.

Im Fokus stehen die gasförmigen Emissionen (Ammoniak, Methan und Geruchsstoffe). Partikel‐ und Bioaerosolemissionen
werden nicht mit untersucht, da keine Effekte der zu untersuchenden Minderungsmaßnahmen
auf diese Emissionen zu erwarten sind.

Für die Forschungsdaten und ‐Ergebnisse werden in der KTBL‐Datenbank die erforderlichen Datenstrukturen
sowie Verarbeitungsprozesse und Auswertungsoberflächen geschaffen. Die Datenaufbereitung und
Veröffentlichung im Fachrepositorium Lebenswissenschaften (FRL) wird durch einen projektbegleitenden,
softwaregestützten Datenmanagementplan unterstützt. Das FRL wird um die erforderlichen Strukturen
zur Datenhaltung und ‐beschreibung erweitert.

Damit werden alle Untersuchungsdaten und ‐Ergebnisse des Verbundvorhabens der interessierten
Fachöffentlichkeit für spätere Forschungszwecke zur Verfügung gestellt. Die Plattform steht auch für Daten
aus anderen laufenden (z. B. EmiDaT) und geplanten Projekten offen.

## Einrichtung der Fragenkataloge

Im Rahmen von EmiMin sind 2 Fragenkataloge entstanden. Einer dient der Erstellung eines Datenmanagementplans für die Projektkoordination (publisso_terms4life_emimin_lead_V1_questions.xml). Der andere Fragenkatalog richtet sich an die Teilprojekte, welche in den Ställen emissionsmindernde Maßnahmen erforschen (publisso_terms4life_emiminV1_questions.xml).

Als Voraussetzung müssen die vom RDMO-Projekt bereitgestellten Standard-Attribute und -Optionen in die eigene RDMO-Instanz importiert worden sein. Diese können unter [Link](/rdmorganiser) heruntergeladen werden.

Unabhängig davon, ob nur ein Fragenkatalog alleine, oder beide zusammen eingerichtet werden soll, bedarf es Anpassungen an der Domäne, den Optionen und Bedingungen. Die dafür notwendigen Erweiterungen befinden sich in den Dateien publisso_terms4life_emiminV1_domain.xml, publisso_terms4life_emiminV1_options.xml und publisso_terms4life_emiminV1_conditions.xml.

Damit die einzelnen Verknüpfungen zwischen den bereits bestehenden und den neu zu importierenden Attributen ohne Fehler angelegt werden können, muss die folgende Reihenfolge beim Import eingehalten werden:

1. publisso_terms4life_emiminV1_domain.xml
2. publisso_terms4life_emiminV1_options.xml
3. publisso_terms4life_emiminV1_conditions.xml

Wird die Reihenfolge nicht eingehalten, werden die EmiMin-Kataloge nicht funktionieren. Dann müssen die Verknüpfungen entweder manuell nachgetragen werden, oder (was wesentlich einfacher sein sollte) die bereits importierten EmiMin-Dateien werden gelöscht und anschließend in der richtigen Reihenfolge importiert.

Hinweis: Diese Schritte sind nur einmal notwendig und fallen nicht pro Fragenkatalog neu an! Sollte also z.B. nur ein Fragenkatalog importiert werden und erst zu einem späteren Zeitpunkt der Zweite, müssen die vorher erläuterten Schritte nicht noch einmal durchlaufen werden.

## Rechtliches und Kontakt

Beide Kataloge stehen unter der Lizenz CC0 zur freien Verfügung.
Bei Fragen und Anmerkungen wenden Sie sich bitte an forschungsdaten@zbmed.de.

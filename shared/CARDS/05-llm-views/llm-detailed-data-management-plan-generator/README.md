# LLM Generator: Ausführlicher Datenmanagementplan

Diese Ansichtsdatei (View) für den Research Data Management Organizer (RDMO) ermöglicht die KI-gestützte Erstellung eines ausführlichen Entwurfs für einen Forschungsdatenmanagementplan (DMP).

**Wichtige Voraussetzung:** Die Ansicht funktioniert nur in einer RDMO-Instanz, in der das [RDMO-LLM-Plugin](https://github.com/rdmorganiser/rdmo-plugins-llm-views) installiert und konfiguriert ist. Zusätzlich ist eine Anbindung an einen kompatiblen LLM-Provider erforderlich (in der Regel über einen API-Schlüssel).

## Allgemeine Informationen

**Autor:innen:** Aleksandra Trifonova (ORCID: 0009-0006-1539-8594), Britta Steinke (ORCID: 0000-0001-6816-5168), Jochen Klar (ORCID: 0000-0002-5883-4273)

**Stand / letzte Aktualisierung:** 10.11.2026

**Version:** 01

**Lizenz:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

**Zitiervorschlag:** Trifonova, A., Steinke, B. & Klar, J. (2026). *LLM Generator: Ausführlicher Datenmanagementplan – RDMO-Ansicht zur KI-gestützten Erstellung eines ausführlichen Forschungsdatenmanagementplans* (Version 01). [Repository-Link ergänzen]

## 1. Inhalt und Zweck

Die Ansicht wurde im Rahmen des durch die Berlin University Alliance geförderten Projekts *Collaboratively Advancing Research Data Support (CARDS)* (2024–2026) entwickelt. Sie erstellt mithilfe eines Large Language Models (LLM) einen Entwurf für einen ausführlichen Datenmanagementplan auf Grundlage der im RDMO-Projekt hinterlegten Informationen.

Der Prompt gibt eine feste Gliederung vor und enthält Vorgaben zu Inhalt, Sprache, Stil und Formatierung.

Der DMP umfasst die folgenden Themenbereiche:

- Administrative Angaben und Projektbeschreibung
- Beschreibung neu erhobener und wiederverwendeter Daten
- Technische Datenmerkmale und Verarbeitungsschritte
- Umgang mit Forschungsdaten
- Rechtliche Aspekte
- Verantwortlichkeiten und Ressourcen

Das Ergebnis dient als erster Entwurf und muss vor seiner Verwendung fachlich geprüft, ergänzt und gegebenenfalls im Team abgestimmt werden.

## 2. Technische Voraussetzungen

Für die Nutzung sind erforderlich:

- eine funktionsfähige RDMO-Instanz
- das installierte und konfigurierte [RDMO-LLM-Plugin](https://github.com/rdmorganiser/rdmo-plugins-llm-views)
- eine Anbindung an einen kompatiblen LLM-Provider (in der Regel über API-Schlüssel)
- Administrationsrechte zum Importieren und Einrichten der Ansicht.

Die Installation des Plugins und die Konfiguration des LLM-Dienstes sind in der [Plugin-Dokumentation](https://github.com/rdmorganiser/rdmo-plugins-llm-views/blob/main/README.md) beschrieben.

**Verwendetes Sprachmodell:** Die Ansicht wurde mit dem über Chat AI der Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen (GWDG) bereitgestellten Modell `meta-llama-3.1-8b-instruct` entwickelt und getestet. Dieses Modell ist auch in der XML-Datei angegeben.

**Hinweis zur Nachnutzung:** Da sich Sprachmodelle schnell weiterentwickeln, wird empfohlen, bei der Übernahme der Ansicht die Modellkonfiguration zu überprüfen und gegebenenfalls ein aktuelleres Modell zu verwenden. Je nach Konfiguration des Plugins können dafür Änderungen an der XML-Datei und/oder an den Einstellungen der RDMO-Instanz erforderlich sein.

## 3. Nutzung und Import in RDMO

1. Die technischen Voraussetzungen erfüllen.
2. Mit Administrationsrechten in RDMO anmelden.
3. Die XML-Datei über die RDMO-Managementoberfläche importieren.
4. Die Ansicht und ihre Modellkonfiguration überprüfen und mit einem Testprojekt erproben.
5. Die Ansicht für die vorgesehenen Nutzer:innen freigeben.
6. Im gewünschten RDMO-Projekt die Ansicht **„Datenmanagementplan"** aufrufen und den generierten Entwurf überprüfen.

Die Ansicht ist **nicht an einen bestimmten RDMO-Fragenkatalog gebunden**. Sie verwendet den gesamten RDMO-Projektexport als Kontext und greift nicht gezielt auf einzelne katalogspezifische Attribute zurück. Dadurch kann sie grundsätzlich mit unterschiedlichen Fragenkatalogen verwendet werden. Welche Informationen in der Ausgabe berücksichtigt werden können, hängt jedoch von den im jeweiligen Projekt vorhandenen Angaben ab.

Der Prompt fordert das LLM auf, ausschließlich die bereitgestellten Projektinformationen zu verwenden, fehlende Angaben mit `[bitte ergänzen]` zu kennzeichnen und die vorgegebene Gliederung einzuhalten. Die Ausgabesprache soll der in RDMO ausgewählten Sprache entsprechen. 

## 4. Bekannte Einschränkungen

Die Ansicht wurde mit der oben genannten Modellkonfiguration erprobt. Dabei wurden Einschränkungen festgestellt, die sich durch Anpassungen des Prompts bislang nicht vollständig beheben ließen:

- **Inhaltliche Zuverlässigkeit:** Die Ausgabe kann fehlerhafte, unvollständige, widersprüchliche oder nicht durch die Eingaben gedeckte Aussagen enthalten. Halluzinationen lassen sich trotz entsprechender Prompt-Anweisungen nicht vollständig ausschließen.
- **Abhängigkeit von Eingabedaten:** Unvollständige oder unklare Angaben im RDMO-Projekt können die Qualität des erzeugten Textes beeinträchtigen.
- **Einhaltung von Anweisungen:** Vorgaben zu Sprache, Umfang, Struktur und Formatierung werden teilweise nicht eingehalten. Beobachtet wurden unter anderem die Vermischung deutscher und englischer Textteile, fehlerhafte Überschriftenebenen sowie unerwünschte Code- und Formatierungsfragmente.
- **Reproduzierbarkeit:** Eine erneute Generierung kann auch bei unveränderten Eingaben zu einem anderen Ergebnis führen. Bereits erzeugte Texte sollten daher bei Bedarf separat gesichert werden.
- **Generierungsdauer:** Die Ausgabe dauerte in den bisherigen Tests in der Regel bis zu etwa 60 Sekunden. Abhängig vom LLM-Dienst und seiner Auslastung kann die Verarbeitung länger dauern. In der getesteten Konfiguration wurde ein Timeout von 300 Sekunden verwendet.
- **Modellabhängigkeit:** Die Qualität und Zuverlässigkeit hängen wesentlich vom eingesetzten Sprachmodell ab. Andere oder neuere Modelle können abweichende Ergebnisse liefern; ein systematischer Modellvergleich wurde bislang nicht durchgeführt.

**Die generierten Dokumente sind ausschließlich als erste Entwürfe zu verstehen.** Sie müssen vor der Verwendung vollständig geprüft und überarbeitet werden.

## 5. Hinweise zur Datenverarbeitung

Bei der Generierung werden Informationen aus dem RDMO-Projektkontext an das konfigurierte Sprachmodell beziehungsweise den angebundenen LLM-Dienst übermittelt.

Welche Daten verarbeitet werden und welche technischen, organisatorischen und datenschutzrechtlichen Rahmenbedingungen gelten, hängt von der Konfiguration der jeweiligen RDMO-Instanz, des Plugins und des verwendeten LLM-Dienstes ab.

Vor einer produktiven Nutzung müssen die betreibenden Einrichtungen die geltenden Anforderungen an den Datenschutz prüfen.
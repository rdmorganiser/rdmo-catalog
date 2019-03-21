---
name: New/Edit Question
about: Create a report to help us improve a question in RDMO catalog UA Ruhr. Provide suggestions for a new RDMO question or for updating an existing one.
title: 'New/Edit Question: TYPE PATH URI HERE
labels: '"Question Issue"'

---

**Describe the request **
A clear and concise description of what the request is.


**Precise details **
Provide details what needs to be changed for an existing question.
When requesting a new question provide `question text` (mandatory) and, if possible, the other content and parameters, too (optional).    
- [ ] uri
- [ ] key
- [ ] path
- [ ] questionset
  - [ ] position in set
- [ ] question text (en and ger)
- [ ] help text (en and ger)
- [ ] answer
  - [ ] widget type
  - [ ] value type
  - [ ] max/min, step and unit
- [ ] optionset
- [ ] condition
- [ ] attribute

** Original setting or content ** 
What is the current content or setting e.g. 

```xml
 <text lang="en">Projektlaufzeit (Monate)</text>
```

** Proposed setting or content ** 
What should it look like in the new version, e.g. 
```xml
 <text lang="en">Projektlaufzeit </text>
```   

**Example of a question in xml **
```xml
<question dc:uri="https://rdmorganiser.github.io/terms/questions/rdmo/general/project-schedule-schedule/project_duration">
	  <uri_prefix>https://rdmorganiser.github.io/terms</uri_prefix>
	  <key>project_duration</key>
	  <path>ua-ruhr/general/project-schedule-schedule/project_duration</path>
	  <dc:comment/>
	  <attribute dc:uri="https://rdmorganiser.github.io/terms/domain/project/schedule/project_duration"/>
	  <questionset dc:uri="https://rdmorganiser.github.io/terms/questions/rdmo/general/project-schedule-schedule"/>
	  <is_collection>False</is_collection>
	  <order>3</order>
	  <help lang="en"/>
	  <help lang="de"/>
	  <text lang="en">Projektlaufzeit (Monate)</text>
	  <text lang="de">Projektlaufzeit (Monate)</text>
	  <verbose_name lang="en"/>
	  <verbose_name lang="de"/>
	  <verbose_name_plural lang="en"/>
	  <verbose_name_plural lang="de"/>
	  <widget_type>textarea</widget_type>
	  <value_type>text</value_type>
	  <maximum/>
	  <minimum/>
	  <step/>
	  <unit/>
	  <optionsets/>
	  <conditions/>
</question>
```


**Additional context**
Add any other context about the problem here.

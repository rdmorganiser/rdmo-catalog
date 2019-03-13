---
name: Change question request
about: Create a report to help us improve the question in rdmo catlog UA Ruhr 
title: 'Request to change rdmo question: xyz'
labels: '"change request"'
assignees: ''

---

**Describe the request **
A clear and concise description of what the request is.


**Precise details **
In the folowing provide details what needs to be changed.  
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

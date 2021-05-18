# R script and tables for the localisation of RDMO catalogues and optionsets

This folder contains tools which allow adding new languages to the RDMO XML files (presently catalogues and optionsets).

The code is still "work in progress".

Suggested procedure:

1. Open the R script. If necessary, adjust the file names and paths.
2. Add the new language to all relevant positions in the script (in particular after each occurrence of `Liste_it`, `Übersetzung_it`, `IT`).
3. Run the first part of the script. This will extract all text chunks (titles, question texts, help texts, verbose names) as well as their XML path into a TSV file.
4. Open the TSV file with a spreadsheet software or an advanced text editor. Add a new column with the new language.
5. Translate the text into the new language. You may sort the table, provided you sort it back at the end. Don't delete the empty rows.
6. Run the second part of the script. This will add the nodes in the new language as siblings to the existing ones in the XML file.
7. Check the resulting XML file for consistency using an XML editor.
8. Upload the resulting XML file to your RDMO instance (and possibly as a pull reqest here on GitHub).

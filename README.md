# EasyEDA
 Python scripts for EasyEDA

JLCPCB.com is a quite nice EMS, especially for prototypes made with the free layout program EasyEDA. The service is quite inexpensive due to a number of "basic components", for which no setup fee is charged. Unfortunately, these parts change frequently. 

These tools help by updating the BOM.

# Extract_Basic_Parts
JLCPCB provides a ![list of parts](https://jlcpcb.com/componentSearch/uploadComponentInfo), they mount on boards. The script extracts all basic parts from that list and adds columns with key values. The result is saved to a file with "_BasicParts.csv" at the end ![(example)](JLCPCB-SMT-Parts-Library(20211211)_BasicParts.csv).

Usage:
Extract_Basic_Parts <name_of_downloaded_list.csv>

Annotation:
If a coding error is rised, plese open the csv file first (e. g. with LibreOffice) and safe it again using utf-8 coding.

# Parse_BOM
This script optimizes a BOM from EasyEDA with the help of the list of basic parts generated above and a crossref list ![(example)](CrossList.csv).

Usage:
Parse_BOM <list_of_basic_parts_as_generated_before.csv> <BOM_from_EasyEDA.csv> <optional: crosslist.csv>

Annotation:
If a coding error is rised, plese open the BOM csv file first (e. g. with LibreOffice) and safe it again using utf-16 coding.

Examples of modified BOMs can be found in my AgOpenGPS project here (V2.0 and V3.0).



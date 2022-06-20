This README.txt file was generated on 2020_05_19 by Ariane Thomas and updated on 2022_06_20 by Ariane Thomas

-------------------
GENERAL INFORMATION
-------------------

Title of Dataset: PCD Clade

Author Information (Name, Institution, Address, Email)

	Principal Investigator:
		Ariane Thomas
		University of Iowa
		114 Macbride Hall
		Iowa City, IA 
		ariane-thomas@uiowa.edu

	Associate or Co-investigator:
		Andrew Kitchen
		University of Iowa
		20 Macbride Hall
		Iowa City, IA
		andrew-kitchen@uiowa.edu

	Alternate Contact(s):None

Date of data collection: 2020_02_01 to 2020_06_01

Geographic location of data collection: Iowa City, Johnson County, IA, USA 

Information about funding sources or sponsorship that supported the collection of the data:
Iowa Recruitment Fellowship

--------------------------
SHARING/ACCESS INFORMATION
-------------------------- 

Licenses/restrictions placed on the data, or limitations of reuse:
	NONE

Recommended citation for the data:
	Thomas and Kitchen. 2020. Indigenous North American Dog Sequences. 

Citation for and links to publications that cite or use the data:
	Ní Leathlobhair, Máire, Angela R. Perri, Evan K. Irving-Pease, Kelsey E. Witt, Anna Linderholm, James Haile, Ophelie Lebrasseur, et al. “The Evolutionary History of Dogs in the Americas.” Science 361, no. 6397 (July 6, 2018): 81–85. https://doi.org/10.1126/science.aao4776.


Links to other publicly accessible locations of the data: N/A

Links/relationships to ancillary or related data sets: N/A


--------------------
DATA & FILE OVERVIEW
--------------------

File list (filenames, directory structure (for zipped files) and brief description of all data files):
	File names are formatted as follows: Dog[mtDNA sequence length]_[starting base position]_to_[ending base position] for job files (.sh) for high performance computing and for Bayesian phylogeny files (.xml). Treeannotator files have an .MCC.trees extension.

Relationship between files, if important for context:  
		Used code in filesforfunction.py to create a list of commands (see filesfor1000.txt for an example) then used that output to run generate_job_files.py to create .sh files and pull_sliding_genomes.py to create xml files of a specified length using a fasta file.

Additional related data collected that was not included in the current data package: N/A

If data was derived from another source, list source: Fasta file generated from Ni Leathlobhair et al. 2018

If there are there multiple versions of the dataset, list the file updated, when and why update was made: Organized and added files to Github in 2022


--------------------------
METHODOLOGICAL INFORMATION
--------------------------

Description of methods used for collection/generation of data: 
	Collected fasta file of ancient dog mitogenomes from Ni Leathlobhair et al. 2018
	Using the sequences in that fasta file, created python scripts to generate a sliding scale to pull out the sequences given a specified length that overlapped the genome because mtDNA is circular. Used python scripts to create BEAST files (.xml) for Bayesian phylogenetic analysis to evaluate the changes in topology associated with sequence length and location within the sequence.

Methods for processing the data: 
	Used python3, BEAST 2.5, Treeannotator, and University of Iowa's HPC (Argon)

Software- or Instrument-specific information needed to interpret the data, including software and hardware version numbers:
	Figtree to view tree topologies

Standards and calibration information, if appropriate: N/A

Environmental/experimental conditions: N/A

Describe any quality-assurance procedures performed on the data: N/A

People involved with sample collection, processing, analysis and/or submission:
	Dr. Andrew Kitchen



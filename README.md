This is a Python script to automate inclusion/exclusion based on a set of abstracts. It was originally developed as part of a large scale scoping review of English medium instruction research, but the code would work in any domain. 

While the code words as code, it is important to test how well ChatGPT is evaluating your abstracts. You can use an inter-rater reliability statistic to measure this. Particularly, Kripendorff's Alpha is useful because it can be used with ordinal data like include/unsure/exclude. 

What it does:

- Loads a .csv file of research abstracts. 

- Applies a user-defined prompt to each abstract and sends it to the OpenAI API. 

- Saves those responses to a new .csv

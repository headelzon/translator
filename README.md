<h1>Automatic Translator</h1>
The project is a program that will help my mother with translation work.<br><br> 
A lot of her work consist of "re-translating" car documents, which are basically a few tables, most of them very similar to each other. She must retype values from a scan or physical document to the ready document she once prepared.<br> 
Instead of rewriting the values from one cell to another, I plan the program to <b>automatically detect the table, segment the image and read the text from each cell.</b><br><br>
Second part of the program will <b>write the read values to the Word document</b>, prepared before.<br> 
Additional part of the program will consist of Graphical User Interface. As my mother is not very familiar with computers in general, she would need a simple GUI.<br><br>

Plan of the program as for <code>Apr 16</code><br>
Using the OpenCV lib for Python: 
<ol><li>Read in the image</li>
<li>Image preprocessing:</li>
<ul><li>Convert to binary</li>
<li>Use opening to get rid of noise</li>
<li>Straighten and crop the image</li></ul>
<li>Use probabilistic Hughes line detection algorithm</li>
<li>Image segmentation (<i>each cell of the table should be recognized compared to the destination table</i>)</li>
<li>OCR text from each segment</li>
<li>Write in text fragments into corresonding table cells in the Word document</li>
<li>Create simple GUI (probably using PyQt)</li>
</ol>

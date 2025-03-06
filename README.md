# zero-shot-protein-segmentation



How to perform zero-shot protein segmentation locally:

1. Clone this repository to your computer
2. Install anaconda, create a new conda environment using zps.yml, and activate this environment (for more detailed instructions see https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
3. open zero_shot_protein_segmentation.py and set your desired options, including if and where to save embeddings
4. run zero_shot_protein_segmentation.py



How to perform zero-shot protein segmentation using Colab:

1. Open https://colab.research.google.com/ in a new tab or window. You may need to log in to your google account
2. From the "open notebook" menu select "GitHub"
3. Enter github URL: "moses-lab/zero-shot-protein-segmentation/"
4. Click on the notebook "/zero-shot-protein-segmentation/zero_shot_protein_segmentation_colab.ipynb"
5. Change your session to use GPU
    a. Click connect on the top right hand corner
    b. Select "View Resources" from the drop down menu at the top right hand corner (this will open up a menu on the right side of the colab notebook)
    c. Click "Change runtime type" and select a GPU option
6. Run blocks of code by clicking on the top left hand corner "play" button (You do not have to run the blocks of code that save the results - some of these generate large data files)
7. To download saved results from colab to your computer: 
    a. Click on the file folder icon on the left and you should be able to see your file(s) 
    b. Click on the 3 vertical dots directly to the right of the file name and select "Download"
    c. If the file does not appear immediately, click on the refresh button in the file folder sub menu (just below the "Files")
Note: files generated in this colab session might be deleted from colab when the window is closed.
Note: you can upload your own fasta sequences to colab in the session or through google drive 




Copyright Statement version 2.0 copyright 2025 by Ami Sangster. This software is provided "as is" without warranty of any kind. The author assumes no responsibility for the results it produces or conclusions based thereupon. It is distributed free of charge for academic use only. Permission to copy and use it is granted free of charge provided that no fee is charged and this copyright notice is not removed.

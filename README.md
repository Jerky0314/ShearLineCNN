## Shear Line CNN

### Preprocessing
1. The proponent manually annotated weather data (2010-2020) with shear line occurences.
2. The annotation generated `388` "shear line" source-target pairs.
3. The remaining unannotated samples from the original dataset (2010-2020) constituted the "no shear line" superset.
4. From the "no shear line" superset, `388` samples were randomly selected (using Python).
5. A total of `766` samples constituted the final dataset, with balanced classes.
6. In both "shear line" and "no shear line" **sources**, the `u,v` components for each samples were paired along the `x,y` axis.
	- This preprocessing constituted to the final set of classes.
7. In the annotated "shear line" **targets**, the matrices denoting the shear lines were extracted.
	- This preprocessing constituted the the final set of "shear line" targets.
	- A zero-filled matrix represent the target area, with the ones denoting the shear line path.
8. The final set of "no shear line" **sources** was used to generate its corresponding targets.
	- A matrix of shape 161x141 pixels, filled with zeros, was programmatically generated.
9. This series of preprocessing ensures that both source classes were balanced and with corresponding target pairs.
	- Balancing the classes avoids bias in the training process.

## Dimensions

```txt
[shape]
 * input: (161, 141, 2)
 * output: (161, 141)

[matrix]
 * 161 is the y-axis (height)
 * 141 is the x-axis (width)
 * 2 is the (u,v) wind components
```

## Local Execution (PC)
1. Clone the repository to your local PC.  
	- Alternatively, you may just download and unzip its ZIP file.  
2. Open the project repository in Command Prompt.  
	- Run: `pip install -U virtualenv`  
	- Run: `virtualenv venv`  
	- Run: `activate.cmd`   
    - If `requirements.txt` is not present, run each line:
```cmd
pip install -U jupyterlab
pip install -U notebook
pip install -U opencv-python 
pip install -U scikit-learn
pip install -U scikit-image
pip install -U matplotlib
pip install -U seaborn
pip install -U tensorflow
pip install -U tabulate
pip freeze > requirements.txt
git add .
git commit -m "[env] Add `requirements.txt` file"
git push -u origin main
```  
3. In the same Command Prompt, launch the annotation tool.  
	- Run: `jupyter notebook`  
	- Wait until the webpage is loaded.  
	- Locate and click the `ShearLineCNN.ipynb` file.
4. Run the cells sequentially.
	- Wait until each cell is completed.
5. Gradually adjust the hyperparamters until an acceptable accuracy is reached.

## Google Colab Environment
1. Clone the `ShearLineCNN` to your PC.
	- Run command: `git@github.com:rmaniego/ShearLineCNN.git`
2. Create your own `ShearLineCNN` repository on the GitHub website.
	- Copy the SSH clone URL, something like: `git@github.com:Jerky0314/ShearLineCNN.git`
3. On the same command prompt, run the following:
```cmd
cd ShearLineCNN
git remote set-url origin git@github.com:Jerky0314/ShearLineCNN.git
git add .
git commit -m "[cnn] Add project to GitHub"
git push -u origin main
```
4. Go to your own GitHub account.
5. Go to https://github.com/settings/tokens.
6. On the sidebar, select Fine-grained tokens.
7. Fill-up appropriate details, limit read/write access.
8. Copy generated PAT to Google Colab secrets.

## Local Execution (PC)  

1. 
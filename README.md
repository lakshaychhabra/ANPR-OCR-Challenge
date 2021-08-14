# ANPR-OCR-Challenge

The aim of the Challenge is to use OCR techniques on a given dataset and extract the Number Plate information. 
Few number plate samples are in bad orientation, bad light and are blurred.

Here in this repo we are using PaddleOCR.
Why PaddleOCR and not Tesseract(Being a popular one)?

> Well In past I have worked on Tesseract so thought of trying something new and PaddleOCR is new and gives promising results.

### Files Description:

    ocr.py: This is the main file that runs OCR on Images and saves the result in a CSV file.

    utils.py: This file contains helper functions to improve the acuracy of our approach.

    get_metrics.py: This file combines the test csv and our predicted labels, and give us the final accuracy.

    dataset_predicted_updated.csv: This file contains our predicted values.

    combined_updated.csv: This file is combination of actual lables (dataset.csv) and predicted labels (dataset_predicted_updated.csv)

### Summary:

We started with the default paddle ocr settings and in the end got 30% exact matching with test labels. Then I noticed that the texts are getting split due to size issues caused by orientation/tilted images. So I added a custom logic which takes into account the area of the detected texts and then join them together on basis of a threshold value. I also removed special characters from the output which boosted my accuracy to ~53% exact match. There were few rows which had only one wrong character recognition that can be corrected on further processing. <br>

### Future Scope:
1. We can use Morphological operations to preprocess the images and remove some noise in them.
2. We can also use prespective transformation to align the number plates correctly so number can become more clear.
3. We can also use Tesseract and then compare the results of both the approach.
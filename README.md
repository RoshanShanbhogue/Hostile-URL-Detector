# Hostile-URL-Detector (HUD)

* This is a multi-staged URL analysis tool to provide useful insights about an input URL.

* With the massive strides in digital technology and popularization of internet, data
  security and privacy comes under an alarming risk of being violated. Several attacks like
  phishing, defacement and malware have been a constant threat to the data of not only big
  corporations but also an internet using individual. These attacks are mostly motivated by
  financial gains like in the case of several phishing attacks where the link/URL (Uniform
  Resource Locator) may redirect the user’s data to a different hidden URL causing unwanted harm. 

* In this project we refer anything harmful whether financial, social or mental as **hostile**. 
  We have proposed a methodology to detect or classify an input URL into one of the attack types
  and provide the user with more information about the URL they are to visit. Here, we have made
  large set of labelled links (**1,89,780 URLs**- which is a combination of URLs taken from various
  sources and contains the types – **malware, malicious, adult, phishing, defacement and spam**)
  on which we perform lexical feature extraction to gain more information about the link (to
  extract literary features) and various novel features which we have proposed are also extracted.
  
* In total, we extracted 62 features and gained the highest predictive accuracy of 99.54% using random forest
  classifier.

## About the code

* Python was used to code the entire project as:
  * It gives easy access to supervised machine learning algorithms with **sklean** and libraries like **numpy** and **pandas**.
  * Provides **tkinter** to make simple GUI.
  * Easy to code and simple to understand data structures and computing logic.





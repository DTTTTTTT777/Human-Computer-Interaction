# Report - Information Retrieval

- Course: Human Computer Interaction
- Student Name: Duan Tingting
- Student ID: 2152402
- Tutor: Deng Hao



[TOC]

## 1. Introduction

This project presents the design and implementation of an image search system interface based on the Five-Stage Framework. The objective is to develop a user-friendly and efficient platform that enables users to upload images, retrieve relevant search results, filter retrieved images by tags and add them to the a personalized favorite list. 

## 2. The requirements of an image search task

1. **Image Upload** (<u>Formulation</u>): The interface should provide an input box or file upload option to allow users to upload an image as a query for the search. 

2. **Query Image Preview** (<u>Formulation</u>): The interface should display a preview of the uploaded query image in the searching window. This preview will help users verify if the correct image has been uploaded before initiating the search. 

3. **Search Button** (<u>Initiation</u>): A search button should be available to initiate the image search process once the query image is uploaded.

4. **Result Overview** (<u>Review</u>): After the search is performed, the interface should provide an overview of the results. This overview could include the total number of results found, displayed prominently to give users an idea of the search output.

5. **Search Parameter Modification** (<u>Refinement</u>): Users should have the ability to modify search parameters or refine their search. For example, they should be able to select specific categories or tags related to the image to narrow down the search results.

6. **Favorite List** (<u>Use</u>): The interface should allow users to take actions on the search results, such as adding selected images to a favorite list. This feature enables users to save and access their preferred images for future reference.

7. **Additional Functions**:

   **a. Image details and metadata**: Displaying additional information about each image, including tag and whether it is in the favorite list, can help users make informed decisions.

   **b. Filtering**: For the tags of images are displayed, users may want to filter the search results based on tags. The interface will display the tags associated with the search results, allowing users to select a specific tag and view only the corresponding search results.

   **c. Favorite list management**: Users can select certain images from the search results and add them to their favorite list. Additionally, they have the option to remove images from the favorite list that are already present in the search results. Users can conveniently access and view their favorite list, and delete any undesired images from it.

## 3. My designs for Five-Stage Search Framework

Below, I will elaborate on my design for each stage, presenting a concise overview followed by illustrations of the resulting pages after various actions are performed.

### 3.1 Formulation

The interface incorporates a "Choose File" button, enabling users to select and upload a local image file as the query image for the search. Adjacent to the button, there is a prompt indicating whether an image has been uploaded. If an image has been uploaded, the interface displays the file name and a thumbnail preview of the image to facilitate user verification.



**Home page**：

![image-20230525133800484](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525133800484.png)



**Upload an image file**：

![image-20230525134542841](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525134542841.png)



### 3.2 Initiation of action

The interface features a "Search Similar Images" button, which users can click after uploading the image to initiate the search for similar images. Upon clicking the button, a loading icon is displayed on the interface to indicate that the search process is underway.



**Click the “Search similar images” button：**

![image-20230525134614644](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525134614644.png)



### 3.3 Review of Results

Once the search is completed, the interface presents the total number of search results (fixed at 9 images in this case), along with thumbnail previews of all the search result images. Additionally, the images' associated tags and their favorite status are displayed, allowing users to review and utilize the search results.



**Upon comleting the search**：

![image-20230525134644788](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525134644788.png)



### 3.4 Refinement

The interface displays the collection of tags associated with the search results. By clicking the "Filter" button, users can access a list of available tags. Clicking on a desired tag enables users to view only the search result images associated with that specific tag, disregarding others.



**Click the “Filter” button**：

![image-20230525134801111](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525134801111.png)



**Click “structures”**：

![image-20230525134933247](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525134933247.png)



**Click “sunset”**：

![image-20230525135045143](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525135045143.png)



**Click “all”**：

![image-20230525135118230](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525135118230.png)



### 3.5 Use

After completing the search, users have the option to add their preferred images to a favorite list or remove them from it. The interface provides a "View favorites" button, which, upon clicking, allows users to access and view the images in their favorite list. From there, users can also remove any undesired images. It is important to note that performing multiple searches or clicking the "Clear" button will not clear the images from the favorite list or alter their favorite status. In other words, the act of favoriting an image is persistent and enduring.



**Click some “✰” buttons ; the page will allert user and buttons will turn into “★”**：

<img src="C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140219640.png" alt="image-20230525140219640" style="zoom:50%;" /> 

![image-20230525135601472](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525135601472.png)



**Initiate a new search(regardless of whether the "Clear" button is clicked or not) ; the favorite list will not be cleared**：

![image-20230525140006288](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140006288.png)



**Click the “★” button to remove an image from the favorite list**：

<img src="C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140354910.png" alt="image-20230525140354910" style="zoom:50%;" /> 

![image-20230525140158398](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140158398.png)



**Click the “View favorites” button**：

![image-20230525140605408](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140605408.png)



**Click the “★” button to remove an image from the favorite list**：

<img src="C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140354910.png" alt="image-20230525140354910" style="zoom:50%;" /> 

![image-20230525140806238](C:\Users\DTTTTTTT\AppData\Roaming\Typora\typora-user-images\image-20230525140806238.png)


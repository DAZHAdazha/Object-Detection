# Result Preview (demo)
![](https://github.com/DAZHAdazha/Final-Project/tree/main/images)
# 1.Objectives & Significance

Object detection has always been of great significance in the field of computer vision whose main objective is to enable the computer to accurately classify the objects in a given picture or video and find the position of each object. In recent years, many computer vision researchers at home and abroad have developed a large number of excellent object detection neural network algorithms, including Faster R-CNN, SSD, YOLO. The goal of this project is to select appropriate object detection algorithms and data sets and train the deep learning model, then develop a website for users which allows users to complete object detection tasks easily.  

From the perspective of research, the significance of object detection is that object detection is one of the fundamental tasks in the field of computer vision, which is also the basis of many other high-level tasks: image classification, face recognition, target tracking, pedestrian re-recognition. Meanwhile, there is a large number of well-known research teams both at home and abroad, had been focused on the field of object detection, for instance, MIT Computer Science and Artificial Intelligence Laboratory, Stanford Computer Vision Lab, National Laboratory of Pattern Recognition of Chinese Academy of Sciences, LAMDA Institute of Nanjing University. 

While from the perspective of the application, object detection has shown a wide range of practical usages: face detection technology, pedestrian detection technology applied in video surveillance, entrance and exit statistics, traffic sign detection technology, vehicle detection technology applied in aided driving, automatic driving. At the same time, major technology companies, for example, Microsoft, Google, Ali, and Baidu, have also spent a lot of manpower and material resources to explore the object detection field, which indicates the significance and prospect of object detection.

# 2. Background Research

Since 2006, in the lead of Hinton, Bengio, Lecun, and other researchers, a large number of deep neural network papers have been published, especially after Hinton's research group participated in the ImageNet image recognition competition in 2012 and won the championship using AlexNet, constructed by CNN network, then neural network began to receive extensive attention from then on. 

Computer vision analysis of target motion can be roughly divided into three levels: motion segmentation and object detection, target tracking, action recognition, and behavior description. Object detection is not only one of the basic tasks to be solved in the field of computer vision, but also the basic task of video surveillance technology among the other tasks. However, object detection is still a challenging task with great potential and space for improvement, since the objects in the video have different poses and often appear to overlap, especially when their movements are irregular. Meanwhile, the resolution, weather, illumination, and other conditions of the surveillance video or images as well as the diversity of scenes should also be taken into consideration, which makes this task more challenging. 

Overall, object detection is a task to find all the objects of interest in the image for two sub-tasks, including object positioning and object classification. The traditional object detection method, for example, the sliding window algorithm is generally divided into three stages: firstly, select some candidate regions on a given image, then extract features from these regions, and finally classify them using trained classifiers.

At present, the mainstream object detection algorithms are mainly based on a deep learning model, which can be roughly divided into two categories:  (1) One-stage object detection algorithm. This kind of detection algorithm does not need the Region Proposal Stage and can directly generate the category probability and position coordinates of objects through only one stage, One-stage typical algorithms include YOLO, SSD, and CornerNet.  (2) Two-stage object detection algorithms divide detection problems into Two stages, the first stage is the generation of Region Proposals, which includes the approximate location information of the object, and the second stage is the classification and location refinement of the candidate regions. The representatives of two-stages algorithms are R-CNN.  Fast R-CNN, Faster R-CNN. 

The main performance indicator of the object detection model is the accuracy and processing speed, and the accuracy mainly considers the positioning and classification accuracy of the object. In general, the two-stage algorithm has advantages in accuracy, while the one-stage algorithm has advantages in processing speed. 

(1) SSD stands for Single Shot MultiBox Detector, is a single-stage, multiple proposal object detection algorithm, SSD use CNN network to detect with multi-scale feature map.

Additionally, SSD adopts VGG16 as the basic model, and then adds a convolution layer based on VGG16 to obtain more feature maps for detection. 

(2) Faster R-CNN, after the evolvement of R-CNN and Fast R-CNN, Ross B. Girshick proposed Faster R-CNN in 2016. In terms of structure, the Faster R-CNN integrated feature extraction, bounding box regression (rect refine), and classification into one network, which greatly improves the overall performance, especially in the detection speed.

 

Yolo, stands for You Only Look Once, which adopts a separate CNN model to achieve end-to-end object detection. The input image is resized and sent to the CNN network, then the detected object results are obtained by processing network prediction. Compared with the R-CNN algorithm, it is a unified framework with faster speed while the training process of Yolo is also end-to-end. 

 

In general, object detection is an active research direction in the field of computer vision. Although one-stage detection algorithm and two-stage detection algorithm have achieved good results, there is still a great potential for promotion for application in real scenes, and this is also a meaningful and challenging topic for now and future.

Reference

[1] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification with deep convolutional neural networks,” in Advances in neural information processing systems, 2012, pp. 1097–1105.

[2] Vishwakarma S, Agrawal A. A survey on activity recognition and behavior understanding in video surveillance [J]. The Visual Computer, 2012: 1-27.

[3] Girshick, R., Donahue, J., Darrell, T., Malik, J.: Rich feature hierarchies for accurate object detection and semantic segmentation. In CVPR 2014.

[4] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. Faster R-CNN: Towards real-time object detection with region proposal networks. In Neural Information Processing Systems (NIPS), 2015.

[5] Redmon, Joseph, et al. "You Only Look Once: Unified, Real-Time Object Detection." (2015):779-788.

[6] Liu, Wei, et al. "SSD: Single Shot MultiBox Detector." European Conference on Computer Vision Springer International Publishing, 2016:21-37.S

# 3. Task and Requirement

The task of this project is to carefully research into object detection area, read and comprehend relative papers to obtain an overall understanding of the current research status of this topic from both national and international perspectives.

Specifically, the task requires diving into the background research from deep learning history to computer vision tasks (including image classification, location, object detection, instance segmentation), then focus on object detection deeply, by understanding the basic thought and implementation of mainstream algorithms: Yolo (You Only Look Once), Faster R-CNN, SSD; comparing the suitable object detection dataset: VOC, COCO, ImageNet; comprehending the benchmark and indicators to evaluate results. After selecting an optimal deep learning algorithm and corresponding datasets, training on a variety of pre-trained models should be carried on, companies with evaluation and promotion on each round of training, in order to enhance model performance. The requirement of the deep learning module should be referred to the corresponding benchmark with indicators: recall, processing speed, average precision.

For the web page implementation, choices of front-end and back-end frameworks (Vue + Python Flask) should be carefully investigated, a proposed implementation of the website should be able to handle the uploading and downloading images or videos from users, processing the images by sending them to encapsulated deep learning API, then sending object detection results back to the user. The requirement of web page implementation should include consideration of user experience, the aesthetics of web pages, standardized API. 

Finally, a paper should be constructed by incorporating the research work including background research, literature in the area and related work, objectives, experiment methods, evaluation, conclusion, reference. The language of the paper should be clear and structural, logically explaining the process of the detailed project, in company with suitable figures, graphs, and tables.

 # 4. Technique Stack

The research approach in this project is divided into two parts: deep learning module and web page module.

In the deep learning module, this project will take into consideration using the state of art object detection algorithm Yolo-v5 as the basis, implemented by Pytorch, as the main component. After implementation of the code that used to transform the dataset into a suitable format, four different pre-trained models (s-small, m-medium, l-large, x-extra) will be trained separately with the dataset VOC 2007 for epochs, evaluation graphs will be made based on dataset benchmark and important indicators: accuracy, average precision, recall, processing speed.

In the web page module, the front-end part will use Vue as front-end skeleton, displaying the representation layer for the user to upload image or video and download results, while Python Flask will be adopted as back-end routers which will call deep learning module to process image or video for object detection tasks.



# 5. Proposal Deliverable

The proposal deliverable of the project should be a software form, which consisted of two main parts, a deep learning module, and a web module. 

The deep learning module should include Pytorch based Yolo-v5 algorithm implementation, weights that trained from datasets VOC2007, code that used to transform dataset format, encapsulated API that process image and videos for object detection tasks.

The web module will contain both front-end and back-end parts. The front-end page will be implemented based on the Vue framework, providing interaction for users to upload images or videos and download object detection results. While the back-end will provide processing routers to call deep learning API, and also record corresponding logs during each process (time, process speed, size).

Additionally, a paper will be constructed as a deliverable of this project, which including the background research, literature in the area and related work, objectives, experiment methods, evaluation, conclusion, reference, in order to demonstrate the whole process and experient details during the project.

 

# 6. Plan

9.20 - 10.8 Complete the project outline and plan, discuss the topic and laboratory usage in the project with the supervisor.

10.9 - 10.17 Object Detection background research:

(1) Basic background research about the general deep learning field on its significance, current application, bottleneck, and future development. 

(2) Background research on object detection and related tasks: classification, location, instance segmentation, and read relevant papers. 

(3) Research on object detection algorithms, for instance, Yolov5, Faster R-CNN (refer to R-CNN, Fast R-CNN as the basis), and SSD, then summarize the advantages and disadvantages of each algorithm. 

(4) Investigate web front-end back-end technology, Python Flask backend framework, and Vue front-end framework. 

(5) Research on object detection dataset, compare VOC, COCO, ImageNet, and select one data set for training. 

(6) Investigate basic indicators and benchmarks related to object detection, read relevant papers, and acquainted with the process for subsequent model evaluation. 

10.18 - 10.25 Prepare for the Thesis Proposal Defense:

 (1) Write the Thesis Proposal Report.

 (2) Prepare the Thesis Proposal Defense slide.

 (3) Prepare the Thesis Proposal Defense presentation.

10.25 - 11.30 Determine the project structure and technology stack, built the development environment, and complete the basic demo: 

 (1) The basic construction of front and back end modules and deep learning framework (technology stack: Vue + Flask + Pytorch + Yolov5)

 (2) Build Anaconda deep learning development environment and install related dependent libraries. 

 (3) Implement data set format conversion code.

 (4) Complete the demo based on the pre-training model, test the object detection accuracy of pictures, videos, and cameras. 

12.1 - 12.31 Start training on multiple pre-training weights:

 (1) Record loss, AP, recall, and other important indicators of each training. 

 (2) Visualize the training results and record the continuous trend of loss, AP and Recall. 

 (3) Record the processing speed of each image predicted by the model.

 (4) Evaluate the training results, use test sets to evaluate the training results, and formulate improvement plans according to the situation. 

 (5) Initial the setup of the front-end page(using Node.js and Vue framework). 

 (6) Write Project Outline and Plan.

1.1 - 1.31 Continue the remaining development tasks:

 (1) Develop and beautify the web page, add status hints and other information to improve user experience. 

 (2) Complete the interface for accessing web pages at the back end, including uploading and downloading pictures. 

 (3) Complete the deep learning Yolo-v5 image object detection module and encapsulate the image object detection processing interface. 

2.1 - 2.28 Continue remaining development tasks and paper writing:

 (1) Complete the front-end upload and download displaying layer for object detection based on the video. 

 (2) Implement a back-end interface to complete video detection. 

 (3) Complete the deep learning Yolo-v5 object detection module based on video and encapsulate the object detection based on the video processing interface.

 (4) Design charts based on previous work (training and test samples, comparison with benchmark) 

 (5) Begin to write the abstract, introduction, and literature review of the paper. 

3.1 - 3.15 Continue to write the paper and prepare for the mid-term examination:

 (1) Continue to write the research method, experimental process, and conclusion part of the paper. 

 (2) Prepare the slide for mid-term examination and defense. 

 (3) Prepare demo of mid-term examination project. 

3.16 - 3.31 Roughly complete the paper writing

 (1) Complete writing the final parts: evaluation and citation of the paper.

 (2) Polish and modify the language and structure of the paper. 

4.1 - 4.20 Prepare for Thesis Defense 

 (1) Prepare slide for Thesis Defense.

 (2) Prepare for the Thesis Defense presentation.

 (3) Consider the advantages and disadvantages of the project, and prepare incoming questions in the defense. 


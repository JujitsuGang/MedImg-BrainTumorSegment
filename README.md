In the world of diagnostics, the intersection of AI and computer vision is proving to be transformative. Precise segmentation of tumors from 2D MRI scans is one such application that's being revolutionised. A Python-based graphical user interface (GUI) created with PyQt5 and OpenCV powers this project.

To segment images, a sequence of image processing steps are used:
1. **Selective Insights:** The first step is to select the image that's to be segmented.
2. **Bilateral Refinement:** A bilateral filter is then applied to preserve finer details while suppressing noise.
3. **Median Transformation:** A median filter is applied to smoothen the image whilst preserving important structures.
4. **Gaussian Symphony:** A Gaussian filter is then used to mix and enhance the image's contours.
5. **Thresholded Precision:** Thresholding is applied to denote the image's essence.
6. **Dilation and Morphology:** Dilation and morphological operations are used for deeper intuition.
7. **Color Mapping Elegance:** Finally, a color map is added to create a dynamic image.
8. **Preserving the Epiphany:** The segmented image is saved.

This project serves as a glimpse into the convergence of AI and computer vision in the realm of medical care. Through it, the medical industry is witnessing a fusion between human expertise and cutting-edge technology. The promise is a shift in the way patient wellbeing is perceived and catered to.

![Project GUI](https://user-images.githubusercontent.com/27898184/84681701-f79fa980-af4d
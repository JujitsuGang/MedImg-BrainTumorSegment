In the world of diagnostics, the intersection of AI and computer vision is proving to be transformative. Precise segmentation of tumors from 2D MRI scans is one such application that's being revolutionised. A Python-based graphical user interface (GUI) created with PyQt5 and OpenCV powers this project.

To segment images, a sequence of image processing steps are used:
1. **Selective Insights:** The first step is to select the image that's to be segmented.
2. **Bilateral Refinement:** A bilateral filter is then applied to preserve finer details while suppressing noise.
3. **Median Transformation:** A median filter is applied to smoothen the image whilst preserving important structures.
4. **Gaussian Symphony:** A Gaussian filter is then used to mix and enhance the image's contours.
5. **T